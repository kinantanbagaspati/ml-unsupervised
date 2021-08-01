def distance(coordinate1, coordinate2):
    toReturn = 0
    for i in range(len(coordinate1)):
        toReturn += (coordinate2[i]-coordinate1[i])**2
    return toReturn

def normalize(data):
    normalized = [[] for i in range(len(data))]
    for i in range(len(data.columns)):
        min_val = data[data.columns[i]].min()
        max_val = data[data.columns[i]].max()
        for j in range(len(data)):
            normalized[j].append((data[data.columns[i]][j] - min_val)/(max_val - min_val))
    return normalized