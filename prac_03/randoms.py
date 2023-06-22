import random

print(random.randint(5, 20))  # line 1\
# 5, 10, 14, 15
# smallest possible 5, largest 20
print(random.randrange(3, 10, 2))  # line 2
# 9, 7, 7, 3
# smallest possible 3, largest 9
# could not have produced a 4 as it started at 3 and had a step of 2, thus selecting only odd numbers
print(random.uniform(2.5, 5.5))  # line 3
# 3.7767027433510503, 3.037769328100832, 2.9586757318063595, 3.094841473951352
# smallest possible 2.5, 5.4999999999999999

print(random.randint(1, 100))
