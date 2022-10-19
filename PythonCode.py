from collections import Counter
import re
import string


def printsomething():
    print("Hello from python!")

def PrintMe(v):
    print("You sent me: " + v)
    return 100;

def SquareValue(v):
    return v * v

def WordFrequency(v):
    counter = {}
    for word in v:
        if word not in counter:
            counter[word] = 0
        counter[word] += 1
    print(counter)

def ItemFrequency(v):
    count = 0
    with open("PInput.txt", "r") as fileInput:
        for line in fileInput:
            words = line.split()
            for i in words:
                if(i == v):
                    count += 1
    with open("frequency.dat", "w") as f:
        total = v + " " + str(count)
        f.write(total)

def Histogram():
    with open("frequency.dat", "r") as d:
        for line in d:
            words = line.split(" ")[0]
            numbers = line.split(" ")[1]
            number = int(numbers)
            print (words + " " + ("*" * number))
