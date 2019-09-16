# JEmPy
A Python library which allows you to execute Java code from within a Python script. When run for the first time, the library will automatically compile the Java code and store it locally. On future uses, the compiled code will be detected and used automatically.

## Usage
Move "jempy.py" into your Python installation's "Lib" directory.
An example usage is if you wanted to create a Java function which took two floats as inputs, and returned their sum as a float, you would do so like this:
```
import jempy

add = jempy.create_function([["float", "a"],
                             ["float", "b"],
                             float,
                             "System.out.println(a+b);")

print(add(3, 4))
```
```
7
```
