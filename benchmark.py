# run cli command
# time python benchmark.py

from FizzBuzz.fizzBuzz import fizzBuzz

for i in range(1, 8000):
    for j in range(1, 10000):
        fizzBuzz(j)

