# 1
def max_num(num1, num2, num3):
    return max(num1, num2, num3)

print(max_num(80, 7, 4))
print(max_num(65, 13, 6))
print(max_num(100, 23, 8))

# 2
def mult_list(list):
    result = 1
    for num in list:
        result = result * num
    return result

print(mult_list([4, 6, 3, 9]))

#3
def rev_string(String):
    return String[::-1]

print(rev_string("Hello world"))


# 4
def num_within(num, start_num, start_end):
    if num in range(start_num, start_end + 1):
        return True
    else:
        return False 
print(num_within(4, 3, 2))
print(num_within(5, 2, 5))
print(num_within(11, 3, 6))

#5
triangle = [[1],[1,1]]
def pascal(n):
  
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      length = len(row_prev)+1
      for i in range(length):
        if i == 0:
          row.append(1)
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1
    for row in triangle:
      print(row)


pascal(5)