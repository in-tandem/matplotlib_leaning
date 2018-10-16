from matplotlib import pyplot as plot 
import random
import pandas as panda

united_nations_immigration_data_remote_location = "https://ibm.box.com/shared/static/lw190pt9zpy5bd1ptyg2aw15awomz9pu.xlsx"

immigration_to_canada_data = panda.read_excel(united_nations_immigration_data_remote_location, \
                            sheet_name='Canada by Citizenship', \
                            skiprows=range(20), \
                            skipfooter=2
                             )

# convert all column names to string values
immigration_to_canada_data.columns = list(map(str, immigration_to_canada_data.columns))

# convert all columns names to lowercase 
immigration_to_canada_data.rename(str.lower, inplace=True, axis='columns')

# rename a few columns for our convinience
immigration_to_canada_data.rename(columns = {'odname' : 'country', 'areaname':'continent'}, inplace=True)

# add an additional column called total 
immigration_to_canada_data['total'] = immigration_to_canada_data.sum(axis=1, numeric_only= True)

def draw_united_nations_migration_line_plot_for_country(country):
     
    immigration_to_canada_data.set_index('country', inplace=True)
    # print(immigration_to_canada_data.head(2))
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
    

def draw_immigration_country_wise_area_chart():

    immigration_to_canada_data.reset_index()
    immigration_to_canada_data.sort_values(['total'], ascending = False, inplace = True)

    years = list(map(str,range(1980,2014)))
    columns = ['country'] + years

    ## use only the columns you require, and take the topmost 5 countries
    data_frame = immigration_to_canada_data[columns].head()
    
    ## index which is set in pandas is used to plot in x axis. we would hence transpose
    data_frame.set_index('country', inplace = True)
    
    data_frame = data_frame.transpose()

    ## my columns are going to become rows. now remember i converted my columns to strings
    ## unless i change them back to numeric, x values will come as empty
    data_frame.index = data_frame.index.map(int) 

    data_frame.plot(kind= 'area')
    plot.title("Area Chart of Top Five Migrating nations")
    plot.xlabel("Years")
    plot.ylabel("Number of Migrants")
    plot.show()


def draw_sample_histogram():
    
    random_ten_thousand_numbers = random.sample(range(600000), 10000)

    plot.hist(random_ten_thousand_numbers, color="black")
    plot.title("Random sampliing of ten thousand numbres")
    plot.show()

def draw_histogram_for_migration_in_particular_year(year):
    immigration_to_canada_data.reset_index()
    immigration_to_canada_data.sort_values(['total'], ascending = False, inplace = True)

    years = list(map(str,range(1980,2014)))
    columns = ['country'] + years

    ## use only the columns you require, and take the topmost 5 countries
    data_frame = immigration_to_canada_data[columns]
    
    ## index which is set in pandas is used to plot in x axis. we would hence transpose
    data_frame.set_index('country', inplace = True)
    
    data_frame = data_frame.transpose()

    ## my columns are going to become rows. now remember i converted my columns to strings
    ## unless i change them back to numeric, x values will come as empty
    data_frame.index = data_frame.index.map(int) 

    print(data_frame.loc[year])

    data_frame.loc[year].plot(kind='hist', color='purple')

    plot.title("HIstogram showing migration across globe for the year %d" %year)
    plot.xlabel("Number of Migrants")
    plot.ylabel("Number of Countries")
    plot.show()


draw_histogram_for_migration_in_particular_year(2013)


# draw_immigration_country_wise_area_chart()
# draw_united_nations_migration_line_plot_for_country('Haiti')
