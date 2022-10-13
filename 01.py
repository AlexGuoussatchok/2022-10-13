import timeit

print("List:", timeit.timeit("[1,2,3,4,5,6,7,8,9,10]", number=1_000_000_000))
print("Tuple:", timeit.timeit("(1,2,3,4,5,6,7,8,9,10)", number=1_000_000_000))

