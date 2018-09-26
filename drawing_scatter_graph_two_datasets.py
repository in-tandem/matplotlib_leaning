
## i am going to plot using simple lists of data
## i am going to draw a scatter plot
## i am going to label x and y axis
## i am going to add color
## i am adding title to the graph
## i am going to add legend

import matplotlib.pyplot as plot

print('i am going to draw a simple graph')

x_axis = [10, 20, 3, 40, 66, 89, 55 ]
y_axis = [42.2, 81.1, 0, 3.8, 9, 99, 86]


_stats_x_axis = [10, 20, 3, 40, 66, 89, 55 ]
_stats_y_axis = [44, 33, 65, 88, 22, 10, 30]



plot.scatter(_stats_x_axis,_stats_y_axis, color="red", label='LS-101') ## simply chaging plot.plot to plot.scatter

plot.scatter(x_axis,y_axis, color="blue", label='CS-213') ## simply chaging plot.plot to plot.scatter
plot.xlabel("Number of Students")
plot.ylabel("Percentages scored in Machine Learning class CS - 213 / Linear Statistics")
plot.title("Student scores in Machine Learning Courses")
plot.legend(loc='upper left')
plot.show()