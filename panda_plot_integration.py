from matplotlib import pyplot as plot 
import random
import pandas as panda

united_nations_immigration_data_remote_location = "https://ibm.box.com/shared/static/lw190pt9zpy5bd1ptyg2aw15awomz9pu.xlsx"

immigration_to_canada_data = panda.read_excel(united_nations_immigration_data_remote_location, \
                            sheet_name='Canada by Citizenship', \
                            skiprows=range(20), \
                            skipfooter=2
                             )

immigration_to_canada_data.columns = list(map(str, immigration_to_canada_data.columns))
# print(immigration_to_canada_data.columns.tolist())

def draw_united_nations_migration_line_plot_for_country(country):
    
    immigration_to_canada_data.set_index('OdName', inplace=True)
    print(immigration_to_canada_data.head(2))
    # print(immigration_to_canada_data.loc['Haiti'])
    
    years = list( map(str,range(1980, 2013)))
    data_frame = immigration_to_canada_data.loc[country, years]
    print(data_frame)
    data_frame.head()
    data_frame.plot()
    plot.title("Migration data")
    plot.xlabel("Years")
    plot.ylabel("Number of Migrants")
    plot.show()
    

def draw_sample_histogram():
    
    random_ten_thousand_numbers = random.sample(range(600000), 10000)

    plot.hist(random_ten_thousand_numbers, color="black")
    plot.title("Random sampliing of ten thousand numbres")
    plot.show()


draw_united_nations_migration_line_plot_for_country('Haiti')
