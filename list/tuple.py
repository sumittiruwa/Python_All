# Tuple creation

point = (10.2,20.3)  #2d coordinates
rgb = (255,128,0)  #color
person = ("krishna", 21, "BCA") # record

# tuple as dict key (list can't do this!)

locations = {(29.8, 77.3): "Bhaktapur", (19.0, 65.2): "patan"}

print(locations[(29.8,77.3)])

# single -element tuple -needs tralling comme

one = (42)
print(type(one))