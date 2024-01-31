import numpy as np
import lineid_plot
import matplotlib as mpl
import pandas as pd
from pgir.utilsvar import masks


work_dir = '/Users/earleyn138/Library/Mobile Documents/com~apple~CloudDocs/Research/grad/science/'
irtf_dir = work_dir + '/irtf_spectra/All_text_091201/'
data_dir = work_dir + 'pgir/pgir_vars/complete_census/'

# wdir = '/Users/earleyn138/Library/Mobile Documents/com~apple~CloudDocs/Research/grad/science/pgir/pgir_vars/'
# speclines = ascii.read(wdir+'sun_spectral_lines.csv')
# mol_bands = ascii.read(wdir+'molecular_bands.csv')
# H_lines = np.sort(np.array(
#     [0.410, 0.434, 0.486, 0.656, 1.875, 1.282, 1.094, 1.005, 0.954, 2.625, 2.166, 1.944, 1.817, 1.458, 2.279, 1.94509,
#      1.81791, 1.73669, 1.68111, 1.64117, 1.61137, 1.58849, 1.57050, 1.55607, 1.54431, 1.53460, 1.52647, 1.51960,
#      1.51374]))
# C12O16 = np.array([2.2935, 2.3227, 2.3525, 2.3829, 2.4141])
# C12O18 = np.array([2.3492, 2.3783, 2.4385])
# C12O17 = np.array([2.3226, 2.3517, 2.3815, 2.4119])
# C13O16 = np.array([2.3448, 2.3739, 2.4037, 2.4341])
# HeI = np.array([1.0833, 1.701, 1.278, 2.059, 2.113, 2.165])
# FI = np.array([1.008713, 1.018615, 1.020957, 1.028545, 1.029301, 1.03808, 1.042629, 1.086231])
# cilines = speclines[np.where(speclines['Element'] == 'Ci')]
# cilinemask = ((cilines['Wav'] > 1.0) & (cilines['Wav'] < 1.1)) | ((cilines['Wav'] > 1.15) & (cilines['Wav'] < 1.25))
# OH = np.array(
#     [1.0829, 1.0831, 1.0841, 1.0856, 1.0876, 1.0895, 1.0923, 1.0948, 1.0972, 1.1006, 1.1026, 1.1069, 1.1086, 1.1137,
#      1.1152, 1.1211, 1.1285, 1.1288, 1.1292])
# H2 = np.array([1.958, 2.0341, 2.0739, 2.1221, 2.1543, 2.2238, 2.2480, 2.4070, 2.4139, 2.4242, 2.4379, 2.2948])
# Mg = np.array([1.5029, 1.5044, 1.5052, 1.7113, 2.1065, 2.1067, 2.2814])
# MgII = np.array([1.7723])
# Fe = np.array([1.5774, 1.5817, 1.7332, 2.0704, 2.2263, 2.2387])
# Si = np.array([1.5892, 2.0923])
# Al = np.array([1.6755, 1.7704, 2.1099, 2.1170])
# Na = np.array([2.2062, 2.2090])
# Ca = np.array([2.2614, 2.2631, 2.2657])
# Ti = np.array([2.1790, 2.1855])
# TiO = np.array([0.9725, 0.9814, 0.9899, 0.9986, 1.0025, 1.0137, 1.0250])
work_dir = '/Users/earleyn138/Library/Mobile Documents/com~apple~CloudDocs/Research/grad/science/'
data_dir = work_dir + 'pgir/pgir_vars/complete_census/'


def add_lines(classname, ax, norm_flux):
    if classname == 'lpv0':
        line_file = data_dir + 'usable_lines2.csv'
        lsl, ats, bl = [5, 5, 5], [11, 12, 10], [11.5, 12.5, 11]
        print('Added lines to', classname)

    if classname == 'lpv1':
        line_file = data_dir + 'usable_lines1.csv'
        lsl, ats, bl = [5, 5, 5], [11, 11.7, 10], [11.5, 12.2, 11]
        print('Added lines to', classname)

    if classname == 'lpv2':
        line_file = data_dir + 'usable_lines1.csv'
        lsl, ats, bl = [5, 5, 5], [3.5, 4.2, 3], [4, 4.6, 3.5]
        print('Added lines to', classname)

    if classname == 'lpvline':
        line_file = data_dir + 'usable_lines0.csv'
        lsl, ats, bl = [5, 5, 5], [3.5, 4.2, 4.5], [4, 4.6, 5]
        print('Added lines to', classname)

    if classname == 'lpvrisek':
        line_file = data_dir + 'usable_lines3.csv'
        lsl, ats, bl = [5, 5, 5], [2.8, 3.8, 2.5], [3, 4, 3]
        print('Added lines to', classname)

    if classname == 'mira':
        line_file = data_dir + 'usable_lines4.csv'
        lsl, ats, bl = [5, 5, 5], [10.2, 10.2, 10.2], [10.8, 10.8, 10.8]
        print('Added lines to', classname)

    if classname == 'erraticm':
        line_file = data_dir + 'usable_lines5.csv'
        lsl, ats, bl = [5, 5, 5], [9, 9, 8], [10, 10, 9]
        print('Added lines to', classname)

    if classname == 'erraticmVO':
        line_file = data_dir + 'usable_lines6.csv'
        lsl, ats, bl = [5, 5, 5], [5, 5, 4], [5.5, 5.5, 4.5]
        print('Added lines to', classname)

    if classname in ['cstar','cstar0','cstar1']:
        line_file = data_dir + 'usable_lines7.csv'
        lsl, ats, bl = [5, 5, 5], [12.1, 12.1, 12.1], [12.3, 12.3, 12.3]
        print('Added lines to', classname)

    if classname in ['He10830em', 'He10830em0', 'He10830em1','He10830exotic1','He10830exotic2']:
        line_file = data_dir + 'usable_lines8.csv'
        lsl, ats, bl = [5, 5, 5], [12.1, 12.1, 12.1], [13, 13, 13]
        print('Added lines to', classname)

    if classname == 'ohir':
        line_file = data_dir + 'usable_lines9.csv'
        lsl, ats, bl = [5, 5, 5], [8.5, 8.5, 8.8], [9.5, 9.5, 9.8]
        print('Added lines to', classname)

    if classname in ['hbandabsorber', 'monsterhband']:
        line_file = data_dir + 'usable_lines10.csv'
        lsl, ats, bl = [5, 5, 5], [11, 11, 11], [11.5, 11.5, 11.5]
        print('Added lines to', classname)

    if classname in ['emline']:
        line_file = data_dir + 'usable_lines11.csv'
        lsl, ats, bl = [5, 5, 5], [18, 13, 15], [20, 15, 16]
        print('Added lines to', classname)


    if classname == 'rcb':
        line_file = data_dir + 'usable_lines12.csv'
        lsl, ats, bl = [5, 5, 5], [5.8, 5.8, 5.8], [6, 6, 6]
        print('Added lines to', classname)

    if classname == 'yso':
        line_file = data_dir + 'usable_lines11.csv'
        lsl, ats, bl = [5, 5, 5], [18, 13, 15], [20, 15, 16]
        print('Added lines to', classname)

    config_labels(norm_flux, line_file, ax)

def config_labels(norm_flux, line_file, ax, lw=0.05):
    irlines = pd.read_csv(line_file)
    lw = irlines['wav']
    ll = irlines['line']

    jmask = masks.j_band_mask(lw)
    hmask = masks.h_band_mask(lw)
    kmask = masks.k_band_mask(lw)
    for i, mask in enumerate([jmask, hmask, kmask]):
        for j,w in enumerate(lw[mask]):
            labels = ll[mask]
            ax[i].axvline(w, ls='--', color='k', lw=0.1, alpha=0.2)
            ax[i].text(w, norm_flux[i], labels.values[j], rotation=90, fontsize=1, alpha=0.5)


#def config_labels(wavs, norm_flux, line_file, ax, lsl, ats, bl):
    # irlines = pd.read_csv(line_file)
    # lw = irlines['wav']
    # ll = irlines['line']
    # label_sizes = [np.ones(len(lw)) * lsl[0], np.ones(len(lw)) * lsl[1], np.ones(len(lw)) * lsl[2]]
    # arrow_tips = [np.ones(len(lw)) * ats[0], np.ones(len(lw)) * ats[1], np.ones(len(lw)) * ats[2]]
    # box_locs = [np.ones(len(lw)) * bl[0], np.ones(len(lw)) * bl[1], np.ones(len(lw)) * bl[2]]
    #
    # for i, a in enumerate(ax):
    #     lineid_plot.plot_line_ids(wavs[i], norm_flux[i], lw, ll, label_sizes[i],
    #                               max_iter=100000,
    #                               ax=a, box_loc=list(box_locs[i]),
    #                               arrow_tip=arrow_tips[i], xval_units='um',
    #                               plot_kwargs={'color': 'k', 'linewidth': 0.05, 'alpha': 0.3})
    #
    # hidelabels = ['CO12_num_{:d}'.format(num) for num in list(range(2, 11))]
    # # print('hidelabels: ', hidelabels)
    # # print('HIw: ', HIw)
    # for a in ax:
    #     aobj = a.findobj(mpl.text.Annotation)
    #     lobja = a.findobj(mpl.lines.Line2D)
    #     for n in aobj:
    #         if n.get_label() in hidelabels:
    #             n.set_visible(False)
    #     for l in lobja:
    #         if l.get_label() in hidelabels:
    #             l.set_visible(False)

# def add_IRlines(ax, ymn, ymx):
#     """
#
#     :param ax:
#     :param ymn:
#     :param ymx:
#     :return:
#     """
#     l0 = ax.vlines(speclines[np.where(speclines['Element'] == 'Fei')]['Wav'], ymin=ymn, ymax=ymx, linestyle='-',
#                    color='r', linewidth=0.5, alpha=1.0, label='Fei')
#     l1 = ax.vlines(speclines[np.where(speclines['Element'] == 'Ci')]['Wav'], ymin=ymn, ymax=ymx, linestyle='-',
#                    color='g', linewidth=0.5, alpha=1.0, label='Ci')
#     l2 = ax.vlines(mol_bands[np.where(mol_bands['Molecule'] == 'CO12')]['wav'], ymin=ymn, ymax=ymx, linestyle='-',
#                    color='b', linewidth=0.5, alpha=1.0, label='CO12')
#     l3 = ax.vlines(mol_bands[np.where(mol_bands['Molecule'] == 'CN')]['wav'], ymin=ymn, ymax=ymx, linestyle='-',
#                    color='b', linewidth=0.5, alpha=1.0, label='CN')
#     l4 = ax.vlines(HeI, ymin=ymn, ymax=ymx, linestyle='--', color='gray', label='HeI')
#     l5 = ax.vlines(speclines[np.where(speclines['Element'] == 'Nai')]['Wav'], ymin=ymn, ymax=ymx, linestyle='-',
#                    color='orange', linewidth=0.5, alpha=1.0, label='Nai')
#     l6 = ax.vlines(speclines[np.where(speclines['Element'] == 'Caii')]['Wav'], ymin=ymn, ymax=ymx, linestyle='-',
#                    color='yellow', linewidth=0.5, alpha=1.0, label='Caii')
#     l7 = ax.vlines(mol_bands[np.where(mol_bands['Molecule'] == 'C2')]['wav'], ymin=ymn, ymax=ymx, linestyle='-',
#                    color='b', linewidth=0.5, alpha=1.0, label='C2')
#     l8 = ax.vlines(speclines[np.where(speclines['Element'] == 'Sii')]['Wav'], ymin=ymn, ymax=ymx, linestyle='-',
#                    color='blue', linewidth=0.5, alpha=1.0, label='Sii')
#     l9 = ax.vlines(speclines[np.where(speclines['Element'] == 'Ki')]['Wav'], ymin=ymn, ymax=ymx, linestyle='-',
#                    color='yellow', linewidth=0.5, alpha=1.0, label='Ki')
#     l10 = ax.vlines(H_lines, ymin=ymn, ymax=ymx, linestyle='-', color='brown', linewidth=0.5, alpha=1.0, label='HI')
#
#     l11 = ax.vlines(C12O16, ymin=ymn, ymax=ymx, linestyle='-', color='brown', linewidth=0.5, alpha=1.0, label='C12O16')
#     l12 = ax.vlines(C12O18, ymin=ymn, ymax=ymx, linestyle='-', color='blue', linewidth=0.5, alpha=1.0, label='C12O18')
#     l13 = ax.vlines(C12O17, ymin=ymn, ymax=ymx, linestyle='-', color='brown', linewidth=0.5, alpha=1.0, label='C12O17')
#     l14 = ax.vlines(C13O16, ymin=ymn, ymax=ymx, linestyle='-', color='brown', linewidth=0.5, alpha=1.0, label='C13O16')
#     l15 = ax.vlines(H2, ymin=ymn, ymax=ymx, linestyle='-', color='blue', linewidth=0.5, alpha=1.0, label='H2')
#     l16 = ax.vlines(TiO, ymin=ymn, ymax=ymx, linestyle='-', color='purple', linewidth=0.5, alpha=1.0, label='TiO')
#     lines = [l0, l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l13, l14, l15, l16]
#
#     return lines
#
#
#
