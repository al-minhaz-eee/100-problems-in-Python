import math

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)
def nearest_neighbor(neighbors, point):
    nearest = None
    min_distance = float('inf')

    for neighbor in neighbors:
        distance = euclidean_distance(neighbor, point)
        if distance < min_distance:
            min_distance = distance
            nearest = neighbor
    return nearest, min_distance

neighbors = [(1, 2), (3, 4), (5, 5), (6, 1), (7, 3)]
point = (4, 3)

nearest, distance = nearest_neighbor(neighbors, point)
print(f"Nearest neighbor to {point} is {nearest} with a distance of {distance:.2f}")