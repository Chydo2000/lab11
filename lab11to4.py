# Declare empty list 
points = []

# Input from user & append the list
for i in range(5):
    score = int(input("Give points:"))
    points.append(score)

# Find the biggest and the smallest number

smallest = points[0]
biggest = points [0]

for i in points:
    if i < smallest:
        smallest = i
    if i > biggest:
        biggest = i

# Remove smallest and biggest from the list

points.remove(smallest)
points.remove(biggest)
