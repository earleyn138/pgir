import astropy.units as u
from specutils import SpectralRegion
from specutils.spectra import Spectrum1D
from specutils.fitting import fit_generic_continuum
from specutils.manipulation import noise_region_uncertainty
from specutils.fitting import find_lines_threshold
from iovar.load_spec import get_object_data



def find_lines(spec_path, namegroup,line_dir):
    noise_region = SpectralRegion(1 * u.um, 2.4 * u.um)
    for n, s in zip(namegroup,spec_path):
        name = s.split('/')[-2]+'_'+n
        print(n, 'Finding lines ', s)
        w, f, fw,ff = get_object_data(s)
        spectrum = Spectrum1D(flux=f * u.Jy, spectral_axis=w * u.um)
        g1_fit = fit_generic_continuum(spectrum, median_window=1)
        contnm = g1_fit(w * u.um)
        norm = f*u.Jy/contnm*u.Jy
        spectrum = Spectrum1D(flux=norm, spectral_axis=w * u.um)
        spectrum = noise_region_uncertainty(spectrum, noise_region)
        lines = find_lines_threshold(norm, noise_factor=3)
        lines.write(line_dir+name+'_lineinfo.csv')