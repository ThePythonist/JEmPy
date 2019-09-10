import sys
sys.path.append("..")
import jempy
import time

sqrt = jempy.create_function([["float", "x"]],
                             float,
                             "System.out.print(Math.sqrt(x));",
                             imports=["java.lang.Math"])

milSqrt = jempy.create_function([],
                                str,
                                """
for (int i=0; i<10000000; i++) {
    Math.sqrt(i);
}""",
                                imports=["java.lang.Math"])

startTime = time.time()
for i in range(10000000):
    i ** 0.5
endTime = time.time()
pythonTime = endTime-startTime
print(pythonTime)

startTime = time.time()
milSqrt()
endTime = time.time()
javaTime = endTime-startTime
print(javaTime)
