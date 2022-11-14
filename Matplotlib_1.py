import numpy as np
import matplotlib.pyplot as plt

num_sample=3000
data=1+(100-1)*np.random.random([2,num_sample])

plt.figure(1)
plt.ion()

C1_X=data[0,0]
C1_Y=data[1,0]

C2_X=data[0,1]
C2_Y=data[1,1]

C3_X=data[0,2]
C3_Y=data[1,2]

C4_X=data[0,3]
C4_Y=data[1,3]


for it in range(30):
    plt.cla()
    C11_X=[];C11_Y=[]
    C22_X=[];C22_Y=[]
    C33_X=[];C33_Y=[]
    C44_X=[];C44_Y=[]

    for i in range(num_sample):
        d1=np.sqrt((data[0,i]-C1_X)**2+(data[1,i]-C1_Y)**2)
        d2=np.sqrt((data[0,i]-C2_X)**2+(data[1,i]-C2_Y)**2)
        d3=np.sqrt((data[0,i]-C3_X)**2+(data[1,i]-C3_Y)**2)
        d4=np.sqrt((data[0,i]-C4_X)**2+(data[1,i]-C4_Y)**2)
        if(d1<d2 and d1<d3 and d1<d4):
            C11_X.append(data[0,i])
            C11_Y.append(data[1,i])
            plt.plot(data[0,i],data[1,i],'ro')
        elif(d2<d1 and d2<d3 and d2<d4):
            C22_X.append(data[0,i])
            C22_Y.append(data[1,i])
            plt.plot(data[0,i],data[1,i],'bd')
        elif(d3<d1 and d3<d2 and d3<d4):
            C33_X.append(data[0,i])
            C33_Y.append(data[1,i])
            plt.plot(data[0,i],data[1,i],'gd')   
        else:
            C44_X.append(data[0,i])
            C44_Y.append(data[1,i])
            plt.plot(data[0,i],data[1,i],'yo')
    C1_X=sum(C11_X)/len(C11_X)
    C1_Y=sum(C11_Y)/len(C11_Y)
    
    C2_X=sum(C22_X)/len(C22_X)
    C2_Y=sum(C22_Y)/len(C22_Y)

    C3_X=sum(C33_X)/len(C33_X)
    C3_Y=sum(C33_Y)/len(C33_Y)

    C4_X=sum(C44_X)/len(C44_X)
    C4_Y=sum(C44_Y)/len(C44_Y)




    plt.title(str(it+1))
    print("Iternation number is="+str(it+1))
        
    plt.plot(C1_X,C1_Y,'k*')
    plt.plot(C2_X,C2_Y,'k*')
    plt.plot(C3_X,C3_Y,'k*')
    plt.plot(C4_X,C4_Y,'k*')

    plt.pause(0.3)       

    




plt.ioff()
