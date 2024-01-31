import numpy as np
from pgir.plotting.plot_spec import plot_specranges
from pgir.plotting.plot_lc import plot_lcgroups

def to_latex(df, output_tex):
    # Extract the first three columns
    names = np.array(df['Names'])
    ras = np.array(df['RA'].astype(float))
    decs = np.array(df['Dec'].astype(float))

    # Write LaTeX table to a file
    with open(output_tex, 'w') as file:
        file.write('\\begin{deluxetable}{lrr}\n')
        file.write('\\tablecaption{ \label{tab: }}\n')
        file.write('\\tablehead{\colhead{PGIR ID} & \colhead{RA} & \colhead{Dec}}\n')
        file.write('\startdata\n')
        for i,n in enumerate(names):
            file.write('{} & {:.3f} & {:.3f} \\\\ \n'.format(n,ras[i],decs[i]))
        file.write('\enddata\n')
        file.write('\end{deluxetable}')

def count_groups(obs, data_dir, irtf_dir,line_dir):
    pdgroup = obs.groupby('classification')
    spec_dir = data_dir + 'spectra/'
    lc_dir = data_dir + 'forced_photometry/'
    fig_dir = data_dir + 'figures/'
    latex_dir = data_dir + 'latex/'

    classes = pdgroup.groups.keys()
    for c in classes:
        print('Grouping class ', c,'\n ======================')
        if c[:3] == 'lpv':
            irtf_file = irtf_dir+'M10+III_IRAS14086-0703.txt'
            irtf_name = 'M10+III, IRAS14086-0703'
        #     irtf_file = irtf_dir+'M8-9III_IRAS21284-0747.txt'
        #     irtf_name = 'M8-9III, IRAS21284-0747'
        elif c == 'He10830em':
            irtf_file = irtf_dir+'M6III_HD196610.txt'
            irtf_name = 'M6III, HD196610'
        elif c in ['He10830exotic1', 'He10830exotic2']:
            irtf_file = None
            irtf_name = None
        elif  c == 'mira':
            irtf_file = irtf_dir+'M7-III:_HD108849.txt'
            irtf_name = 'M7-III, HD108849'
        elif c[:8] == 'erraticm':
            irtf_file = irtf_dir+'M8III_IRAS01037+1219.txt'
            irtf_name = 'M8III, IRAS01037+1219'
        elif c =='cstar':
            irtf_file = irtf_dir+'C7,6e(N4)_HD31996.txt'
            irtf_name = 'C7,6e(N4), HD31996'
        elif c == 'emline':
            irtf_file = None
            irtf_name = None
        elif c == 'emlinerisej':
            irtf_file = None
            irtf_name = None
        elif c == 'yso':
            irtf_file = irtf_dir+'M7-III:_HD207076.txt'
            irtf_name = 'M7-III, HD207076'
        elif c =='ohir':
            irtf_file = irtf_dir+'M8III_IRAS01037+1219.txt'
            irtf_name = 'M8III, IRAS01037+1219'
        elif c == 'hbandabsorber':
            irtf_file = irtf_dir+'C7,6e(N4)_HD31996.txt'
            irtf_name = 'C7,6e(N4), HD31996'
        elif c == 'monsterhband':
            irtf_file = None
            irtf_name = None
        elif c in ['rcb', 'rcbkbump','rcbV23','DYper']:
            irtf_file = irtf_dir+'C7,6e(N4)_HD31996.txt'
            irtf_name = 'C7,6e(N4), HD31996'
        if c in ['hbandabsorber', 'erraticm', 'cstar', 'He10830em']:
            nmax = 11
        else:
            nmax = 10
        if c == 'emline':
            fritz = '/Users/earleyn138/Downloads/mWTP20aachbe.fits.txt'
        else:
            fritz = None
        c_df = pdgroup.get_group(c)
        to_latex(c_df, latex_dir+c+'_table.tex')
        print('Saved ', c+'_table.tex')
        specfiles = c_df['specfilename']
        obs_run = c_df['Run']
        name = c_df['Names']
        lcfiles = c_df['lcfile']
        n_subgroups = len(specfiles) // nmax
        print('Subgroups: ', n_subgroups)
        if n_subgroups > 0 and len(specfiles)/nmax != 1:
            for i in range(n_subgroups + 1):
                try:
                    spec_fni = specfiles[nmax * i:nmax * i + nmax]
                    runi = obs_run[nmax * i:nmax * i + nmax]
                    namei = name[nmax * i:nmax * i + nmax]
                    lcfilesi = lcfiles[nmax * i:nmax * i + nmax]

                except:
                    spec_fni = specfiles[10 * i:]
                    runi = obs_run[10 * i:]
                    namei = name[10 * i:]
                    lcfilesi = lcfiles[10 * i:]

                spec_pathi = spec_dir + runi + '/' + spec_fni + '.fits'
                lc_pathi = lc_dir + lcfilesi
                spectime_list = plot_specranges(spec_pathi, namei, fig_name=fig_dir + c + str(i), irtf_file=irtf_file,irtf_name=irtf_name,fritz_temp=fritz)
                plot_lcgroups(lc_pathi, namei, spectimes=spectime_list, fig_name=fig_dir + c + str(i) + '_fph.pdf')
        else:
            spec_path = spec_dir + obs_run + '/' + specfiles + '.fits'
            lc_path = lc_dir + lcfiles
            spectime_list=plot_specranges(spec_path, name, fig_name=fig_dir+c, irtf_file=irtf_file, irtf_name=irtf_name,fritz_temp=fritz)
            plot_lcgroups(lc_path, name, spectimes=spectime_list, fig_name=fig_dir + c + '_fph.pdf')
