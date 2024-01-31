import numpy as np
import matplotlib.pyplot as plt
from pgir.utilsvar.masks import full_spec_mask
from pgir.iovar.load_spec import get_object_data,get_norm_template,get_norm_values,get_fritz_template
from pgir.plotting.add_lines import add_lines
from pgir.plotting.spec_config import config_spec
from pgir.utilsvar.calc_width import eqwidth

def plot_specgroups(spec_path, namegroup, wholespec=True,
                jband=False, hband=False, kband=False,
                irtf_file=None, irtf_name=None,
                fig_name=None, title=None,
                show_He=False, show_H=False, show_C=False, fritz_temp=None):
    #UPDATE
    classname = ((fig_name.split('/')[-1]).split('_')[0])
    specdate_list = []
    if wholespec:
        fig, ax = plt.subplots(1, 3, figsize=(8.5, 7), sharey=True)
        fig.add_subplot(111, frameon=False)
        plt.tick_params(labelcolor='none', which='both', top=False, bottom=False, left=False, right=False)
        space = 0

        for n, s in zip(namegroup,spec_path):
            print(n, 'Plotted the spectrum of ', s)
            w, f, fw,ff,time = get_object_data(s)
            specdate_list.append(time)
            classname = ((fig_name.split('/')[-1]).split('_')[0])
            ref_wav, textpos, axind, ylim, ymax, ymin, calc_widths = config_spec(classname)
            wavs, norm_flux = get_norm_values(w, f,fw, ff,ref_wav-0.1,ref_wav+0.1)
            if calc_widths:
                eqwHe = eqwidth(wavs[0], norm_flux[0], linecenter=1.0833, lineregion=(1.08, 1.089), specregion=(1.079, 1.1), save_fig=True,fig_name=n+'_He10830.pdf')
                eqwCO = eqwidth(wavs[2], norm_flux[2], linecenter=2.2935, lineregion=(2.25, 2.33), specregion=(2.1, 2.34), save_fig=True,fig_name=n+'_CO.pdf')
            if classname == 'rcb':
                sp = 1.1
            else:
                sp = 1
            ax[0].plot(wavs[0], norm_flux[0] + sp*space, linewidth=0.1, alpha=1)
            ax[1].plot(wavs[1], norm_flux[1] + sp*space, linewidth=0.1, alpha=1)
            ax[2].plot(wavs[2], norm_flux[2] + sp*space, linewidth=0.1, alpha=1)
            # if wholespec:
            ax[axind].text(textpos, np.nanmedian(norm_flux[1])+sp*space, n, fontsize=5)
            space += 1

        if ylim:
            for a in ax:
                a.set_ylim(ymin, ymax)

        if irtf_file != None:
            tw, tf = get_norm_template(irtf_file, ref_wav-0.1,ref_wav+0.1,get_mask=full_spec_mask)
            ax[0].plot(tw[0], tf[0] + sp*space, linewidth=0.1, alpha=0.5,color='k')
            ax[1].plot(tw[1], tf[1] + sp*space, linewidth=0.1, alpha=0.5,color='k')
            ax[2].plot(tw[2], tf[2] + sp*space, linewidth=0.1, alpha=0.5,color='k')
            if wholespec:
                ax[axind].text(textpos, np.nanmedian(tf[1])+space, irtf_name, fontsize=5)

        if fritz_temp != None:
            tw, tf = get_fritz_template(fritz_temp, ref_wav - 0.1, ref_wav + 0.1)
            ax[0].plot(tw[0], tf[0] + 2*space, linewidth=0.1, alpha=0.5, color='k')
            ax[1].plot(tw[1], tf[1] + 2*space, linewidth=0.1, alpha=0.5, color='k')
            ax[2].plot(tw[2], tf[2] + 2*space, linewidth=0.1, alpha=0.5, color='k')
            if wholespec:
                ax[axind].text(textpos, np.nanmedian(tf[1]) + 2*space+1, 'WTP20aachbe', fontsize=5)

        (ymj,ymaj), (ymh,ymah),(ymk,ymak) = ax[0].set_ylim(), ax[1].set_ylim(),ax[2].set_ylim()
        add_lines(classname, ax, np.array([ymaj, ymah, ymak])*1.01)
        plt.ylabel('$f_\lambda/f_\lambda({:.1f} \mu m)$ + offset'.format(ref_wav))
        plt.xlabel('Observed Wavelength, um')
        plt.subplots_adjust(wspace=0.05)
        if fig_name:
            plt.savefig(fig_name, bbox_inches='tight')
        plt.close('all')

    ###########
        # fig = plt.figure(figsize=(10, 7))
        # gs = gridspec.GridSpec(1, 1)
        # ax2 = fig.add_subplot(gs[0])
        # i=0
        # for n, s in zip(namegroup,spec_path):
        #     print(i, 'Plotted the spectrum of ', s)
        #     w, f, fw,ff = get_object_data(s)
        #     wavs, norm_flux,contnm = get_norm_values(w, f,fw,ff)
        #     # if obs['Names'][i + imin] in check_norms:
        #     #     fig2 = plt.figure(figsize=(10, 7))
        #     #     gs2 = gridspec.GridSpec(1, 1)
        #     #     ax3 = fig2.add_subplot(gs2[0])
        #     #     spectrum = Spectrum1D(flux=f * u.Jy, spectral_axis=w * u.um)
        #     #     g1_fit = fit_generic_continuum(spectrum, median_window=1)
        #     #     contnm = g1_fit(w * u.um)
        #     #     ax3.plot(w, contnm, linewidth=0.8, alpha=0.8)
        #     #     ax3.plot(w, f, + i, linewidth=0.8, alpha=0.8)
        #     #     plt.savefig('norm_check_'+obs['Names'][i + imin]+'.pdf', bbox_inches='tight')
        #     ax2.plot(wavs, norm_flux + i, linewidth=0.8, alpha=0.8)
        #     if wholespec:
        #         ax2.text(1.81,1 + i, n)
        #     i+=1


        # if irtf_file != None:
        #     tw, tf, = get_norm_template(irtf_file, get_mask=full_spec_mask)
        #     ax2.plot(np.array(tw), np.array(tf) + i, linewidth=0.8, alpha=0.8)
        #     if wholespec:
        #         ax2.text(1.81, 1+i, irtf_name)
        #
        # classname = ((fig_name.split('/')[-1]).split('_')[0])[:3]
        # if classname == 'lpv':
        #     print('hello')
        #     ymax = i+3
        # else:
        #     ymax  = i+2
        # plt.ylim(0, ymax)
        # if classname == 'lpv':
        #     plt.axvline(1.04626, alpha=0.2, ls='--', color='k')
        #     plt.axvline(1.04822, alpha=0.2, ls='--', color='k')
        # # if show_He:
        # #     for l in HeI:
        # #         if l > 1 and l < 1.3:
        # #             plt.axvline(l, alpha=0.2, ls='--', color='b')
        # #
        # # if show_H:
        # #     for l in H_lines:
        # #         if l > 1 and l < 1.3:
        # #             plt.axvline(l, alpha=0.2, ls='--', color='r')
        # # if show_C:
        # #     for l in cilines['Wav']:
        # #         if l > 1 and l < 2:
        # #             plt.axvline(l, alpha=0.2, ls='--', color='g')
        #
        # if jband:
        #     plt.xlim(0.99, 1.34)
        # if hband:
        #     plt.xlim(1.42, 1.8)
        # if kband:
        #     plt.xlim(2.1, 2.48)
        # else:
        #     plt.xlim()
        # plt.ylabel('Normalized flux + offset')
        # plt.xlabel('Observed Wavelength, um')
        # plt.title(title)
        # if fig_name:
        #     plt.savefig(fig_name, bbox_inches='tight')
        #     plt.close('all')

    return specdate_list


def plot_specranges(spec_path, namegroup, fig_name=None, irtf_file=None, irtf_name=None,fritz_temp=None):
    specrange = ['whole', 'j', 'h', 'k']
    for s in specrange:
        if s == 'whole':
            print('Plotting whole spectrum')
            spectimes = plot_specgroups(spec_path, namegroup, wholespec=True, jband=False, show_He=False, show_H=False,
                        fig_name=fig_name + '_wholespec.pdf', irtf_file=irtf_file, irtf_name=irtf_name,fritz_temp=fritz_temp)
        # elif s == 'j':
        #     print('Plotting the j band spectrum')
        #     plot_specgroups(spec_path, namegroup, wholespec=False, jband=True, show_He=False, show_H=False,
        #                 fig_name=fig_name + '_jband.pdf', irtf_file=irtf_file, irtf_name=irtf_name)
        #
        # elif s == 'h':
        #     print('Plotting the h band spectrum')
        #     plot_specgroups(spec_path, namegroup, wholespec=False, hband=True, show_He=False, show_H=False,
        #                 fig_name=fig_name + '_hband.pdf', irtf_file=irtf_file, irtf_name=irtf_name)
        #
        # elif s == 'k':
        #     print('Plotting the k band spectrum')
        #     plot_specgroups(spec_path, namegroup, wholespec=False, kband=True, show_He=False, show_H=False,
        #                 fig_name=fig_name + '_kband.pdf', irtf_file=irtf_file, irtf_name=irtf_name)


    return spectimes