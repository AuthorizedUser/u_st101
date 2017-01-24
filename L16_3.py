data1=[1,2,5,10,-20]

def median(data):
    data.sort()
    return data[(len(data) / 2)]

#test appears broken.... Here is true way to calculate value
# print "Value | Median Index"
# testlist = [2, 5, 8, 9, 10, 11, 13]
# for value in testlist:
#     print "{:2} | {:2}".format(value, (value / 2) + (value % 2) - 1)
