import matplotlib.pyplot as plt
from matplotlib import gridspec
import pandas as pd
from nirstid.masks import full_spec_mask
from load_spec import get_object_data
from norm_spec import get_norm_values
from prep_irtfspec import get_norm_template
from load_lc import get_gattini_lc
from add_lines import *
import sys
from astropy.time import Time
from PyAstronomy.pyasl import baryCorr
from astropy.coordinates import SkyCoord

obsfile = '/Users/earleyn138/Downloads/Gattini LAV census - complete_census.csv'
obs = pd.read_csv(obsfile)

work_dir = '/Users/earleyn138/Library/Mobile Documents/com~apple~CloudDocs/Research/grad/science/'
irtf_dir = work_dir + '/irtf_spectra/All_text_091201/'
data_dir = work_dir + 'pgir/pgir_vars/complete_census/'
fig_dir = data_dir+'figures/'

def plot_groups(imin, imax, wholespec=True,
                jband=False, hband=False, kband=False,
                irtf_file=None, irtf_name=None,
                figname=None, title=None,
                show_He=False, show_H=False, show_C=False):
    specfiles = obs['specfilename'][imin:imax]
    fig = plt.figure(figsize=(10, 7))
    gs = gridspec.GridSpec(1, 1)
    ax2 = fig.add_subplot(gs[0])
    for i, s in enumerate(specfiles):
        print(i, s)
        w, f, fw,ff = get_object_data(data_dir+'spectra/'+ obs['Run'][i + imin] + '/' + s + '.fits')
        wavs, norm_flux = get_norm_values(w, f,fw,ff)
        ax2.plot(wavs, norm_flux + i , linewidth=0.8, alpha=0.8)
        if wholespec:
            ax2.text(1.81, 1 + i, obs['Names'][i + imin])

    if irtf_file != None:
        tw, tf, = get_norm_template(irtf_file, get_mask=full_spec_mask)
        ax2.plot(np.array(tw), np.array(tf) + (i + 1), linewidth=0.8, alpha=0.8)
        if wholespec:
            ax2.text(1.81, 2 + i, irtf_name)

    plt.ylim(0, i + 3)
    if show_He:
        for l in HeI:
            if l > 1 and l < 1.3:
                plt.axvline(l, alpha=0.2, ls='--', color='g')
    if show_H:
        for l in H_lines:
            if l > 1 and l < 1.3:
                plt.axvline(l, alpha=0.2, ls='--', color='r')
    if show_C:
        for l in cilines['Wav']:
            if l > 1 and l < 2:
                plt.axvline(l, alpha=0.2, ls='--', color='g')

    if jband:
        plt.xlim(0.99, 1.34)
    if hband:
        plt.xlim(1.42, 1.8)
    if kband:
        plt.xlim(2.1, 2.48)
    else:
        plt.xlim()
    plt.ylabel('Normalized flux + offset')
    plt.xlabel('Observed Wavelength, um')
    plt.title(title)
    if figname:
        plt.savefig(figname, bbox_inches='tight')


def group_lc(json_file, ax):
    g_time, g_mag, g_umag, g_lims, g_snr = get_gattini_lc(json_file)

    g_time = g_time - Time.now().jd#g_time[-1]
    detection = (g_mag != -99) & (g_snr > 3)
    nondetection = (g_mag != -99) & (g_snr < 3)
    ax.errorbar(g_time[detection], g_mag[detection],
                yerr=g_umag[detection], ls='', marker='o',
                color='slateblue', alpha=0.7, markersize=2)

    ax.errorbar(g_time[nondetection], g_mag[nondetection], ls='', color='slateblue', alpha=0.2, marker='v',
                markerfacecolor='none', markersize=2)

    ax.set_ylim(ax.get_ylim()[::-1])
    if np.max(g_mag[g_mag != -99]) > 17:
        ylolim = 17
    else:
        ylolim = np.max(g_mag[g_mag != -99]) + 0.5
    ax.set_ylim(ylolim, )
    # ax.set_ylabel('Magnitude')
    ax.set_xlabel('JD-JD0')


def plot_specranges(imin, imax, fig=None, irtf_file=None, irtf_name=None):
    specrange = ['whole', 'j', 'h', 'k']
    for s in specrange:
        if s == 'whole':
            plot_groups(imin, imax, wholespec=True, jband=False, show_He=False, show_H=False,
                        figname=fig + '_wholespec.pdf', irtf_file=irtf_file, irtf_name=irtf_name)

        elif s == 'j':
            plot_groups(imin, imax, wholespec=False, jband=True, show_He=False, show_H=False,
                        figname=fig + '_jband.pdf', irtf_file=irtf_file, irtf_name=irtf_name)

        elif s == 'h':
            plot_groups(imin, imax, wholespec=False, hband=True, show_He=False, show_H=False,
                        figname=fig + '_hband.pdf', irtf_file=irtf_file, irtf_name=irtf_name)

        elif s == 'k':
            plot_groups(imin, imax, wholespec=False, kband=True, show_He=False, show_H=False,
                        figname=fig + '_kband.pdf', irtf_file=irtf_file, irtf_name=irtf_name)



def plot_lc(json_file):
    fig = plt.figure(figsize=(10, 7))
    gs = gridspec.GridSpec(1, 1)
    ax = fig.add_subplot(gs[0])
    g_time, g_mag, g_umag, g_lims, g_snr = get_gattini_lc(json_file)

    g_time = g_time - g_time[-1]
    detection = (g_mag != -99) & (g_snr > 3)
    nondetection = (g_mag != -99) & (g_snr < 3)
    ax.errorbar(g_time[detection], g_mag[detection],
                yerr=g_umag[detection], ls='', marker='o',
                color='slateblue', alpha=0.7, markersize=2)

    ax.errorbar(g_time[nondetection], g_lims[nondetection], ls='', color='slateblue', alpha=0.2, marker='v',
                markerfacecolor='none', markersize=2)

    ax.set_ylim(ax.get_ylim()[::-1])
    ax.set_ylim(18, )
    ax.set_ylabel('Magnitude')
    ax.set_xlabel('JD-JD0')


def plot_lcfigs(imin, imax,name=None):
    lcfiles = data_dir+obs['lcfile']

    fig,axs = plt.subplots(len(range(imin,imax)),1,figsize=(7, 7),sharex=True)
    for ax,lc in zip(axs[::-1],lcfiles[imin:imax]):
        print(lc)
        group_lc(lc,ax)

    plt.subplots_adjust(hspace=0)
    fig.text(0.03, 0.5, 'Magnitude (J)', va='center', rotation='vertical')
    plt.savefig(name,bbox_inches='tight')



def main():
    args = sys.argv[1:]
    imin = int(args[0])
    imax = int(args[1])
    class_name = args[2]
    temp_fn = args[3]
    temp_name = args[4]

    if temp_fn:
        irtf_file = irtf_dir + temp_fn
        irtf_name = temp_name
    else:
        irtf_file = None
        irtf_name = None

    plot_specranges(imin, imax, fig=fig_dir+class_name,
                    irtf_file=irtf_file, irtf_name=irtf_name)

    plot_lcfigs(imin, imax, fig_dir+class_name+'_fph.pdf')

if __name__ == "__main__":
    main()