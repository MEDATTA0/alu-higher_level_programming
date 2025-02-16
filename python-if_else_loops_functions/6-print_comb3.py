#!/usr/bin/python3

for i in range(100):
    if i == 89:
        print("89")
    elif int(str(i).zfill(2)) < int(str(i).zfill(2)[::-1]):
        print("{:02}".format(i), end=", ")
