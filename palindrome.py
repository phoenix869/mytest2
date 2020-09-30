#!/usr/bin/python
string="yummuy"
count=1
for i in range(0, int(len(string)/2)):
    if string[i] != string[len(string)-i-1]:
        count=-1


if count==1:
    print("palindrome")
else:
    print("Not pallindrome")

