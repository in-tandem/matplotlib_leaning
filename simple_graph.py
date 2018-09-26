
## i am going to plot using simple lists of data
## i am going to label x and y axis
## i am going to add color
## i am adding title to the graph
import matplotlib.pyplot as plot

print('i am going to draw a simple graph')

x_axis = [10, 20, 30, 40, 66, 89]
y_axis = [2.2, 1.1, 0, 3, -9, 99]

plot.plot(x_axis,y_axis, color="blue")
plot.xlabel("Number of Routers")
plot.ylabel("Distances from Master Router( -ve means inner circle) ")
plot.title("some graph silly silly")
plot.show()