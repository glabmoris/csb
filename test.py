import georeference
import uncertainty
import math

#TODO formalize unit tests

latitude = math.radians(48.4525) 
longitude = math.radians(-68.5232)
ellipsoidal_height = -28
heading = math.radians(350)
pitch = math.radians(0.5)
roll = math.radians(1.5)
depth = 5
offset_x = 1
offset_y = 2
offset_z = 3
latitude_sigma = 0.00001
longitude_sigma = 0.0001
ellipsoidal_height_sigma = 1
heading_sigma = 1
pitch_sigma = 1
roll_sigma = 1
depth_sigma = 0.5
offset_x_sigma = 0.0000001
offset_y_sigma = 0.0000001
offset_z_sigma = 0.0000001


print("Georeferencing")
g = georeference.Georeference()

print("Raw position:")
print(g.llh2ecef(latitude,longitude,ellipsoidal_height))

print("Sounding position:")
print(g.compute(latitude,longitude,ellipsoidal_height,heading,pitch,roll,depth,offset_x,offset_y,offset_z))

print("Uncertainty")
u = uncertainty.TotalPropagatedUncertainty()

tpu = u.compute(latitude,longitude,ellipsoidal_height,heading,pitch,roll,depth,offset_x,offset_y,offset_z,latitude_sigma,longitude_sigma,ellipsoidal_height_sigma,heading_sigma,pitch_sigma,roll_sigma,depth_sigma,offset_x_sigma,offset_y_sigma,offset_z_sigma)

print(tpu)
error_x=math.sqrt(tpu[0][0])
error_y=math.sqrt(tpu[1][1])
error_z=math.sqrt(tpu[2][2])

print(f"Approximate x error: {error_x:.3f} m")
print(f"Approximate y error: {error_y:.3f} m")
print(f"Approximate z error: {error_z:.3f} m")
