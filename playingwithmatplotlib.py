import matplotlib.pyplot as lt
lt.rcParams['axes.facecolor'] = 'grey'
lt.figure().patch.set_facecolor('xkcd:purple')
x=[1,1,5,5]
y=[2,1.8,1.8,2]
lt.plot(x,y)
lt.fill_between([1,1.2,1.2,1,1],[3,3,2.75,2.75,3])
lt.fill_between([4.8,5,5,4.8,4.8],[3,3,2.75,2.75,3])
lt.fill_between([3,2.5,3.5,3],[2.6,2.4,2.4,2.6])
lt.legend()
lt.show()
