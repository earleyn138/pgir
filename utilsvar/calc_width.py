import matplotlib.pyplot as plt
from specutils.analysis import equivalent_width
from specutils.spectra import Spectrum1D
from specutils.spectra import SpectralRegion
from specutils.fitting import fit_generic_continuum
from specutils.manipulation import extract_region
import astropy.units as u
from astropy.modeling import models
from astropy.modeling import functional_models
from specutils.fitting import fit_lines
import warnings


def eqwidth(wavelength, flux, linecenter, lineregion, specregion,save_fig=False,fig_name=None):
    spectrum = Spectrum1D(flux * u.Jy, spectral_axis=wavelength * u.micron)
    sub_reg = SpectralRegion(specregion[0] * u.um, specregion[1] * u.um)
    sub_spectrum = extract_region(spectrum, sub_reg)

    warnings.filterwarnings("ignore", message="Model is linear in parameters; consider using linear fitting methods.")
    g1_fit = fit_generic_continuum(sub_spectrum, median_window=1)
    x = sub_spectrum.spectral_axis
    contnm_flux = g1_fit(x)

    norm_spec = Spectrum1D((sub_spectrum.flux / contnm_flux) * u.Jy, spectral_axis=x)

    # Gaussian model
    g_init = models.Gaussian1D(amplitude=1. * u.Jy, mean=linecenter * u.micron, stddev=0.001 * u.micron)

    # Voigt model
    #g_init = functional_models.Voigt1D(amplitude_L=1. * u.Jy, x_0=linecenter * u.micron, fwhm_L=0.001 * u.micron, fwhm_G=0.001 * u.micron)


    spec_fit = fit_lines(norm_spec-1*u.Jy, g_init, window=(lineregion[0]*u.um, lineregion[1]*u.um))
    y_fit = spec_fit(x)
    model_spec = Spectrum1D(y_fit, spectral_axis=x)

    eqw_micron = equivalent_width(model_spec+1*u.Jy, regions=SpectralRegion(lineregion[0] * u.micron, lineregion[1] * u.micron))
    eqw = eqw_micron.to(u.angstrom)

    if save_fig:
        fig,ax = plt.subplots(figsize=(10, 7))
        ax.plot(x, norm_spec.flux)
        ax.plot(x, model_spec.flux+1*u.Jy)
        ax.set_title('Equivalent Width = '+str(eqw))
        ax.axvline(lineregion[0],alpha=0.5,color='k',ls='--')
        ax.axvline(lineregion[1],alpha=0.5,color='k',ls='--')
        plt.savefig(fig_name,bbox_inches='tight')
        plt.close()
        print('Calculated equivalent width ', fig_name)

    return eqw

