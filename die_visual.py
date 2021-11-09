from die import Die

# create a 6 sides die
die = Die()

# roll dice and store the results
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# analyse the result
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)
