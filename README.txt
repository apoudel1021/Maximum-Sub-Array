Documentation on Implementation of linear time maximum subarray algorithm

This program has been written using Python language in Spyder (IDE)
It aims to calculate the largest sum of the sub array in the array. 
Firslty, when the program is run, it prompts the user to enter the number of elements that you want in the array 

Ex: 

How many elements do you want in an array?

Secondly, it prompts the user to enter the numbers in the array, accepting both the positive and negative values.

To perform the subarray problem in linear time complexity i.e. 0(n), I have used Kandane's Algorithm

The pseudo code for the implementation of Kandane's Algorithm, which I have followed in my code is:

Initialize:
    max_so_far = 0
    max_ending_here = 0

Loop for each element of the array
  (a) max_ending_here = max_ending_here + a[i]
  (b) if(max_ending_here < 0)
            max_ending_here = 0
  (c) if(max_so_far < max_ending_here)
            max_so_far = max_ending_here
return max_so_far
 
Source: https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/

For the following example, where user selects to have the array of size 9 

and enters the number as: [-2, 1, -3, 4, -1, 2, 1, -5,4]

the program shall display the output as: [4,-1,-2,1]  with the maximum sum of 6

