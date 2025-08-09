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
