import numpy as np

text = False

while text is False:
    value = input("What is the temperature?")
    if value == "":
        continue
    else:
        break

value = float(value)

outer_temp = np.linspace(-20,10,4)
layer_temp = np.linspace(-20,15,4)
tb_temp = np.linspace(-20,40,4)
inner_temp = np.linspace(-20,0,4)

outer = ("down jacket", "down coat", "coat", "windbreaker")
layer = ("light down jacket", "thick jumper", "thick cardigan", "cardian")
top = ("thick shirt", "long sleeve t-shirt", "t-shirt", "sleeveless")
bottom = ("thick pants", "jeans", "thick cargo pants", "shorts")
inner_wear = ("thick top and bottom warmer", "top and bottom", "bottom", "top")

if value <= outer_temp[0]:
    print(outer[0])
elif outer_temp[0] < value <= outer_temp[1]:
    print(outer[1])
elif outer_temp[1] < value <= outer_temp[2]:
    print(outer[2])
elif outer_temp[2] < value <= outer_temp[3]:
    print(outer[3])

if value <= layer_temp[0]:
    print(layer[0])
elif layer_temp[0] < value <= layer_temp[1]:
    print(layer[1])
elif layer_temp[1] < value <= layer_temp[2]:
    print(layer[2])
elif layer_temp[2] < value <= layer_temp[3]:
    print(layer[3])

if value <= tb_temp[0]:
    print(top[0])
    print(bottom[0])
elif tb_temp[0] < value <= tb_temp[1]:
    print(top[1])
    print(bottom[1])
elif tb_temp[1] < value <= tb_temp[2]:
    print(top[2])
    print(bottom[2])
elif tb_temp[2] < value <= tb_temp[3]:
    print(top[3])
    print(bottom[3])

if value <= inner_temp[0]:
    print(inner_wear[0])
elif inner_temp[0] < value <= inner_temp[1]:
    print(inner_wear[1])
elif inner_temp[1] < value <= inner_temp[2]:
    print(inner_wear[2])
elif inner_temp[2] < value <= inner_temp[3]:
    print(inner_wear[3])
