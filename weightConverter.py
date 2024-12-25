
convert = 0.0
weight = input( "Input your weight: ")
metric = input("is the weight in (K)g or (L)bs: ")

#convert from string to float so could convert
float_num = float(weight)

if metric == 'K' :
    convert = float_num * 2.2
    print(f"{convert} pounds(lbs)")
elif metric == 'L':
    convert = float_num / 2.2
    print(f"{convert} Kilograms(Kgs)")
else:
    print("invalid choice")
