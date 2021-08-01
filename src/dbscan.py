from .my_util import *

def dbscan(data, e, min_pts):
    normalized = normalize(data)
    dim = len(data.columns)
    e = e*e*dim
    result = [-1 for i in range(len(data))]
    cluster_id = 0
    for i in range(len(normalized)):
        if result[i] < 0: #Belom punya cluster
            neighbor = 0
            for j in range(len(normalized)):
                if(distance(normalized[i], normalized[j]) < e):
                    neighbor += 1
            if neighbor >= min_pts:
                #mulai cluster
                q = [i]
                result[i] = cluster_id
                print(str(i), "masuk ke cluster", str(cluster_id))
                while(len(q)>0):
                    head = q.pop(0)
                    for j in range(len(normalized)):
                        if(distance(normalized[head], normalized[j]) < e) and (result[j]<0):    
                            q.append(j)
                            result[j] = cluster_id
                cluster_id += 1
    data["cluster"] = result
