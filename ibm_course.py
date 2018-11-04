import pandas as panda 
from matplotlib import pyplot as plot


remote_location = 'https://cocl.us/datascience_survey_data'

data = panda.read_csv(remote_location, index_col=0)

print(data)

data.sort_values(inplace = True, by = 'Very interested', ascending = False)

data['Very interested'] = (data['Very interested']/2233) * 100 

data['Somewhat interested'] = (data['Somewhat interested']/2232) * 100 
data['Not interested'] = (data['Not interested']/ 2232) * 100


# print(data)
# import matplotlib as mpl
# mpl.rcParams['toolbar'] = 'None'


axes = data.plot(kind='bar', figsize = (20, 8), color = ['#5cb85c','#5bc0de','#d9534f'], width = 0.8)
axes.set_title('Percentage of Respondent\'s Interest In Data Science Areas', {'fontsize': 16})
# axes.set_ylabel('')
axes.get_yaxis().set_visible(False)
# axes.get_xaxis().set_visible(False)
axes.legend(fontsize = 14)
axes.spines['top'].set_visible(False)
axes.spines['right'].set_visible(False)

# axes.spines['bottom'].set_visible(False)
axes.spines['left'].set_visible(False)


# set individual bar lables using above list
for i in axes.patches:
    # get_x pulls left or right; get_height pushes up or down
    axes.text(i.get_x(), i.get_height()+ 2, \
            str(round(i.get_height(), 2))+'%', fontsize=10,
                color='black', bbox=dict(facecolor='dimgrey', alpha=0.5))

plot.tight_layout()
plot.show()

# plot.axis('off')