from pgir.utilsvar.count_groups import count_groups
import pandas as pd

obsfile = '/Users/earleyn138/Downloads/Gattini LAV census - complete_census.csv'
obs = pd.read_csv(obsfile)

work_dir = '/Users/earleyn138/Library/Mobile Documents/com~apple~CloudDocs/Research/grad/science/'
irtf_dir = work_dir + '/irtf_spectra/All_text_091201/'
data_dir = work_dir + 'pgir/pgir_vars/complete_census/'

line_dir = data_dir+'lineinfo/'


def main():
    count_groups(obs,data_dir,irtf_dir,line_dir)

if __name__ == "__main__":
    main()