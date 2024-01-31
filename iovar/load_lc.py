import numpy as np
import json

def get_gattini_lc(json_file):
    """

    :param json_file:
    :return:
    """

    with open(json_file) as f:
        data = json.load(f)
    time, mag, umag, lims, snr = [], [], [], [], []

    for ep in data:
        timepoint = data[ep]
        t, m, um = timepoint['jd'], timepoint['mag_ap2'], timepoint['magerr_ap2']
        time.append(t)
        mag.append(m)
        umag.append(um)
        ml, msnr = timepoint['maglim_ap2'], timepoint['magsnr_ap2']
        lims.append(ml)
        snr.append(msnr)

    time, mag, umag, lims, snrs = np.array(time), np.array(mag), np.array(umag), np.array(lims), np.array(snr)

    return time, mag, umag, lims, snrs
