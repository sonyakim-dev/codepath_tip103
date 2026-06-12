def analyze_library(library_catalog, actual_distribution):
    result = {}
    for key, val in library_catalog.items():
        result[key] = actual_distribution[key] - library_catalog[key]
    return result

library_catalog = {
    "Room A": 150,
    "Room B": 200,
    "Room C": 250,
    "Room D": 300
}

actual_distribution = {
    "Room A": 150,
    "Room B": 190,
    "Room C": 260,
    "Room D": 300
}

# print(analyze_library(library_catalog, actual_distribution))


def find_common_artifacts(artifacts1, artifacts2):
    artifacts1 = set(artifacts1)
    result = [] 
    
    for art2 in artifacts2:
        if art2 in artifacts1:
            result.append(art2)
    return result

# artifacts1 = ["Statue of Zeus", "Golden Vase", "Bronze Shield"]
# artifacts2 = ["Golden Vase", "Silver Sword", "Bronze Shield"]

# print(find_common_artifacts(artifacts1, artifacts2))

from collections import Counter


def declutter(souvenirs, threshold):
    counter = Counter(souvenirs)
    result = []
    
    for souv, count in counter.items():
        if count < threshold:
            result.append(souv)
    return result

# souvenirs1 = ["coin", "alien egg", "coin", "coin", "map", "map", "statue"]
# threshold1 = 3
# print(declutter(souvenirs1, threshold1))

# souvenirs2 = ["postcard", "postcard", "postcard", "sword"]
# threshold2 = 2
# print(declutter(souvenirs2, threshold2))


def num_of_time_portals(portals, destination):
    count = 0
    for i in range(len(portals)):
        for j in range(len(portals)):
            if i == j: continue
            if portals[i] + portals[j] == destination:
                count += 1
    return count

portals1 = ["777", "7", "77", "77"]
destination1 = "7777"
portals2 = ["123", "4", "12", "34"]
destination2 = "1234"
portals3 = ["1", "1", "1"]
destination3 = "11"

print(num_of_time_portals(portals1, destination1))
print(num_of_time_portals(portals2, destination2))
print(num_of_time_portals(portals3, destination3))


def detect_temporal_anomaly(time_points, k):
    pass

time_points1 = [1, 2, 3, 1]
k1 = 3

time_points2 = [1, 0, 1, 1]
k2 = 1

time_points3 = [1, 2, 3, 1, 2, 3]
k3 = 2

print(detect_temporal_anomaly(time_points1, k1))  
print(detect_temporal_anomaly(time_points2, k2)) 
print(detect_temporal_anomaly(time_points3, k3)) 
