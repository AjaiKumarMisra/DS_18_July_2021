#from pylab import plot, show, legend, title,xlabel,ylabel,axis
import matplotlib.pyplot as a

def graph_draw():
    x_2000=[43.9,46.3,46.4,43.4,44.5,45.8,46.8,45.0,45.3,44.0,46.7,46.4]
    x_2006=[53.8,56.5,56.9,53.6,54.9,55.1,56.8,55.2,55.63,54.1,56.2,56.3]
    x_2012=[33.3,36.7,36.1,33.9,34.9,35.1,36.3,35.7,35.4,34.4,36.1,36.9]

    y=range(2000,2013)
    months=range(1,13)
    a.title('Average monthly temp')
    a.xlabel('Month')
    a.ylabel('Temp')
    a.plot(months,x_2000,months,x_2006,months,x_2012,marker='o')
    a.savefig('myfirstimage2.png')
    a.legend([2000,2006,2012])
    a.axis(ymin=0)
    a.show()
    
    
    
if __name__=='__main__':
    graph_draw()