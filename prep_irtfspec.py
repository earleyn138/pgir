import numpy as np
from astropy.io import ascii
from norm_spec import get_norm_values
from nirstid.masks import full_spec_mask

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

    # Masking bandpasses with limited atmospheric transmission, removing nans for normalization wrt continuum
    mask = get_mask(temp_full_wavs)
    temp_wavs = temp_full_wavs[mask]
    temp_fluxes = temp_full_fluxes[mask]

    # Keeping original arrays as well for plotting purposes later on, populating the masked values with nans
    # to prevent matplotlib from interpolating between the transmissive bandpasses
    temp_full_fluxes[~mask] = np.nan
    return temp_wavs, temp_fluxes, temp_full_wavs, temp_full_fluxes


def get_norm_template(template_filename, get_mask=full_spec_mask):
    temp_wavs, temp_fluxes,temp_full_wavs,temp_full_fluxes = get_irtf_data(template_filename, get_mask=get_mask)
    _, temp_norm_flux = get_norm_values(temp_wavs, temp_fluxes,temp_full_wavs,temp_full_fluxes)
    return temp_full_wavs, temp_norm_flux