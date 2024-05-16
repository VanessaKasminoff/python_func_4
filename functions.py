'''
1. Write a Python function called max_num()to find the maximum of three numbers.

2. Write a Python function called mult_list() to multiply all the numbers in a list.

3. Write a Python function called rev_string() to reverse a string.

4. Write a Python function called num_within() to check whether a number falls in a given range.
The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.

'''
# Question 1:

def max_num(a, b, c):
    print(max([a, b, c]))

# max_num(1, 2, 3, 4)

# Question 2:

def mult_list(lst):
  #if empty list, return 0
  if len(lst) == 0:
    return 0
  #product starts with first element of list
  prod = lst[0]

  #go through list elements and multiply them together
  if len(lst) > 1:
    for i in lst[1:]:
      prod = prod * i

  return prod
    
# print(mult_list([1,2,3]))
# print(mult_list([]))
# print(mult_list([15]))

# Question 3:

def rev_string(my_str):
  return my_str[::-1]

# print(rev_string(""))
# print(rev_string("apple"))
# print(rev_string("mt string"))

# Question 4:

def num_within(x,a,b):
  return x in range(a, b + 1)
     
# print(num_within(3,2,4))     
# print(num_within(3,1,3))     
# print(num_within(10,2,5))


'''

5. Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
The function accepts the number n, the number of rows to print
Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together.

'''

triangle = [[1],[1,1]]
def pascal(n):
  #base case
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    #fill up correct number of rows in triangle
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      #create correct row, then add to triangle (this row will be 1 longer than row before it)
      length = len(row_prev)+1
      for i in range(length):
        #first number is 1
        if i == 0:
          row.append(1)
        #intermediate nunmbers get added from previous rows
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        #last number is 1
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    #print triangle
    for row in triangle:
      print(row)

pascal(2)
pascal(5)