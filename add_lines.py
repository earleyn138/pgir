import numpy as np
from astropy.io import ascii

wdir = '/Users/earleyn138/Library/Mobile Documents/com~apple~CloudDocs/Research/grad/science/pgir/pgir_vars/'
speclines = ascii.read(wdir+'sun_spectral_lines.csv')
mol_bands = ascii.read(wdir+'molecular_bands.csv')
H_lines = np.sort(np.array(
    [0.410, 0.434, 0.486, 0.656, 1.875, 1.282, 1.094, 1.005, 0.954, 2.625, 2.166, 1.944, 1.817, 1.458, 2.279, 1.94509,
     1.81791, 1.73669, 1.68111, 1.64117, 1.61137, 1.58849, 1.57050, 1.55607, 1.54431, 1.53460, 1.52647, 1.51960,
     1.51374]))
C12O16 = np.array([2.2935, 2.3227, 2.3525, 2.3829, 2.4141])
C12O18 = np.array([2.3492, 2.3783, 2.4385])
C12O17 = np.array([2.3226, 2.3517, 2.3815, 2.4119])
C13O16 = np.array([2.3448, 2.3739, 2.4037, 2.4341])
HeI = np.array([1.0833, 1.701, 1.278, 2.059, 2.113, 2.165])
FI = np.array([1.008713, 1.018615, 1.020957, 1.028545, 1.029301, 1.03808, 1.042629, 1.086231])
cilines = speclines[np.where(speclines['Element'] == 'Ci')]
cilinemask = ((cilines['Wav'] > 1.0) & (cilines['Wav'] < 1.1)) | ((cilines['Wav'] > 1.15) & (cilines['Wav'] < 1.25))
OH = np.array(
    [1.0829, 1.0831, 1.0841, 1.0856, 1.0876, 1.0895, 1.0923, 1.0948, 1.0972, 1.1006, 1.1026, 1.1069, 1.1086, 1.1137,
     1.1152, 1.1211, 1.1285, 1.1288, 1.1292])
H2 = np.array([1.958, 2.0341, 2.0739, 2.1221, 2.1543, 2.2238, 2.2480, 2.4070, 2.4139, 2.4242, 2.4379, 2.2948])
Mg = np.array([1.5029, 1.5044, 1.5052, 1.7113, 2.1065, 2.1067, 2.2814])
MgII = np.array([1.7723])
Fe = np.array([1.5774, 1.5817, 1.7332, 2.0704, 2.2263, 2.2387])
Si = np.array([1.5892, 2.0923])
Al = np.array([1.6755, 1.7704, 2.1099, 2.1170])
Na = np.array([2.2062, 2.2090])
Ca = np.array([2.2614, 2.2631, 2.2657])
Ti = np.array([2.1790, 2.1855])
TiO = np.array([0.9725, 0.9814, 0.9899, 0.9986, 1.0025, 1.0137, 1.0250])


def add_IRlines(ax, ymn, ymx):
    """

    :param ax:
    :param ymn:
    :param ymx:
    :return:
    """
    l0 = ax.vlines(speclines[np.where(speclines['Element'] == 'Fei')]['Wav'], ymin=ymn, ymax=ymx, linestyle='-',
                   color='r', linewidth=0.5, alpha=1.0, label='Fei')
    l1 = ax.vlines(speclines[np.where(speclines['Element'] == 'Ci')]['Wav'], ymin=ymn, ymax=ymx, linestyle='-',
                   color='g', linewidth=0.5, alpha=1.0, label='Ci')
    l2 = ax.vlines(mol_bands[np.where(mol_bands['Molecule'] == 'CO12')]['wav'], ymin=ymn, ymax=ymx, linestyle='-',
                   color='b', linewidth=0.5, alpha=1.0, label='CO12')
    l3 = ax.vlines(mol_bands[np.where(mol_bands['Molecule'] == 'CN')]['wav'], ymin=ymn, ymax=ymx, linestyle='-',
                   color='b', linewidth=0.5, alpha=1.0, label='CN')
    l4 = ax.vlines(HeI, ymin=ymn, ymax=ymx, linestyle='--', color='gray', label='HeI')
    l5 = ax.vlines(speclines[np.where(speclines['Element'] == 'Nai')]['Wav'], ymin=ymn, ymax=ymx, linestyle='-',
                   color='orange', linewidth=0.5, alpha=1.0, label='Nai')
    l6 = ax.vlines(speclines[np.where(speclines['Element'] == 'Caii')]['Wav'], ymin=ymn, ymax=ymx, linestyle='-',
                   color='yellow', linewidth=0.5, alpha=1.0, label='Caii')
    l7 = ax.vlines(mol_bands[np.where(mol_bands['Molecule'] == 'C2')]['wav'], ymin=ymn, ymax=ymx, linestyle='-',
                   color='b', linewidth=0.5, alpha=1.0, label='C2')
    l8 = ax.vlines(speclines[np.where(speclines['Element'] == 'Sii')]['Wav'], ymin=ymn, ymax=ymx, linestyle='-',
                   color='blue', linewidth=0.5, alpha=1.0, label='Sii')
    l9 = ax.vlines(speclines[np.where(speclines['Element'] == 'Ki')]['Wav'], ymin=ymn, ymax=ymx, linestyle='-',
                   color='yellow', linewidth=0.5, alpha=1.0, label='Ki')
    l10 = ax.vlines(H_lines, ymin=ymn, ymax=ymx, linestyle='-', color='brown', linewidth=0.5, alpha=1.0, label='HI')

    l11 = ax.vlines(C12O16, ymin=ymn, ymax=ymx, linestyle='-', color='brown', linewidth=0.5, alpha=1.0, label='C12O16')
    l12 = ax.vlines(C12O18, ymin=ymn, ymax=ymx, linestyle='-', color='blue', linewidth=0.5, alpha=1.0, label='C12O18')
    l13 = ax.vlines(C12O17, ymin=ymn, ymax=ymx, linestyle='-', color='brown', linewidth=0.5, alpha=1.0, label='C12O17')
    l14 = ax.vlines(C13O16, ymin=ymn, ymax=ymx, linestyle='-', color='brown', linewidth=0.5, alpha=1.0, label='C13O16')
    l15 = ax.vlines(H2, ymin=ymn, ymax=ymx, linestyle='-', color='blue', linewidth=0.5, alpha=1.0, label='H2')
    l16 = ax.vlines(TiO, ymin=ymn, ymax=ymx, linestyle='-', color='purple', linewidth=0.5, alpha=1.0, label='TiO')
    lines = [l0, l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l13, l14, l15, l16]

    return lines
