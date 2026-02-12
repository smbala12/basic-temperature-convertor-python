#Temperature convertor (Warning all are approximate values)

convert = input("Choose convert from C to F / C to K / F to C / F to K / K to C / K to F: ")
if convert == "C to C":
    print ("Sorry same conversion")
    exit()
elif convert == "F to F":
    print ("Sorry same conversion")
    exit()
elif convert == "K to K":
    print ("Sorry same conversion")
    exit()
elif convert == "":
    print ("Sorry no value is detected")
    exit()
val = input("Enter a value C/F/K: ")
val_1 = float(val)
if convert == "C to F":
    converted = val_1 * 9 / 5 + 32
    print (f"{round (converted, 2)}\u00B0F")
elif convert == "C to K":
    converted = val_1 + 273.15
    print (f"{round (converted , 2)}\u00B0K")
elif convert  == "F to C":
    converted = (val_1-32)*5/9
    print (f"{round (converted , 2)}\u00B0C")
elif convert == "F to K":
    converted = (val_1-32)*5/9 + 273.15
    print (f"{round (converted , 2)}\u00B0K")
elif convert == "K to C":
    converted = val_1 - 273.15
    print (f"{round (converted , 2)}\u00B0C")
elif convert == "K to F":
    converted = (val_1-273.15)*9/5 + 32
    print (f"{round (converted , 2)}\u00B0F")
else:
    print ("Sorry not valid conversion entered above!")
    exit ()