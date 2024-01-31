import numpy as np
import matplotlib.pyplot as plt
from pgir.iovar.load_lc import get_gattini_lc
from astropy.time import Time

def plot_lc(json_file, ax,spec_time):
    g_time, g_mag, g_umag, g_lims, g_snr = get_gattini_lc(json_file)
    g_time = g_time - Time.now().jd
    ax.axvline(spec_time-Time.now().jd,ls='--',color='k',alpha=0.5)
    detection = (g_mag != -99) & (g_snr > 3)
    nondetection = (g_lims != -99) & (g_snr < 3)
    ax.errorbar(g_time[detection], g_mag[detection],
                yerr=g_umag[detection], ls='', marker='o',
                color='slateblue', alpha=0.7, markersize=1.5)

    ax.errorbar(g_time[nondetection], g_lims[nondetection], ls='', color='slateblue', alpha=0.2, marker='v',
                markerfacecolor='none', markersize=1.5)

    ax.set_ylim(ax.get_ylim()[::-1])
    try:
        if np.max(g_mag[detection]) > 17:
            ylolim = 17
        else:
            ylolim = np.max(g_mag[detection]) + 0.5
        ax.set_ylim(ylolim, )
        # ax.set_ylabel('Magnitude')
        #ax.set_xlabel('JD-JD0')
    except:
        print('There is a problem with ', json_file)


# def plot_lc(json_file):
#     fig = plt.figure(figsize=(10, 7))
#     gs = gridspec.GridSpec(1, 1)
#     ax = fig.add_subplot(gs[0])
#     g_time, g_mag, g_umag, g_lims, g_snr = get_gattini_lc(json_file)
#
#     g_time = g_time - g_time[-1]
#     detection = (g_mag != -99) & (g_snr > 3)
#     nondetection = (g_mag != -99) & (g_snr < 3)
#     ax.errorbar(g_time[detection], g_mag[detection],
#                 yerr=g_umag[detection], ls='', marker='o',
#                 color='slateblue', alpha=0.7, markersize=2)
#
#     ax.errorbar(g_time[nondetection], g_lims[nondetection], ls='', color='slateblue', alpha=0.2, marker='v',
#                 markerfacecolor='none', markersize=2)
#
#     ax.set_ylim(ax.get_ylim()[::-1])
#     ax.set_ylim(18, )
#     ax.set_ylabel('Magnitude')
#     ax.set_xlabel('JD-JD0')


def plot_lcgroups(lcfiles,names,spectimes,fig_name=None):
    print('number of lcfiles: ', len(lcfiles))
    if len(lcfiles) > 1:
        fig,axs = plt.subplots(len(lcfiles),1,figsize=(5, 7),sharex=True)
        fig.text(-0.02, 0.5, 'Magnitude (J)', va='center', rotation='vertical')
        plt.xlabel('JD-JD0')
        for ax,lc,n,t in zip(axs[::-1],lcfiles,names,spectimes):
            print('Plotted ', lc.split('/')[-1])
            plot_lc(json_file=lc,ax=ax,spec_time=t)
            #fn = (((lc.split('/')[-1]).split('lc_')[-1])).split('_r')[0]
            #ax.text(0.1,0.1,fn,transform=ax.transAxes,fontsize=8)
            ax.text(0.8, 0.1, n, transform=ax.transAxes, fontsize=8)
            ax.yaxis.set_major_locator(plt.MaxNLocator(nbins=3, integer=True))
            ax.tick_params(axis='both', which='major', labelsize=8)
            ax.tick_params(axis='both', which='minor', labelsize=8)

        fig.tight_layout()
        plt.subplots_adjust(hspace=0)
        plt.savefig(fig_name,bbox_inches='tight')
        plt.close('all')

    else:
        print(lcfiles)
        fig, ax = plt.subplots(1, 1, figsize=(5, 7), sharex=True)
        fig.text(-0.02, 0.5, 'Magnitude (J)', va='center', rotation='vertical')
        plt.xlabel('JD-JD0')
        lc = lcfiles.values[0]
        n = names.values[0]
        plot_lc(json_file=lc, ax=ax, spec_time=spectimes[0])
        # fn = (((lc.split('/')[-1]).split('lc_')[-1])).split('_r')[0]
        # ax.text(0.1,0.1,fn,transform=ax.transAxes,fontsize=8)
        ax.text(0.8, 0.1, n, transform=ax.transAxes, fontsize=8)
        ax.yaxis.set_major_locator(plt.MaxNLocator(nbins=3, integer=True))
        ax.tick_params(axis='both', which='major', labelsize=8)
        ax.tick_params(axis='both', which='minor', labelsize=8)

        fig.tight_layout()
        plt.subplots_adjust(hspace=0)
        plt.savefig(fig_name, bbox_inches='tight')
        plt.close('all')
