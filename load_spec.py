import numpy as np
from astropy.io import fits
from nirstid.masks import full_spec_mask

def get_object_data(specname, get_mask=full_spec_mask):
    """

    :param specname:
    :param get_mask:
    :return:
    """

    with fits.open(specname) as spec:
        if len(spec[0].data.shape) == 3:
            full_wavs = np.ndarray.flatten(np.array([spec[0].data[3][0], spec[0].data[2][0], spec[0].data[1][0], spec[0].data[0][0]]))
            full_fluxes = np.ndarray.flatten(np.array([spec[0].data[3][1], spec[0].data[2][1], spec[0].data[1][1], spec[0].data[0][1]]))
        else:
            full_wavs, full_fluxes = spec[0].data[0], spec[0].data[1]

    # Gets full NIR spec mask
    mask = get_mask(full_wavs)

    # Masking bandpasses with limited atmospheric transmission, removing nans for normalization wrt continuum
    wavs, fluxes = full_wavs[mask], full_fluxes[mask]
    nanmask = np.invert(np.isnan(fluxes))
    wavs, fluxes = wavs[nanmask], fluxes[nanmask]
    sinds = np.argsort(wavs)
    wavs, fluxes = wavs[sinds], fluxes[sinds]

    # Keeping original arrays as well for plotting purposes later on, populating the masked values with nans
    # to prevent matplotlib from interpolating between the transmissive bandpasses
    full_fluxes[~mask] = np.nan

    return wavs, fluxes, full_wavs, full_fluxes


