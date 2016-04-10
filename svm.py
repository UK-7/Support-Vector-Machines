from __future__ import division
import cvxopt as cvx

import numpy as np
import syntheticData as sd
import sys
import matplotlib.pyplot as plt

'''
Computation of lagrange multipliers using CVXOPT package QP solver
Input: Data and Label X, Y as NP array, slack c as integer
Output: Lagrange Mulitpliers vector aplha
'''
def computeAlpha(X, Y, c):
      m = len(X)
      K = np.zeros((m,m))
      for i in range(m):
            for j in range(m):
                  K[i,j] = np.dot(X[i], X[j])
      P = cvx.matrix(np.outer(Y, Y) * K)
      q = cvx.matrix(np.ones(m) * -1)
      if c != None:
            g1 = np.asarray(np.diag(np.ones(m) * -1))
            g2 = np.asarray(np.diag(np.ones(m)))
            print np.append(g1, g2, axis=0)
            G = cvx.matrix(np.append(g1, g2, axis=0))
            h = cvx.matrix(np.append(np.zeros(m), (np.ones(m) * c), axis =0))
            print np.append(np.zeros(m), (np.ones(m) * c), axis =0)
      else:
            G = cvx.matrix(np.diag(np.ones(m) * -1))
            h = cvx.matrix(np.zeros(m))
      A = cvx.matrix(Y, (1,m), 'd')
      b = cvx.matrix(0.0)

      sol = cvx.solvers.qp(P, q, G, h, A, b)
      alpha = (sol['x'])
      alpha = np.ravel(alpha)
      primal = sol['primal objective']
      return alpha, primal

'''
Support Vector Machine implementation
Input: Data Matrix X, Label Y and slack limit c
Output: Weight parameters W and bias W_0
'''
def svm(X, Y, c=None):
      alpha, primal = computeAlpha(X, Y, c)
      print alpha
      sv = alpha > 1e-6
      ind = np.arange(len(alpha))[sv]
      alpha_sv = alpha[sv]
      sv_y = Y[sv]
      sv = X[sv]
      print "%d support vectors found" % len(sv)
     
      W = np.sum((alpha*Y).reshape(len(X), 1)*X, axis=0)
      b = np.sum(np.dot(sv, W) - sv_y)
      return W, b, ind
    

if __name__ == "__main__":
      X, Y = sd.seperable(samples=1000, margin=1)
      W, b, ind = svm(X, Y)
      sd.plotData(X, Y, "Seperable", ind)
      X, Y = sd.inseparable(samples=1000)
      W, b, ind = svm(X, Y)
      sd.plotData(X, Y, "Inseperable", ind)

