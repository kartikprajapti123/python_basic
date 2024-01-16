import random

# random number from 0 to 1
print(random.random())
# Output 0.16123124494385477

# random number from 10 to 20
print(random.randint(10, 20))
# Output 18

# random number from 10 to 20 with step 2
print(random.randrange(10, 20, 2))
# Output 14

# random float number within a range
print(random.uniform(5.5, 25.5))
# Output 5.86390810771935

# random choice from sequence
print(random.choice([10, 20, 30, 40, 50]))
# Output 30

# random sample from sequence
print(random.sample([10, 20, 30, 40, 50], k=3))
# Output [50, 10, 20]

# random sample without replacement
print(random.choices([10, 20, 30, 40, 50], k=3))
# Output [30, 10, 40]

# random shuffle
x = [10, 20, 30, 40, 50, 60]
random.shuffle(x)
print(x)
# [60, 10, 30, 20, 50, 40]

# random seed
random.seed(2)
print(random.randint(10, 20))
# 10
random.seed(2)
print(random.randint(10, 20))
# 10
import uuid

# get a random UUID
safeId = uuid.uuid4()
print("safe unique id is ", safeId)