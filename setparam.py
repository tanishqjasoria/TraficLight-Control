import numpy as np
import configparser
#Congfigratuion file reader, donot edit anything in this code
def ConfigSectionMap(section):
    dict1 = {}
    options = config.options(section)
    for option in options:
        try:
            dict1[option] = config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1

config = configparser.ConfigParser()
config.read('config/config.ini')

class Path():
	"""docstring for ClassName"""
	def __init__(self, cam_range,num_lanes):
		#super(Vehicle, self).__init__()
		self.cam_range = cam_range
		self.num_lanes=num_lanes#Num of lanes
		self.car_len=float(ConfigSectionMap("Parameters")['carlen'])#Length of car
		self.truck_len=float(ConfigSectionMap("Parameters")['trucklen'])
		self.motor_len=float(ConfigSectionMap("Parameters")['motorlen'])
		self.congestion=0
	def car_capacity(self):
		return np.floor((self.cam_range/self.car_len)*self.num_lanes)
	def truck_capacity(self):
		return np.floor((self.cam_range/self.truck_len)*self.num_lanes)
	def motor_capacity(self):
		return np.floor((self.cam_range/self.motor_len)*self.num_lanes*2)#2 multipled because two bikes can accomadte per lane
	def get_value(self):
		cc=np.floor((self.cam_range/self.car_len)*self.num_lanes)#car capacity
		tl=np.floor((self.cam_range/self.truck_len)*self.num_lanes)#Truck capacity
		ml=np.floor((self.cam_range/self.motor_len)*self.num_lanes*2)#Motor Capacity
		valuecar_max=30#Dont Disturb this, set values h
		valuebike_max=150#Dont disturb, dont dare touch it
		A =[[0,0,6.0*cc//16],[3*cc//16,(7.0*cc//16),9.0*cc//16,13.0*cc//16],[10.0*cc//16,16.0*cc/16,cc]]
		B =[[0,0,10.0*tl//valuecar_max],[5*tl//valuecar_max,(12.0*tl//valuecar_max),18.0*tl//valuecar_max,25.0*tl//valuecar_max],[20.0*tl//valuecar_max,tl,tl]]
		C =[[0,0,50.0*ml//valuebike_max],[30*ml//valuebike_max,(60.0*ml//valuebike_max),90.0*ml//valuebike_max,120.0*ml//valuebike_max],[100.0*ml//valuebike_max,ml,ml]]
		return A,B,C
	def set_congestion_value(self,congestion):
		self.congestion=congestion#Gives you congestion output
'''
lis=[]
Ge=Path(2,3)
lis.append(Ge)
Ge=Path(4,5)
lis.append(Ge)
print lis[1].car_capacity()
A,B,C=lis[1].get_value()
print A[2]
lis[1].set_congestion_value(4)
print lis[0].congestion
print Ge.get_value
'''