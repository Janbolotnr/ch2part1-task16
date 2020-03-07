earth_weight = 68
moon_index = 0.165
moon_weight_2020 = earth_weight * moon_index
print('Your weight 2020 year: ' + str(moon_weight_2020))

for i in range(1, 16):
    print(i, round(earth_weight * moon_index, 2))
    earth_weight += 1


#num = int(input("Your weight: "))
#sum = (num * 0.165) * 15 
#print(sum)

#nada proverit'