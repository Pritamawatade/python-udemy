# Python course

## Section 1

### Virtual environment

for Windows python -m venv .venv
It will create a whole new python environment for you. To activate the environment type
`      source .venv\Scripts\activate
     `

      To deactivate the environment type
      ```
      deactivate
      ```

      To install a package in the environment type
      ```
      pip install flask
      ```
      To install packages with the requirements file type
      ```
      pip install -r requirements.txt
      ```

### How to orginize python code

      /root
      | run.py // main file
      | chai.py // module
      /utils
         | __init__.py // init file

## Section 2 - Data types

- Everything in python is object.
- Every object has type, identity, and value.
- mutable means you can change the value (identity).
- immutable means you can't change the value (identity).
- In the world of immutable what change is reference. variable points to the new memore location(reference).

Lists:
      - In python world we call it list in other langs we call it array.  it's mutable.
      Sets:
      - A set is an unordered collection of unique elements. It's mutable.
      ```python
      my_set = {1, 2, 3, 4}
      my_set.add(5)
      ```

      Tuples:
      - A tuple is an ordered, immutable collection of elements.
      ```python
      my_tuple = (1, 2, 3)
      ```

      Dictionaries:
      - A dictionary is a mutable collection of key-value pairs.
      ```python
      my_dict = {'name': 'Alice', 'age': 25}
      my_dict['city'] = 'New York'
      ```

      Collections (from `collections` module):
      - The `collections` module provides specialized container datatypes like `namedtuple`, `deque`, `Counter`, etc.
      ```python
      from collections import namedtuple, deque, Counter

      Point = namedtuple('Point', ['x', 'y'])
      p = Point(1, 2)

      d = deque([1, 2, 3])
      d.append(4)

      c = Counter(['a', 'b', 'a', 'c', 'b', 'a'])
      ```
