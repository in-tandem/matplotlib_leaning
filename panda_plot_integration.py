from matplotlib import pyplot as plot 
import random
import pandas as panda
import numpy

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

    # print(data_frame.loc[year]) data is a country name - number of migrants table

    data_frame = data_frame.loc[year]

    ## even distribution on the x axis
    count, _edges = numpy.histogram(data_frame)

    data_frame.plot(kind='hist', color='purple', xticks = _edges, figsize = (20,10))

    plot.title("HIstogram showing migration across globe for the year %d" %year)
    plot.xlabel("Number of Migrants")
    plot.ylabel("Number of Countries")
    plot.show()

def draw_bar_chart_for_a_country_trend(country):

    immigration_to_canada_data.reset_index()
    immigration_to_canada_data.set_index('country', inplace = True)
    immigration_to_canada_data.sort_values(['total'], ascending = False, inplace = True)

    years = list(map(str,range(1980,2014)))
    
    ## use only the columns you require, and take the topmost 5 countries
    data_frame = immigration_to_canada_data.loc[country, years]
    
    data_frame.plot(kind='bar', color='red', figsize = (20,10))

    plot.title("Bar Chart showing migration trends from %s " %country)
    plot.xlabel("Number of Migrants")
    plot.ylabel("Number of Countries")
    plot.show()

def draw_histogram_migration_trends_for_a_year_multiple_countries(year, countries):

    immigration_to_canada_data.reset_index()
    immigration_to_canada_data.sort_values(['total'], ascending = False, inplace = True)

    years = list(map(str,range(1980,2014)))
    columns = ['country'] + years

    ## use only the columns you require, and take the topmost 5 countries
    data_frame = immigration_to_canada_data[columns]
    
    ## index which is set in pandas is used to plot in x axis. we would hence transpose
    data_frame.set_index('country', inplace = True)
    
    data_frame = data_frame.loc[countries].transpose()

    ## my columns are going to become rows. now remember i converted my columns to strings
    ## unless i change them back to numeric, x values will come as empty
    data_frame.index = data_frame.index.map(int) 

    print(data_frame)
    ## even distribution on the x axis
    count, _edges = numpy.histogram(data_frame, 15)

    data_frame.plot(
                    kind = 'hist', \
                    alpha=0.6, \
                    bins = 15, \
                    color = ['coral', 'darkslateblue', 'mediumseagreen'], \
                    xticks = _edges, \
                    figsize = (20,10) \
                    )

    plot.title("Histogram showing migration across globe for the countries %s" %countries)
    plot.xlabel("Number of Migrants")
    plot.ylabel("Number of Years")
    plot.show()
    

def draw_pie_migration_across_continents():
    immigration_to_canada_data.reset_index()
    data_frame = immigration_to_canada_data.groupby('continent', axis=0).sum()
    data_frame['total'].plot(kind = 'pie')

    plot.title("Migration trends across continents")
    plot.show()


def draw_scatter_plot_migration_totals_all_years():

    immigration_to_canada_data.reset_index()
    
    years = list(map(str, range(1980,2014)))

    data_frame = panda.DataFrame(immigration_to_canada_data[years].sum(axis = 0))
    data_frame.index = map(int, data_frame.index)
    data_frame.reset_index(inplace = True)
    data_frame.columns = ['year', 'total']
    data_frame.plot(kind='scatter', x = 'year', y = 'total')
    plot.title("Ïmmigration totals over the years")
    plot.xlabel("Years")
    plot.ylabel("Total")
    plot.show()

draw_scatter_plot_migration_totals_all_years()
# draw_pie_migration_across_continents()
# draw_histogram_migration_trends_for_a_year_multiple_countries(2013, ['India', 'China', 'Albania'])   
# draw_bar_chart_for_a_country_trend('India')
# draw_histogram_for_migration_in_particular_year(2013)
# draw_immigration_country_wise_area_chart()
# draw_united_nations_migration_line_plot_for_country('Haiti')
