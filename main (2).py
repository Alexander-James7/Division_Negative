# Created by: Alexander James with help by Owen Whalley
# Created on: 2022/10/12

# This code divides 2 negative numbers with the use of repeated subtraction
x = int(input("What is your first number: "))
y = int(input("What is your second number: "))

count = 0
# This line converts the negative numbers to postive with repeated subtraction, in order to more easily divide.
if x < 0 and y < 0:
  x2 = x -x -x 
  y2 = y - y - y

elif x < 0 and y > 0:
  x2 = x - x - x
  y2 = y
else:
  x2 = x
  y2 = y

while x2 > 0:
  x2 -= y2
  count += 1

if x2 < 0:
  for z in range(1):
    x2 += y2
    count += 1

if x < 0 and y > 0 or x > 0 and y < 0:
  count = count - count - count
print("Your quotient is: "+str(count))
print("And the remainder is "+str(x2))