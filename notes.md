# Python course

## Section 1

### Virtual environment

for Windows python -m venv .venv
It will create a whole new python environment for you. To activate the environment type
`     source .venv\Scripts\activate
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

Lists: - In python world we call it list in other langs we call it array. it's mutable.
Sets: - A set is an unordered collection of unique elements. It's mutable.
`python
      my_set = {1, 2, 3, 4}
      my_set.add(5)
      `

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

## Conditionals

- we use pass keyword just to pass the control like continue keyword it says don't do anything just move to the next step.

- if
- elif
- else

## Loops:

- enumerate(iterable) - it return the index also
- zip(inter1, iter2) - it return the index and value of each list, first list element is index and second list vlaue type. i mean in short it return the touple of the two list.
- break - it break the whole loop, means the execution loop stops after the break keyword.

- for else loop

```python
for age,name in voters:
    if age >= 18:
        print(f"{name} is eligble for vote")
else:
    print("we entered into the else block of loop")
```
in this code else code will only execute if the loop didn't  break, if loops finished normally without any break the else part will run, continue does not effect the elese.


## Functions 

- Every variable is function scoped
- nonlocal: nonlocal is keyword in python which  is used to refer the context of the varible which is outside the function scope. (inner function to outer function). it works function to function.


- *args: 
    When passing the args all the arugment passed without the keyword become args. At the function defination it's just the touple. 

- *kwargs: 
    when calling function all the keyword arguments  become kwargs.  It's dictonary of key value pairs.
- if return nothing from a function it return None.

- Types of function
    - pure vs impure function      : pure function only manupulate data within itself not form global scope recommanded. impure is opposite. 
    - recursive function           : the function which call itself
    - lambdas (anonymous) function : function without name, anonymous function

- Imports
    - Named import

        from recipe.flavors import demo_chai, ginger_chai # named import
        print(ginger_chai())
        print(demo_chai())
    
    - All import

        import recipe.flavors  # all import
        print(recipe.flavors.demo_chai())
        print(recipe.flavors.ginger_chai())

-  __init__.py
    - This file convert the normal python folder into the python module/package. In python 3.3 we don't need it actully.

## Comprehensions 

- Comprehensions is mainly used for their readibility and easiness of using.

- Comprehension is followed by expression then for loop and then other code.

- list comprehension
```python
    l = [item for item in menu if "lemon" in item]
```

- set comprehension
```python
    unique_spices = {spice for ingradients in recipes.values() for spice in ingradients}

```

- dictonary comprehension
```python
    tea_prices_usd = {tea:price*80 for tea, price in tea_prices_inr.items() }

```
- generator comprehension

    generator comprehensions are used to save memory since it doesn't create data/list in memory it gives the object of generator which gives the data one by one
```python
 generator_comprehension = (sale for sale in sales if sale > 10)
    

```

## Generators

- generators is also a one type of function in which we use the `yield` keyword and it used to save memory.
- we use it when we don't want the result immedietely, lazy evalution. 

```python
def serve_chai():
    yield "chai 1"
    yield "chai 2"


one = serve_chai()
```
- in this one is keeping the reference of the whole function (serve_chai) and when we loop over one it uses that memory to print the data.
```
print(next(one)) # prints the next value form the iterator. The function resume where it is left 

``` 
## Decorators

- decorator is a function that takes another function as an argument, adds some functionality, and then returns a new function (or a modified version of the original). 

## Oops

* changing in the object value doesn't effect the class value and other object value
* Attribute shadowing means if the attribute's fallback value exist in the class defination after deleation the attribute will have that value, if not then error.
* self keyword in oops in python used to refer the current object of class and with . operator on self we can access the all the property and methods of a class.

* So if you put () brackters in front of the class and write the name of the parent class it's called inheritence.
* But instead of that you assign a variable the reference of the class it's called compositon.
```python
# Composition

class BaseChai:
    # code
class ChildClass:
    chai = BaseChai # comppositon
```

* Every class has constructor if you don't create it. python automatically creates it at the time of execution.

* Accessing base class can be done with 3 methods #see file base_class.py
- Code Duplication
- Explicit call
- super method

* static methods doesn't require static methods they can be callled with class and without object.
