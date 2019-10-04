# -*- coding: utf-8 -*-
"""
Created on Thu Oct 03 18:35:52 2019

@author: deadp
"""

num = int(raw_input("How many elements do you want in an array: "))
array = []

def seta(number):
    for i in range(0,number):
        try:
            val= int(raw_input("Enter the numbers into the array: "))
            array.append(val)
        except:
            print("Please enter the numerical int value/ accepts both + or -")
        number= number+1
    print "The array that you have entered is: "
    print array 

# linear time subarray problem can be solved using Kandane's algorithm 
def Kandanealg(number,a):
#    print a
#    print number
    start=0
    end = 0
    begin = 0
    i=0
    max_sofar=0
    max_endinghere =  0
    while i < number:
        max_endinghere = max_endinghere + a[i]
        if max_endinghere<0:
            max_endinghere=0
            begin = i +1
#            print begin
#            print "******************"
        if max_endinghere>0:
#            start = i
#            print start
#            print "+++++++++++++++++++"
            if max_sofar<max_endinghere:
                start = begin
                end=i
#                print end
                max_sofar=max_endinghere
               
        i+=1
    print "The sum of the maximum sub array is: "
    print max_sofar
    b=[]
    for j in range(start ,end+1):
#        print end 
##        print "****"
#        print start  
#        print a[start]
        b.append(a[j])
    print "The sub array with the largest sum is: "
    print b
    
#    return max_sofar
 
seta(num)
Kandanealg(num,array)
