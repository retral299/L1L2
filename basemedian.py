import pyfiglet
import xlsxwriter
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics
import os
import sys
from statistics import StatisticsError

R = '\033[31m'
G = '\033[32m'
Y = '\033[33m'
C = '\033[36m'
W = '\033[0m'

splitter = '='*50

def ban():

    print(f'''{C+pyfiglet.figlet_format("L1---L2")}
{R+splitter+W}''')

def lister():

    print(G+f'''2. 2G Calculation
3. 3G Calculation
4. 4G Calculation
{R+splitter+W}''')


df_2 = pd.read_excel('test_real.xlsx', sheet_name='Sheet1')
# df_3 = pd.read_excel('test_data.xlsx', sheet_name='Sheet2')
# df_4 = pd.read_excel('test_data.xlsx', sheet_name='Sheet3')

astro_2 = df_2.to_dict('records')
# astro_3 = df_3.to_dict('records')
# astro_4 = df_4.to_dict('records')


if __name__ == '__main__':

    while True:

        os.system('cls' if os.name == 'nt' else 'clear')

        userCh = int(input('Tech as integer : '))

        match userCh:

            case 2:

                main_cell_source_index_2 = df_2[['cell_ref']].dropna()
                main_cell_source_index_2 = np.asanyarray(main_cell_source_index_2).flatten()
                main_cell_source_index_2 = list(np.nan_to_num(main_cell_source_index_2))

                for z in range(len(main_cell_source_index_2)):

                    #---------------------------------- 2G KPIs
                    kpi_1 = []

                    for i in range(len(astro_2)):

                        if astro_2[i]['cell'] == main_cell_source_index_2[z]:

                            kpi_1.append(astro_2[i]['tbf_establishment_success_rate(ul+dl)(%)(hu_cell)'])

                        else:

                            continue                

                    print(f'cell : {C+main_cell_source_index_2[z]+W}')
                    print(Y+'tbf_establishment_success_rate(ul+dl)(%)(hu_cell)'+W, f'= {kpi_1}'+G,
                        f'Median : {float(statistics.median(kpi_1))}'+W)
                    

                print(R+splitter+W)
                userfdec = input(C+'2G calculation Done! continue? [y/n] : '+W)

                userfdec = userfdec.lower()

                

          

        
