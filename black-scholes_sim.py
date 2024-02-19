import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as ss

M = 700
T = 1.0
dt = T/(M-1)
sigma = 0.20
r = 0.06
K=99.0

t = np.linspace(0, T, M)
S = np.empty(M)
V = np.empty(M)

#call option price at t=0
def C0():
    d1 = np.log(S[0]/K) + (r+sigma**2 / 2) * T
    d2 = d1 - sigma*np.sqrt(T)
    return S[0]*N(d1) - np.exp(-r*T)*K*N(d2)

def N(x):
    return ss.norm.cdf(x)

#delta-parameter at time t
def delta(t, sigma=sigma): 
    i = int(t/dt)
    d1 = np.log(S[i]/K) + (r+sigma**2 / 2) * (T-t)
    return N(d1)


S[0] = 100.0
V[0] = C0()

#calculate stock price
for i in range(M-1):

    Z_m = np.random.normal()
    S[i+1] = S[i] + \
          r*S[i]*dt + \
              sigma*S[i]*np.sqrt(dt)*Z_m

#calculate call option price
for i in range(M-1):

    #example for "weekly" hedge adjustment, meaning only update the call option price every 7th timeinterval:
    if i % 7 == 0:
        V[i+1] = V[i] + \
            delta(i*dt, sigma=0.2) * \
                (S[i+1]-S[i])
    else: V[i+1] = V[i]

plt.xlabel("t")
plt.ylabel("price")
plt.plot(t, S, label="S_t")
plt.plot(t, V, label="C_t")
plt.legend()
plt.show()