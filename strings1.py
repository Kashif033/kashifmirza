#
# #with_tax=price*1.89
#print(price,with_tax)
#7.5 8.175
#print("base price: $(:,2f).with tax: ${:.2f}".format(price,with_tax))
def to_celcius(x):
    return (x-32)*5/9
for x in range(0,101,10):
print("{:>3} F | {:>6.2f} C".format(x, to_celcius(x)))