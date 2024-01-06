import numpy as np
from specutils.spectra import Spectrum1D
from specutils.fitting import fit_generic_continuum
import astropy.units as u
from nirstid.masks import j_band_mask, h_band_mask, k_band_mask

def get_norm_values(wavs, fluxes, full_wavs, full_fluxes):
    """

    :param wavs:
    :param fluxes:
    :param full_wavs:
    :param full_fluxes:
    :return:
    """
    spectrum = Spectrum1D(flux=fluxes * u.Jy, spectral_axis=wavs * u.um)
    g1_fit = fit_generic_continuum(spectrum, median_window=1)
    contnm = g1_fit(wavs * u.um)
    #norm_flux = fluxes / contnm

    jfullmask, hfullmask, kfullmask = j_band_mask(full_wavs),h_band_mask(full_wavs),k_band_mask(full_wavs)
    jmask, hmask, kmask = j_band_mask(wavs), h_band_mask(wavs), k_band_mask(wavs)
    jflux, hflux, kflux = full_fluxes[jfullmask]/contnm[jmask], full_fluxes[hfullmask]/contnm[hmask], full_fluxes[kfullmask]/contnm[kmask]

    norm_flux = np.full(full_wavs.shape,np.nan)
    norm_flux[jfullmask], norm_flux[hfullmask], norm_flux[kfullmask] = jflux, hflux, kflux

    return full_wavs, norm_flux

