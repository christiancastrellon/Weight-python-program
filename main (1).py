# FIXME (1): Prompt for four weights. Add all weights to a list. Output list.
people_weights =[]
num_weights = 4
for i in range(num_weights):
    single_weight = float(input(f'Enter weight {i+1}:\n'))
    people_weights.append(single_weight)

print(f'Weights: {people_weights}')

# FIXME (2): Output average of weights.
avg_weight = sum(people_weights) / len(people_weights)
print(f'\nAverage weight: {avg_weight:.2f}')

# FIXME (3): Output max weight from list.
print(f'Max weight: {max(people_weights):.2f}')

# FIXME (4): Prompt the user for a list index and output that weight in pounds and kilograms.
index = int(input('\nEnter a list location (1 - 4):\n'))
chosen_weight = people_weights[index-1]
print(f'Weight in pounds: {chosen_weight:.2f}')
print(f'Weight in kilograms: {chosen_weight/2.2:.2f}')

# FIXME (5): Sort the list and output it.
people_weights.sort()
print(f'\nSorted list: {people_weights}')