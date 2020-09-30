import re

character_1 = "Dorothy"
character_2 = "Henry"

regular_expression = re.compile("[A-Za-z]{7}")

result_1 = regular_expression.match(character_1)

match_1 = result_1.group(0)

result_2 = re.match("[A-Za-z]{7}", character_2)
print(result_2)

# import L. Frank Baum's The Wonderful Wizard of Oz
oz_text = open("the_wizard_of_oz_text.txt",encoding='utf-8').read().lower()

found_wizard = re.search("wizard", oz_text)

all_lions = re.findall("lion", oz_text)

number_lions = len(all_lions)
print(number_lions)
