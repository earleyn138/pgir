#!/bin/sh
python plot_spec.py 0 10 lpvs1 'M7-III:_HD108849.txt' 'M7-III, HD108849'
python plot_spec.py 10 20 lpvs2 'M7-III:_HD108849.txt' 'M7-III, HD108849'
python plot_spec.py 20 27 lpvs3 'M7-III:_HD108849.txt' 'M7-III, HD108849'
python plot_spec.py 27 35 miras 'M7-III:_HD108849.txt' 'M7-III, HD108849'
python plot_spec.py 38 53 mdips 'M7-III:_HD108849.txt' 'M7-III, HD108849'
python plot_spec.py 53 57 He10830ems 'M7-III:_HD108849.txt' 'M7-III, HD108849'
python plot_spec.py 57 73 cstars 'C7,6e(N4)_HD31996.txt' 'C7,6e(N4), HD31996'
python plot_spec.py 73 80 emline 'M7-III:_HD108849.txt' 'M7-III, HD108849'
python plot_spec.py 80 84 yso 'M7-III:_HD108849.txt' 'M7-III, HD108849'
python plot_spec.py 84 91 hbandbump 'M10+III_IRAS14086-0703.txt' 'M10+III, IRAS14086-0703'
python plot_spec.py 91 101 15micronabs 'C7,6e(N4)_HD31996.txt' 'C7,6e(N4), HD31996'
python plot_spec.py 101 115 rcb 'C-N4.5C24.5_HD92055.txt' 'C-N4.5C24.5, HD92055'

