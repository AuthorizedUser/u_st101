data1=[1,2,5,10,-20,5,5]

def mode(data):
    frequency = [(i, data.count(data[i])) for i in range(0, len(data))]

    highest = frequency[0]
    for i in range(0, len(frequency)):
        compare = frequency.pop(0)
        if compare[1] >= highest[1]:
            highest = compare

    return data[highest[0]]
# Could shorten this with another list comp but would add complexity



# list1 = [1, 5, 2, 6, 8, 2, 10, 5, 2]
#
# print mode(list1)
