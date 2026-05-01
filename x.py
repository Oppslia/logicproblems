class Point():
    def __init__(self, x, y ,z):
        self.x = x
        self.y = y
        self.z = z
        self.connected = False
        self.closestPoint = None
        self.belongsToCircuit = False
        # import os
        # self.id = os.urandom()
    def findClosestPoint(self, points:list):
        smallestDistance = float('inf')
        closestCoord = None
        for point in points:
            distance = (((self.x - point.x) ** 2) + ((self.y - point.y) ** 2) + ((self.z - point.z) ** 2)) ** 0.5
            if distance > 0 and distance < smallestDistance:
                closestCoord = point
                smallestDistance = distance
        self.closestPoint = closestCoord
        self.distanceToClosestPoint = smallestDistance
        return self

def tablePrint(circuits):
    # Header for the table
    print(f"{'GRP':<4} | {'IDX':<4} | {'ORIGIN (c1)':<20} | {'NEAREST (c2)':<20} | {'DISTANCE'}")
    print("—" * 85)

    # Outer loop: Iterates through each sub-list (circuit)
    for group_idx, points_list in enumerate(circuits):
        
        # Inner loop: Iterates through each Point object in that sub-list
        for point_idx, p in enumerate(points_list):
            c1 = f"({p.x},{p.y},{p.z})"

            if p.closestPoint:
                q = p.closestPoint
                c2 = f"({q.x},{q.y},{q.z})"
                dist_str = f"{p.distanceToClosestPoint:,.2f}"
            else:
                c2 = "None"
                dist_str = "N/A"

            # Added GRP (Group Index) so you know which sub-list the point belongs to
            print(f"{group_idx:<4} | {point_idx:<4} | {c1:<20} | {c2:<20} | {dist_str}")
        
        # Optional: Print a small separator between groups for readability
        if len(points_list) > 0:
            print("-" * 85)

# Example usage:
# tablePrint(circuits)
with open("Advent2025Resources/day_8_input.txt") as file:
    lines = file.readlines()
    points:list[Point] = []
    for line in lines:
        x, y, z = map(int, (c.strip('\n') for c in line.split(',')))
        points.append(Point(x = x, y = y, z = z))
    sortedPoints = [point.findClosestPoint(points) for point in points]
    sortedPoints.sort(key=lambda c: c.distanceToClosestPoint)
    circuits = [[c] for c in sortedPoints]
    circuits[0].append(circuits[0][0].closestPoint)
    circuits[0][0].belongsToCircuit = circuits[0][1].belongsToCircuit = True
    connections_made = 0
    for index, point in enumerate(sortedPoints):
        if connections_made >= 1000: 
            break # Puzzle says connect 1000 pairs
        pointCircuitIndex = [i for i in range(len(circuits)) if point in [p for p in circuits[i]]][0]
        closestPointCircuitIndex = [i for i in range(len(circuits)) if point.closestPoint in [p for p in circuits[i]]][0]

        if point.closestPoint.belongsToCircuit: # Closest Point belongs to a circuit
            if point.belongsToCircuit: # Point also belongs to a circuit
                if pointCircuitIndex != closestPointCircuitIndex: # The circuits they belong to are not the same, merge them
                    circuits[pointCircuitIndex].extend(circuits[closestPointCircuitIndex])
                    circuits[closestPointCircuitIndex].clear()
                    connections_made += 1
                    continue
                else: # They belong to the same circuit, do nothing
                    continue
            else: # Point doesn't belong to a circuit, but the closest point does
                circuits[closestPointCircuitIndex].append(point)
                circuits[pointCircuitIndex].clear()
                point.belongsToCircuit = True
                connections_made += 1
                continue
        if point.belongsToCircuit: # Point belongs to a circuit, but it's closest point does not.
            circuits[pointCircuitIndex].append(point.closestPoint)
            circuits[closestPointCircuitIndex].clear()
            point.closestPoint.belongsToCircuit = True
            connections_made += 1
            continue
        
        else: # Neither belong to a circuit.
            circuits[pointCircuitIndex].extend(circuits[closestPointCircuitIndex])
            circuits[closestPointCircuitIndex].clear()
            point.belongsToCircuit = True
            point.closestPoint.belongsToCircuit = True
            connections_made += 1
            continue
    circuits = [c for c in circuits if len(c) > 0]
    tablePrint(circuits)
    tablePrint([c for c in circuits if len(c) > 1])
    top_three = sorted([len(sub) for sub in circuits if len(sub) > 0], reverse=True)[:3]
    print(f"Product: {top_three[0] * top_three[1] * top_three[2]}")
    
    # for point in range(len(circuits)): # loop through the circuits
    #     closestCoord = points[point].findClosestPoint(circuits)
        

    
    # circuitMerged = False
    # # Group Circuits
    # for circuitIndex in range(len(circuits)): # loop through the circuits GROUP array. [[{x,y,z}, {x,y,z}]]
    #     if closestCoord in circuits[circuitIndex]: # If the coord with the smallest distance from the main circuit is in the group
    #         print('Box closest to the main box is already a part of a circuit')
    #         circuits[circuitIndex].append(points[point])
    #         circuitMerged = True
    #         break
    # if not circuitMerged:
    #     print('Creating_Circuit: ', points[point])
    #     circuits.append([points[point], closestCoord])

        
#     print([len(c) for c in circuits])
#     # fig = plt.figure()
#     # ax = fig.add_subplot(projection='3d')
    
#     # xs = [c['x'] for c in coordinates]
#     # ys = [c['y'] for c in coordinates]
#     # zs = [c['z'] for c in coordinates]
#     # ax.plot(xs, ys, zs)
#     # for coord in coordinates:
#     #     ax.scatter(coord['x'], coord['y'], coord['z'])

#     # ax.set_xlabel('X')
#     # ax.set_ylabel('Y')
#     # ax.set_zlabel('Z')

#     # plt.show()
