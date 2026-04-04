# sum array of element and stop when it found STOP
#Input
# calculateSumUntilStop(['1','2','3',"STOP",'4'])
# calculateSumUntilStop(['1','2','3',"STOP",'4'])


def calculateSumUntilStop(mylist):
    sum = 0
    for i in mylist:
        if i == "STOP":
            break
        sum += int(i)
    return sum

add = calculateSumUntilStop(['1','2','3',"STOP",'4'])
print(add)
