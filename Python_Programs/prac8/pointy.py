import geometry

print(dir(geometry))

def pointyShapeVolume(x,y,square_base):
    if square_base:
        base_area = geometry.square_area(x)
        vol = base_area*y/3
        print("Volume of pyramid: ",vol)
    else:
        base_area = geometry.circle_area(x)
        vol = base_area*y/3
        print("Volume of cone: ", vol)

print("Cone")
pointyShapeVolume(3,4,False)
print("Pyramid")
pointyShapeVolume(3,4,True)
   