import numpy as np
from astropy.io import fits,ascii
from astropy.time import Time
from specutils.fitting import fit_generic_continuum
#from specutils.fitting.continuum import fit_continuum
import astropy.units as u
from pgir.utilsvar.masks import full_spec_mask,j_band_mask, h_band_mask, k_band_mask
from specutils.spectra import Spectrum1D
from astropy.modeling.polynomial import Chebyshev1D
import warnings


def get_object_data(specname, get_mask=full_spec_mask):
    """

    :param specname:
    :param get_mask:
    :return:
    """
    warnings.filterwarnings("ignore", message="The following header keyword is invalid or follows an unrecognized non-standard convention:")
    with fits.open(specname) as spec:
        if specname.split('/')[-2].split('_')[0] == 'IRTF':
            spectime = Time(spec[0].header['Date_OBS']+'T'+spec[0].header['TIME_OBS']).jd
        else:
            spectime = Time(spec[0].header['UTSHUT']).jd
        if len(spec[0].data.shape) == 3:
            full_wavs = np.ndarray.flatten(np.array([spec[0].data[3][0], spec[0].data[2][0], spec[0].data[1][0], spec[0].data[0][0]]))
            full_fluxes = np.ndarray.flatten(np.array([spec[0].data[3][1], spec[0].data[2][1], spec[0].data[1][1], spec[0].data[0][1]]))
        else:
            full_wavs, full_fluxes = spec[0].data[0], spec[0].data[1]

    # # Gets full NIR spec mask
    # mask = get_mask(full_wavs)
    #
    # # Masking bandpasses with limited atmospheric transmission, removing nans for normalization wrt continuum
    # wavs, fluxes = full_wavs[mask], full_fluxes[mask]
    # nanmask = np.invert(np.isnan(fluxes))
    # wavs, fluxes = wavs[nanmask], fluxes[nanmask]
    # sinds = np.argsort(wavs)
    # wavs, fluxes = wavs[sinds], fluxes[sinds]
    #
    # # Keeping original arrays as well for plotting purposes later on, populating the masked values with nans
    # # to prevent matplotlib from interpolating between the transmissive bandpasses
    # full_fluxes[~mask] = np.nan
    wavs = full_wavs
    fluxes = full_fluxes
    return wavs, fluxes, full_wavs, full_fluxes,spectime


def get_irtf_data(template_filename, get_mask=full_spec_mask):
    """

    :param template_filename:
    :param get_mask:
    :return:
    """
    template = ascii.read(template_filename)
    template = template[template['col2']>0]
    temp_full_wavs = template['col1']
    temp_full_fluxes = template['col2']

    # # Masking bandpasses with limited atmospheric transmission, removing nans for normalization wrt continuum
    # mask = get_mask(temp_full_wavs)
    # temp_wavs = temp_full_wavs[mask]
    # temp_fluxes = temp_full_fluxes[mask]
    #
    # # Keeping original arrays as well for plotting purposes later on, populating the masked values with nans
    # # to prevent matplotlib from interpolating between the transmissive bandpasses
    # temp_full_fluxes[~mask] = np.nan

    temp_wavs = temp_full_wavs
    temp_fluxes = temp_full_fluxes

    return temp_wavs, temp_fluxes, temp_full_wavs, temp_full_fluxes


def get_norm_template(template_filename, lo, hi, get_mask=full_spec_mask):
    temp_wavs, temp_fluxes,temp_full_wavs,temp_full_fluxes = get_irtf_data(template_filename, get_mask=get_mask)
    #_, temp_norm_flux, temp_contnm = get_norm_values(temp_wavs, temp_fluxes,temp_full_wavs,temp_full_fluxes)
    temp_wavs, temp_norm_flux = get_norm_values(temp_wavs, temp_fluxes,temp_full_wavs,temp_full_fluxes,lo,hi)
    return temp_wavs, temp_norm_flux

def get_fritz_template(fritz_file, lo, hi):
    fritz_wav, fritz_flux, fritz_ferr = np.loadtxt('/Users/earleyn138/Downloads/mWTP20aachbe.fits.txt').T
    temp_wavs, temp_norm_flux = get_norm_values(fritz_wav*1e-4, fritz_flux,fritz_wav,fritz_flux,lo,hi)
    return temp_wavs, temp_norm_flux

def get_norm_values(wavs, fluxes, full_wavs, full_fluxes, lo,hi):
    """
    :param wavs:
    :param fluxes:
    :param full_wavs:
    :param full_fluxes:
    :return:
    """
    jwavs,jflux = wavs[j_band_mask(wavs)], fluxes[j_band_mask(wavs)]/np.median(fluxes[(wavs > lo) & (wavs < hi)])
    hwavs,hflux = wavs[h_band_mask(wavs)], fluxes[h_band_mask(wavs)]/np.median(fluxes[(wavs > lo) & (wavs < hi)])
    kwavs,kflux = wavs[k_band_mask(wavs)], fluxes[k_band_mask(wavs)]/np.median(fluxes[(wavs > lo) & (wavs < hi)])

    return [jwavs,hwavs,kwavs],[jflux,hflux,kflux]

    # jfullmask, hfullmask, kfullmask = j_band_mask(full_wavs),h_band_mask(full_wavs),k_band_mask(full_wavs)
    # jmask, hmask, kmask = j_band_mask(wavs), h_band_mask(wavs), k_band_mask(wavs)

    # norm_flux = np.full(full_wavs.shape,np.nan)
    # spectrum = Spectrum1D(flux=fluxes * u.Jy, spectral_axis=wavs * u.um)
    # #g1_fit = fit_generic_continuum(spectrum,median_window=1,model=Chebyshev1D(5))
    # g1_fit = fit_generic_continuum(spectrum, median_window=1)
    # contnm = g1_fit(wavs * u.um)
    #
    # for fm, mask in zip([jfullmask, hfullmask, kfullmask],[jmask,hmask,kmask]):
    #     # norm_flux_order = full_fluxes[fm]/contnm[mask]
    #     # norm_flux[fm] = norm_flux_order
    #     norm_flux_order = full_fluxes[fm] / np.nanmedian(full_fluxes[fm])
    #     norm_flux[fm] = norm_flux_order

    #
    # #region = [(1.0 * u.um, 1.34 * u.um), (1.42 * u.um, 1.8 * u.um), (2.1 * u.um, 2.47 * u.um)]
    # contnmlist=[]
    # # for fm, mask in zip([jfullmask, hfullmask, kfullmask],[jmask,hmask,kmask]):
    # #     spectrum = Spectrum1D(flux=fluxes[mask] * u.Jy, spectral_axis=wavs[mask] * u.um)
    # #     g1_fit = fit_generic_continuum(spectrum, median_window=1)
    # #     # g1_fit = fit_continuum(spectrum, window=region)
    # #     # contnm = g1_fit(wavs[mask] * u.um)
    # #     # contnmlist.append(contnm)
    # #     # norm_flux_order = full_fluxes[fm] / contnm
    # #     # norm_flux[fm] = norm_flux_order
    #
    # # jmask, hmask, kmask = j_band_mask(wavs), h_band_mask(wavs), k_band_mask(wavs)
    # # jflux, hflux, kflux = full_fluxes[jfullmask]/contnm[jmask], full_fluxes[hfullmask]/contnm[hmask], full_fluxes[kfullmask]/contnm[kmask]
    # #
    # # norm_flux = np.full(full_wavs.shape,np.nan)
    # # norm_flux[jfullmask], norm_flux[hfullmask], norm_flux[kfullmask] = jflux, hflux, kflux

    #return full_wavs, norm_flux, contnm