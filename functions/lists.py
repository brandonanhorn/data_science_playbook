
"""
1) Create a function named reversed_list() that takes two lists of
the same size as parameters named lst1 and lst2.

The function should return True if lst1 is the same as lst2 reversed.
The function should return False otherwise.
"""
## Answer
def reversed_list(lst1, lst2):
  for index in range(len(lst1)):
    if lst1[index] != lst2[len(lst2) - 1 - index]:
      return False
  return True
## Proof it works
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))

"""
2) Create a function named divisible_by_ten() that takes a list of
numbers named nums as a parameter.

Return the count of how many numbers in the list are divisible by 10.
"""
## Answer
def divisible_by_ten(nums):
  count = 0
  for number in nums:
    if (number % 10 == 0):
      count += 1
  return count
#Proof
print(divisible_by_ten([20, 25, 30, 35, 40]))

"""
3) Create a function named add_greetings() which takes a list
of strings named names as a parameter.

In the function, create an empty list that will contain each greeting.
Add the string "Hello, " in front of each name in names and
append the greeting to the list.

Return the new list containing the greetings.
"""
## Answer
def add_greetings(names):
  fuckgoof = []
  for name in names:
    fuckgoof.append("Hello, " + name)
  return fuckgoof
# Proof
print(add_greetings(["Owen", "Max", "Sophie"]))

"""
4) Write a function called delete_starting_evens() that
has a parameter named lst.

The function should remove elements from the front of lst until
the front of the list is not even. The function should then return lst.

For example if lst started as [4, 8, 10, 11, 12, 15],
then delete_starting_evens(lst) should return [11, 12, 15].

Make sure your function works even if every element in the list is even!
"""
# Answer
def delete_starting_evens(lst):
  while (len(lst) > 0 and lst[0] % 2 == 0):
    lst = lst[1:]
  return lst
# Proof
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

"""
5) Create a function named odd_indices() that has one parameter named lst.

The function should create a new empty list and add every element
from lst that has an odd index. The function should then return this new list.

For example, odd_indices([4, 3, 7, 10, 11, -2])
should return the list [3, 10, -2].
"""
# Answer
def odd_indices(lst):
  empty = []
  for i in range(1, len(lst), 2):
    empty.append(lst[i])
  return empty
# Proof
print(odd_indices([4, 3, 7, 10, 11, -2]))

"""
6) Create a function named exponents() that takes two lists
as parameters named bases and powers. Return a new list containing
every number in bases raised to every number in powers.
"""
# Answer
def exponents(bases, powers):
  new_lst = []
  for base in bases:
    for power in powers:
      new_lst.append(base ** power)
  return new_lst
# Proof
print(exponents([2, 3, 4], [2, 4, 6]))

"""
7) Create a function named larger_sum() that takes
two lists of numbers as parameters named lst1 and lst2.

The function should return the list whose elements sum
to the greater number. If the sum of the elements of each list are equal,
return lst1.
"""
# Answer
def larger_sum(lst1, lst2):
  sum1 = 0
  sum2 = 0
  for number in lst1:
    sum1 += number
  for number in lst2:
    sum2 += number
  if sum1 >= sum2:
    return lst1
  else:
    return lst2
# Proof
print(larger_sum([1, 9, 5], [2, 3, 7]))

"""
8) Create a function named over_nine_thousand() that takes a
list of numbers named lst as a parameter.

The function should sum the elements of the list until
the sum is greater than 9000. When this happens, the function
should return the sum. If the sum of all of the elements is
never greater than 9000, the function should return total sum
 of all the elements. If the list is empty, the function should return 0.

For example, if lst was [8000, 900, 120, 5000],
then the function should return 9020.
"""
# Answer
def over_nine_thousand(lst):
  sum = 0
  for number in lst:
    sum += number
    if (sum > 9000):
      break
  return sum
# Proof
print(over_nine_thousand([8000, 900, 120, 5000]))

"""
9) Create a function named max_num() that takes a list of
numbers named nums as a parameter.

The function should return the largest number in nums
"""
# Answer
def max_num(nums):
  maximum = nums[0]
  for number in nums:
    if number > maximum:
      maximum = number
  return maximum
# Proof
print(max_num([50, -10, 0, 75, 20]))

"""
10) Write a function named same_values() that takes
two lists of numbers of equal size as parameters.

The function should return a list of the indices where the
values were equal in lst1 and lst2.
"""
# Answer
def same_values(lst1, lst2):
  new_lst = []
  for index in range(len(lst1)):
    if lst1[index] == lst2[index]:
      new_lst.append(index)
  return new_lst
# Proof
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {letters:points for letters,points in zip(letters,points)}

letter_to_points[" "] = 0

def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letter_to_points[letter]
  return point_total

score_word("BROWNIE")
