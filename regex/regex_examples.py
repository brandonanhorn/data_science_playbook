import re

zip_code = '90210'
match = re.search('[0-9]{5}', zip_code)
print(match.group(0))

zip_code = '90210-1234'
match = re.search('[0-9]{5}-[0-9]{4}', zip_code)
print(match.group(0))

zip_code = '90210+1234'
match = re.search('[0-9]{5}\+[0-9]{4}', zip_code)
print(match.group(0))

foo = '\t baz'
print(foo)
bar = r'\t baz'
print(bar)

shrug = '¯\_(ツ)_/¯'
match = re.search('¯\\\\_', shrug)
print(match.group(0))
match = re.search(r'¯\\_', shrug) # raw string notation
print(match.group(0))

# (\1) is a "backreference"
haha = 'haha!!!!!!'
match = re.search(r'([a-z]+)(\1)(!*)', haha)
print(match.group())
print(match.group(0))
print(match.groups())
print(match.group(1))
print(match.group(2))
print(match.group(3))

# long string
long_string = """
I said a hop,
The hippie, the hippie,
To the hip, hip hop, and you don't stop, a rock it
To the bang bang boogie, say, up jump the boogie,
To the rhythm of the boogie, the beat.
"""

match = re.search('hip(p?)', long_string)
print(match.groups()) # Shows what is matched in groups
print(match.group(0)) # Shows entire match
print(match.group(1)) # Group #1

matches = re.finditer('hip(p?)', long_string)
for element in matches:
    print(element.group(0))

# Findall
match = re.findall('h[io]p', long_string)
print(match)

match = re.findall('hello [a-z]+', 'hello world')
print(match)

# raw notation
match = re.findall('\\blo', 'hello lollipop world')
print(match)
match = re.findall(r'\blo', 'hello lollipop world')
print(match)

# sub
result = re.sub('[a-f]', '*', 'hello world')
print(result)

# Multiline
match = re.search('^C', 'A\nB\nC', re.MULTILINE)
print(match.group(0))

match = re.findall('^C', 'A\nB\nC', re.MULTILINE)
print(match)
