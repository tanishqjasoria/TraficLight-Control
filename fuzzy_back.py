
# coding: utf-8

# In[9]:


import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
import setparam as sp

# In[77]:


def fuzzy(var_car,car_confi,var_truck,truck_confi,var_bike,bike_confi,obj):
    n_truck=obj.truck_capacity()
    n_car=obj.car_capacity()
    n_bike=obj.motor_capacity()
    
    A,B,C=obj.get_value()

    x_truck = np.arange(0,n_truck , 1)
    x_car= np.arange(0,n_car, 1)
    x_bike= np.arange(0,n_bike, 1)
    
    list=truck_confi
    
    #for truck
    min_truck=0
    i=0

    for i in range(0,len(list)):
        if(list[i]>90):
            min_truck+=1
    ##print(min_truck)
    
    max_truck,i=0,0
    for i in range(0,len(list)):
        if(list[i]>50):
            max_truck+=1
    #print(max_truck)
    
    sum_truck=0
    for i in list:
        if (i>50 and i<90):
            sum_truck=sum_truck+i
    sum_truck/=100
    avg_truck=sum_truck+min_truck
    #print(avg_truck)

    #for car
    list=car_confi
    min_car=0
    i=0
    for i in range(0,len(list)):
        if(list[i]>90):
            min_car+=1
    max_car,i=0,0
    for i in range(0,len(list)):
        if(list[i]>50):
            max_car+=1

    sum_car=0
    for i in list:
        if (i>50 and i<90):
            sum_car=sum_car+i
    sum_car/=100
    avg_car=sum_car+min_car
    #print(avg_car)

    #for bike
    list=bike_confi
    min_bike=0
    i=0
    for i in range(0,len(list)):
        if(list[i]>90):
            min_bike+=1
    max_bike,i=0,0
    for i in range(0,len(list)):
        if(list[i]>50):
            max_bike+=1

    sum_bike=0
    for i in list:
        if (i>50 and i<90):
            sum_bike=sum_bike+i
    sum_bike/=100
    avg_bike=sum_bike+min_bike
    #print(avg_bike)

    #for congestion
    min_congestion=min_truck/n_truck+min_car/n_car+min_bike/n_bike
    max_congestion=max_truck/n_truck+max_car/n_car+max_bike/n_bike
    avg_congestion=avg_truck/n_truck+avg_car/n_car+avg_bike/n_bike
    '''
    min_congestion=round(min_congestion,2)
    max_congestion=round(max_congestion,2)
    avg_congestion=round(avg_congestion,2)
    #print (min_congestion,max_congestion,avg_congestion)
    '''
    #Defuzzification
    x_congestion = np.arange(0,1.01,.01,dtype=float)
    np.float64(x_congestion)
    congestion_mf=fuzz.trimf(x_congestion, [round(min_congestion,2),round(avg_congestion,2),round(max_congestion,2)])
    #fig, ax0 = plt.subplots(figsize=(8, 9))

    value=fuzz.defuzzify.dcentroid(x_congestion, congestion_mf, 0.0)
    #print(value)
    

    # Generate fuzzy membership functions
    """ 
    truck_low = fuzz.trimf(x_truck, [0, 0, 6])
    truck_med = fuzz.trapmf(x_truck, [3, 7, 9,13])
    truck_high = fuzz.trimf(x_truck, [10, 16,16])
    car_low = fuzz.trimf(x_car, [0, 0, 10])
    car_med = fuzz.trapmf(x_car, [5, 12,18,25])
    car_high = fuzz.trimf(x_car, [20, 30, 30])
    bike_low = fuzz.trimf(x_bike, [0, 0, 50])
    bike_med = fuzz.trapmf(x_bike, [30,60,90,120])
    bike_high= fuzz.trimf(x_bike, [100,150,150])"""


    # In[59]:


    x_truck=np.arange(0,n_truck,1)
    x_car=np.arange(0,n_car,1)
    x_bike=np.arange(0,n_bike,1)

    truck_mf=fuzz.trimf(x_truck,[min_truck,avg_truck,max_truck])
    car_mf=fuzz.trimf(x_car,[min_car,avg_car,max_car])
    bike_mf=fuzz.trimf(x_bike,[min_bike,avg_bike,max_bike])

    truck_low = fuzz.trimf(x_truck, B[0])
    truck_med = fuzz.trapmf(x_truck, B[1])
    truck_high = fuzz.trimf(x_truck, B[2])
    car_low = fuzz.trimf(x_car, A[0])
    car_med = fuzz.trapmf(x_car, A[1])
    car_high = fuzz.trimf(x_car, A[2])
    bike_low = fuzz.trimf(x_bike, C[0])
    bike_med = fuzz.trapmf(x_bike, C[1])
    bike_high= fuzz.trimf(x_bike, C[2])


    # In[67]:

    '''
    # Visualize these universes and membership functions
    fig, (ax0, ax1, ax2,ax3) = plt.subplots(nrows=4, figsize=(8, 9))

    """"ax0.plot(x_truck, truck_low, 'b', linewidth=1.5, label='Bad')
    ax0.plot(x_truck, truck_med, 'g', linewidth=1.5, label='Decent')
    ax0.plot(x_truck, truck_high, 'r', linewidth=1.5, label='Great')
    ax0.set_title('truck')"""
    ax0.plot(x_congestion, congestion_mf, 'b', linewidth=1.5, label='congestion')
    ax0.set_title('congestion')
    ax0.legend()

    """ax1.plot(x_car, car_low, 'b', linewidth=1.5, label='Poor')
    ax1.plot(x_car, car_med, 'g', linewidth=1.5, label='Acceptable')"""
    ax1.plot(x_car, car_mf, 'r', linewidth=1.5, label='car')
    ax1.plot(x_car, car_low, 'b', linewidth=1.5, label='Poor')
    ax1.plot(x_car, car_med, 'g', linewidth=1.5, label='Acceptable')
    ax1.plot(x_car, car_high, 'r', linewidth=1.5, label='Amazing')
    ax1.set_title('car')
    ax1.legend()

    """ax2.plot(x_bike, bike_low, 'b', linewidth=1.5, label='Low')
    ax2.plot(x_bike, bike_med, 'g', linewidth=1.5, label='Medium')"""
    ax2.plot(x_bike, bike_mf, 'r', linewidth=1.5, label='bike')
    ax2.plot(x_bike, bike_low, 'b', linewidth=1.5, label='Low')
    ax2.plot(x_bike, bike_med, 'g', linewidth=1.5, label='Medium')
    ax2.plot(x_bike, bike_high, 'r', linewidth=1.5, label='High')
    ax2.set_title('bike')
    ax2.legend()

    """ax3.plot(x_truck, truck_low, 'b', linewidth=1.5, label='Low')
    ax3.plot(x_truck, truck_med, 'g', linewidth=1.5, label='Medium')"""
    ax3.plot(x_truck, truck_mf, 'r', linewidth=1.5, label='truck')
    ax3.plot(x_truck, truck_low, 'b', linewidth=1.5, label='Bad')
    ax3.plot(x_truck, truck_med, 'g', linewidth=1.5, label='Decent')
    ax3.plot(x_truck, truck_high, 'r', linewidth=1.5, label='Great')
    ax3.set_title('truck')
    ax3.legend()

	'''
    # Turn off top/right axes
    """for ax in (ax0, ax1, ax2,ax3):
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.get_xaxis().tick_bottom()
        ax.get_yaxis().tick_left()"""

    #plt.tight_layout()
    #plt.show()

    if(value<0.33):
        congestion="low"
        flag=1
    elif(value>0.33 and value<0.66):
        congestion="medium"
        flag=2
    elif(value>0.66 and value<1):
        congestion="high"
        flag=3

    obj.set_congestion_value(flag)
