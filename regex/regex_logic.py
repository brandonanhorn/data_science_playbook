import re

#phone numbers
[\d\(][\d\s]\d[\d\.\-][\d\)][\s\d]\d[\d\.\-]\d[\s\d]\d{0,4}


#1) Regular expressions are special sequences of characters that describe a pattern of text that is to be matched

#2) We can use literals to match the exact characters that we desire

#3) Alternation, using the pipe symbol |, allows us to match the text preceding or following the |

#4) Character sets, denoted by a pair of brackets [], let us match one character from a series of characters

#5) Wildcards, represented by the period or dot ., will match any single character (letter, number, symbol or whitespace)

#6) Ranges allow us to specify a range of characters in which we can make a match

#7) Shorthand character classes like \w, \d and \s represent the ranges representing word characters, digit characters, and whitespace characters, respectively

#8) Groupings, denoted with parentheses (), group parts of a regular expression together, and allows us to limit alternation to part of a regex

#9) Fixed quantifiers, represented with curly braces {}, let us indicate the exact quantity or a range of quantity of a character we wish to match

#10) Optional quantifiers, indicated by the question mark ?, allow us to indicate a character in a regex is optional, or can appear either 0 times or 1 time

#11) The Kleene star, denoted with the asterisk *, is a quantifier that matches the preceding character 0 or more times

#12) The Kleene plus, denoted by the plus +, matches the preceding character 1 or more times

#13) The anchor symbols hat ^ and dollar sign $ are used to match text at the start and end of a string, respectively
