import numpy as np
import pandas as pd
from astropy.coordinates import SkyCoord
import astropy.units as u
from astroquery.simbad import Simbad
from astropy.io import fits


obs = pd.read_csv('/Users/earleyn138/Downloads/Gattini LAV census - complete_census.csv')
specs = '/Users/earleyn138/Library/Mobile Documents/com~apple~CloudDocs/Research/grad/science/pgir/pgir_vars/complete_census/spectra/'+obs['Run']+'/'+obs['specfilename']+'.fits'

customSimbad = Simbad()
customSimbad.add_votable_fields('otype')

names = np.array(obs['Names'])
ras = np.ones(names.size)
decs = np.ones(names.size)
classes = []
for i, s in enumerate(specs):
    with fits.open(s) as sp:
        head = sp[0].header
    try:
        c = SkyCoord(head['RA'], head['DEC'], unit=(u.hourangle, u.deg))
    except:
        c = SkyCoord(head['TCS_RA'], head['TCS_DEC'], unit=(u.hourangle, u.deg))

    result_table = customSimbad.query_region(c, radius=0.1 * u.deg)
    if result_table is not None and len(result_table) > 0:
        object_type = result_table['OTYPE'][0]
    else:
        object_type = 'None'
    classes.append(object_type)
    ras[i] = c.ra.deg
    decs[i] = c.dec.deg

headers = np.array(['Name', 'RA', 'DEC', 'Class'])
data = np.array([names, ras, decs, classes])
pd.DataFrame(data.T, columns=headers).to_csv('/Users/earleyn138/Downloads/coords.csv', index=None)
