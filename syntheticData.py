import numpy as np
import matplotlib.pyplot as plt

'''
Generate a series of random points on in a normal distribution
based on the variable of distribution provided
Input: Range, Mu, Sigma
Output: Randoom sequence of point
'''
def generateRandomData(x, mu, sigma):
      X = sigma * np.random.randn(x, 2) + mu
      return X


'''
Create linearly seperable random 2D data points
Input: No of samples. default = 1000
Output: 2D np array of data X,  1D np array of labels Y
'''
def seperable(samples = 1000, margin = 1):
      Y = []
      X = []
      while len(X) < samples:
            point = generateRandomData(1, samples/2, samples/6)
            diff = point[0,0] - point[0,1]
            if diff >= 0:
                  if(diff >= margin):
                        X.append(point[0])
                        Y.append(1)
            else:
                  if(diff <= (0-margin)):
                        X.append(point[0])
                        Y.append(-1)
      X = np.asarray(X)
      return np.asarray(X), np.asarray(Y)

'''
Create linearly inseperable random 2D data points
Input: No of samples. Default = 1000
Output: 2D np array of data X, 1D np array of labels Y
'''
def inseparable(samples = 1000):
      Y = np.ones(samples)
      Y[:(samples/2)] = -1
      np.random.shuffle(Y)
      X = generateRandomData(samples, (samples/2), (samples/6))
      return X, Y

'''
Plot given data points according to labels
Input: np array of data X, np array of labels Y
Output: null
'''
def plotData(X,Y, plotTitle, ind=None):
      fig  = plt.figure()
      ax = fig.add_subplot(111)
      for point, label in zip(X,Y):
            if label == 1:
                  ax.scatter(point[1], point[0], alpha=0.4, color="red", marker="o")
            else:
                  ax.scatter(point[1], point[0], alpha=0.4, color="blue", marker="o")
      for i in ind:
            print X[i]
            ax.scatter(X[i,1], X[i,0], s=100, alpha = 0.6, color="green")
      ax.plot(range(len(X)))
      plt.title(plotTitle)
      plt.axis("tight")
      plt.show()


'''
Main Function
'''
if __name__ == "__main__":
      X, Y = seperable(margin = 50)
      plotData(X,Y,"Seperable")
      X, Y = inseparable()
      plotData(X,Y,"Inseperable")


