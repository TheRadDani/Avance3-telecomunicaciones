import numpy as np
import matplotlib.pyplot as plt

percent=40.0
TimePeriod=10.0
Cycles=30
dt=0.01

t=np.arange(0,Cycles*TimePeriod,dt)
pwm= (t%TimePeriod) < (TimePeriod*percent/100)

x=np.linspace(-10,10,len(pwm))
y=(np.sin(x))

y[pwm == 0] = 0

plt.plot(t,y)

plt.ylim([-3,3])
plt.grid()
plt.show()