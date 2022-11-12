import numpy as np
import matplotlib.pyplot as plt

num_sample=1000
data=1+(100-1)*np.random.random([2,num_sample])
plt.figure(1)
plt.subplot(2,1,1)
plt.plot(data[0,:],data[1,:],'ro')
plt.subplot(2,1,2)


for i in range(num_sample):
    if(data[0,i]>=50 and data[1,i]>=50):
        plt.plot(data[0,i],data[1,i],'ro')
    elif(data[0,i]>=50 and data[1,i]<50):
         plt.plot(data[0,i],data[1,i],'bo')
    elif(data[0,i]<50 and data[1,i]<50):
        plt.plot(data[0,i],data[1,i],'cs')
    else:
        plt.plot(data[0,i],data[1,i],'bd')

plt.show()
