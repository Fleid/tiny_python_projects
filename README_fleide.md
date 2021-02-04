# Tiny Python Projects

## Meta

Terminal displays:
- Top, **run** :
- Bottom left (alt shift -), **test** : `pytest -v -x test.py` or `make` if there's a Makefile
- Bottom right (alt shift =), **git** : `git add.` `git commit -m ...`, `git push origin master`

## Chapter 0 - Installation

First pip was missing so:

```BASH
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

python3 get-pip.py
python3 -m pip install -U pip
```

Got an error message : ` The scripts pip, pip3 and pip3.8 are installed in '/home/fleide/.local/bin' which is not on PATH`
Which means I need to add that directory to the `PYTHONPATH`.
On Ubuntu (WSL), that's in `~/.bashrc` where you add `export PYTHONPATH="${PYTHONPATH}:/my/other/path"`

Then after forking the repo:

```BASH
git clone https://github.com/Fleid/tiny_python_projects
cd tiny_python_projects
python3 -m pip install -r requirements.txt
```
The requirements installed:
- Code formatters : black, yapf
- Linters : Pylint, flake8
- Type hints : Mypy
- Interactive (notebook) Python : ipython

### NB

```BASH
yapf -i hello.py
bin/new.py HelloWorld.py
```

## Chapter 1 - Write and test a Python program

```BASH
pytest -v -x test.py
```

Add a shush bang (#!) to get the file executable from the shell
Use `which python3` to find which one to link to, then add `#!/usr/bin/python3` to the file
Or default to the env via `#!/usr/bin/env python3` to make it portable
Then run with `./hello.py` (if necessary `chmod +x hello.py`)

Nice to have:
- make with a `Makefile` for testing

### Parameters

Using `argparse`


```PYTHON
import argparse

parser = argparse.ArgumentParser(description='Say Hello')
#parser.add_argument('name', help='Name to greet, positional')
parser.add_argument('-n', '--name', metavar='name', default='World', help='Name to greet, optional')
args = parser.parse_args()
```

### Linting

```BASH

flake 8 hello.py
pylint hello.py

```


## Chapter 2 - Strings

```PYTHON

help(str)

word[n]     # from left, 1 char starting at 0
word[-n]    # from right, 1 char starting at -1

# slicing a string as a list of strings

word[n:p]   # substring()
word[:p]    # left()
word[n:]    # right()

```

## Chapter 3 - Lists

```PYTHON

items = list()
len(items)

items.append('b')
items.append(['c','d']) # ['b', ['c', 'd']]
items.extend(['c','d']) # ['b', 'c', 'd']

items.insert(0, 'a')
items.index('chips')    # returns 0, unsafe - check if there before
                        # slicing applies, and is safe

items.pop()             # removes index -1 (last)
items.pop(0)            # a

items.remove('b')       # removes the first occurence, unsafe - check if there before

items.sort()            # in-place
items.sort(reverse=True)
items.reverse()         #in-place
sorted(items)           # returns a new sorted list
reversed(items)         #returns a new reversed list, lazy, needs to be invoked via list(...)

items_joined = ', '.join(items)        # output a single string with separator

# easier way to generate a list of individual static words
adjectives = """
bankrupt base caterwauling corrupt cullionly detestable dishonest false
filthsome filthy foolish foul gross heedless indistinguishable infected
insatiate irksome lascivious lecherous loathsome lubbery old peevish
rascaly rotten ruinous scurilous scurvy slanderous sodden-witted
thin-faced toad-spotted unmannered vile wall-eyed
""".strip().split()

```

## Chapter 4 - Dictionaries

```PYTHON

answers = dict()
answers = {}

answers = dict(name='Lancelot',quest='Holy Grail')
answers= {'name': 'Lancelot', 'quest': 'Holy Grail'}

answers['name']
answers['age']          # => exception
'age' in answers        # => false
answers.get('age')      # => nothing
answers.get('age',30)   # => 30

answers['key'] = 'value'

len(answers)
answers.keys()
answers.values()

for key in answers.keys():
    print(key, answers[key])

#or

answers.items()
for key, value in answers.items():
    print(key, value)

dict.pop()
dict.update()
#etc

```

## Chapter 5 - Reading/writing files and STDOUT

```PYTHON

import os
os.path.isfile('haha.csv')
os.path.dirname(file)
os.path.basename(file)

os.getcwd()     # Current directory

# Reading

file_handler = open(file)
file_handler.read()     # Empties the file handler
file_handler.seek(0)    # To return to start and be able to read again

if os.path.isfile(file):
    str = open(file).read().rstrip() # Better (plus option to trim right)

# Writing

out_fh = open('new.txt','wt')   # Modes : r/w/append, and text/bytes

# NB : sys.stdout is a file handler!
out_fh = open('new.txt','wt') if flag else sys.stdout

out_fh.write('Some text plus a return feed because else its missing \n')
print('or via print and then no need for the return', file=out_fh)

out_fh.close()

# Reading large files

if os.path.isfile(file):
    text = open(file) # Open but not read

for line in text:
    str = line.upper()

#also
import io
text = io.StringIO(filepath)


```

## Chapter 6 - Reading files and STDIN, f'{}'

```PYTHON

import argparse
import sys

parser.add_argument('file',
                    help='Input file(s)',
                    metavar='FILE',
                    type=argparse.FileType('rt'),
                    default=[sys.stdin], # default to STDIN
                    nargs='*') # 0 or more

#...

print(f'{num_lines:8}{num_words:8}{num_bytes:8} {fh.name}')

```

## Chapter 7 - Parsing text via a dictionary

```PYTHON

dictionary = {}

for line in dictionary_source:
    dictionary[line[0].upper()] = line.rstrip()

#alt
lookup = { line[0].upper() : line.rstrip() for line in dictionary_source}

#from module import function as alias
from pprint import pprint as pp
pp(dictionary)

```

## Chapter 8 - List comprehension, map, lambda

```PYTHON

# Using list comprehension

squares = [num ** 2 for num in range(1,5)]

new_text = [
    vowel if c in 'aeiou' else vowel.upper() if c in 'AEIOU' else c for c in text
]

# Using list comprehension with a function

def new_char(c):
    return vowel if c in 'aeiou' else vowel.upper() if c in 'AEIOU' else c

new_text = ''.join([new_char(c) for c in text])

# Using the map (lazy) function

def new_char(c):
    return vowel if c in 'aeiou' else vowel.upper() if c in 'AEIOU' else c

new_text = ''.join(map(new_char,text))


# Using the map (lazy) function with anonymous function (lambda)

new_text = ''.join(
    map (
        lambda c: vowel if c in 'aeiou' else vowel.upper() if c in 'AEIOU' else c
        ,text
    )
)

# Using Regex

import re
pattern = '[aeiou]'
vowel = 'o'
new_text = re.sub(pattern, vowel, text)
new_text = re.sub(pattern.upper(), vowel.upper(), new_text)

```

## Chapter 9 - Random, Generating arg errors

```PYTHON

import random
random.seed(args.seed)

adjectives = """
bankrupt base caterwauling corrupt cullionly detestable dishonest false
filthsome filthy foolish foul gross heedless
""".strip().split()

random.choice(adjectives)   # single value
random.sample(adjectives,3) # multiple value, non repeating
random.choices(adjectives,3) # multiple value, repeating

```

```PYTHON

    parser.add_argument('-n',
                        '--number',
                        help='Number of insults',
                        metavar='insults',
                        type=int,
                        default=3)

    args = parser.parse_args()

    if args.number < 1:
        parser.error(f'--number "{args.number}" must be > 0')

    return parser.parse_args()

```
