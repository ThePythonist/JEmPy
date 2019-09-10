import sys
sys.path.append("..")
import jempy

add = jempy.create_function([["float", "a"],
                             ["float", "b"]],
                            float,
                            "System.out.print(a+b);")


print(add(5, 65))
print(add(3, 4))
