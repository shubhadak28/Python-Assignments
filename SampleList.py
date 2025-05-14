'''
10. Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
11. Expected Output : ['Green', 'White', 'Black']

'''

color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

color = [x for (i, x) in enumerate(color) if i not in (0, 4, 5)]

print(color)

