import numpy as np

def gradient_descent(x,y):
    m_curr = b_curr = 0
    iterations = 10000

    for i in range(iterations):
        y_pred = m_curr * x + b_curr
        cost = (1 / len(x)) * sum([val**2 for val in (y-y_pred)])
        md = -(2 / len(x)) * sum(x * (y - y_pred))
        bd = -(2 / len(x)) * sum(y - y_pred)
        m_curr = m_curr - 0.01 * md
        b_curr = b_curr - 0.01 * bd
        print("m {}, b {}, cost {}, iteration {}".format(m_curr, b_curr, cost, i)) #"m_curr, b_curr)

x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])

gradient_descent(x,y)