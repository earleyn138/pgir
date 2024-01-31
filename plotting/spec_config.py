def config_spec(classname):
    if classname in ['lpv0', 'lpv1' ,'lpv2' ,'lpvdimVO' ,'lpvline' ,'lpvrisek']:
        ref_wav = 1.7
        textpos, axind = 1.42, 1
        ylim = False
        calc_widths = False
    if  classname == 'mira' or classname in ['cstar', 'cstar0' ,'cstar1']:
        ref_wav = 1.7
        textpos, axind = 1.42, 1
        ylim = False
        calc_widths = False
    elif classname in ['hbandabsorber' ,'hbandabsorber0' ,'hbandabsorber1']:
        ref_wav = 1.7
        textpos, axind = 1.42, 1
        ylim =True
        ymax = 12
        ymin = 0
        calc_widths = False
    elif classname in ['monsterhband']:
        ref_wav = 1.7
        textpos, axind = 1.42, 1
        ylim =True
        ymax = 9
        ymin = -0.5
        calc_widths = False
    elif classname == 'ohir':
        ref_wav = 2.2
        textpos, axind = 1.42, 1
        ylim =True
        ymax = 10
        ymin = -0.5
        calc_widths = False
    elif classname in ['He10830em', 'He10830em0', 'He10830em1','He10830exotic1','He10830exotic2']:
        ref_wav = 1.6
        textpos, axind = 1.42, 1
        ylim = False
        calc_widths = True
    elif classname in ['erraticm' ,'erraticm0', 'erraticm1', 'erraticmVO']:
        ref_wav = 1.7
        textpos, axind = 1.42, 1
        ylim = False
        calc_widths = False
    elif classname in ['emline']:
        ref_wav = 1.5
        textpos, axind = 1.42, 1
        ylim = False
        calc_widths = False
    elif classname in ['rcb', 'rcbkbump' ,'rcbV23']:
        ref_wav = 1.3
        textpos, axind = 1.42, 1
        ylim = False
        calc_widths = False
    elif classname == 'DYper':
        ref_wav = 1.7
        textpos, axind = 1.42, 1
        ylim = True
        ymax = 8
        ymin = 0
        calc_widths = False
    elif classname == 'yso':
        ref_wav = 1.7
        textpos, axind = 1.1, 0
        ylim = False
        calc_widths = False
    else:
        print('this class is not accounted for: ', classname)

    if ylim:
        return ref_wav, textpos, axind, ylim, ymax, ymin, calc_widths
    else:
        return ref_wav, textpos, axind, ylim, None, None, calc_widths