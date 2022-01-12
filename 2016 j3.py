import math
string = input()
length = len(string)
current = length
for i in range(length):
    for j in range(length-current+1):
        test = string[j:j+current]
        # print(test, test[math.ceil(len(test)/2):][::-1], test[:len(test)//2])
        if (test[math.ceil(len(test)/2):][::-1] == test[:len(test)//2]):
            print(len(test))
            quit()
    current -= 1
