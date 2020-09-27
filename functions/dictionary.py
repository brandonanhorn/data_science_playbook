"""
1) Create a function named count_first_letter that takes a dictionary
named names as a parameter. names should be a dictionary where the
key is a last name and the value is a list of first names.
For example, the dictionary might look like this:
"""
def count_first_letter(names):
  letters = {}
  for key in names:
    first_letter = key[0]
    if first_letter not in letters:
      letters[first_letter] = 0
    letters[first_letter] += len(names[key])
  return letters

print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}

"""
2) Create a function named unique_values that takes a
dictionary named my_dictionary as a parameter.
The function should return the number of unique values in the dictionary.
"""
def unique_values(my_dictionary):
  seen_values = []
  for value in my_dictionary.values():
    if value not in seen_values:
      seen_values.append(value)
  return len(seen_values)

print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2
print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 1

"""
3) Write a function named frequency_dictionary that takes a
list of elements named words as a parameter.
The function should return a dictionary containing the
frequency of each element in words.
"""
def frequency_dictionary(words):
  freqs = {}
  for word in words:
    if word not in freqs:
    	freqs[word] = 0
    freqs[word] += 1
  return freqs

print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}

"""
4) Write a function named word_length_dictionary that takes
a list of strings named words as a parameter.
The function should return a dictionary of key/value pairs
where every key is a word in words and every value is the length of that word.
"""
def word_length_dictionary(words):
  word_lengths = {}
  for word in words:
    word_lengths[word] = len(word)
  return word_lengths

print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}

"""
5) Write a function named max_key that takes a dictionary named
my_dictionary as a parameter. The function should return the
key associated with the largest value in the dictionary.
"""
def max_key(my_dictionary):
  largest_key = float("-inf")
  largest_value = float("-inf")
  for key, value in my_dictionary.items():
    if value > largest_value:
      largest_value = value
      largest_key = key
  return largest_key

print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"

"""
6) Create a function named values_that_are_keys that takes a
dictionary named my_dictionary as a parameter. This function should
return a list of all values in the dictionary that are also keys.
"""
def values_that_are_keys(my_dictionary):
  value_keys = []
  for value in my_dictionary.values():
    if value in my_dictionary:
      value_keys.append(value)
  return value_keys

print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# should print [1, 4]
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# should print ["a"]

"""
7) Create a function named add_ten that takes a dictionary with
integer values named my_dictionary as a parameter. The function should
add 10 to every value in my_dictionary and return my_dictionary
"""
def add_ten(my_dictionary):
  for key in my_dictionary.keys():
    my_dictionary[key] += 10
  return my_dictionary

print(add_ten({1:5, 2:2, 3:3}))
# should print {1:15, 2:12, 3:13}
print(add_ten({10:1, 100:2, 1000:3}))
# should print {10:11, 100:12, 1000:13}

"""
8) Create a function called sum_even_keys that takes a dictionary named
my_dictionary, with all integer keys and values, as a parameter.
This function should return the sum of the values of all even keys.
"""
def sum_even_keys(my_dictionary):
  total = 0
  for key in my_dictionary.keys():
    if key%2 == 0:
      total += my_dictionary[key]
  return total

print(sum_even_keys({1:5, 2:2, 3:3}))
# should print 2
print(sum_even_keys({10:1, 100:2, 1000:3}))
# should print 6

"""
9) Write a function named sum_values that takes a dictionary named
my_dictionary as a parameter. The function should return the sum of the
values of the dictionary
"""
def sum_values(my_dictionary):
  something = 0
  for i in my_dictionary.values():
    something += i
  return something

print(sum_values({"milk":5, "eggs":2, "flour": 3}))
# should print 10
print(sum_values({10:1, 100:2, 1000:3}))
# should print 6
