from .my_util import *
import random

def kmeans(data, k):
    normalized = normalize(data)

    result = [-1 for i in range(len(data))]
    min_error = -1
    episodes = 20
    for episode in range(episodes):
        print("Mulai episode", str(episode), end=", error: ")
        calc_result = [-1 for i in range(len(data))]
        means = [[random.uniform(0,1) for j in range(len(normalized[0]))] for i in range(k)]
        done = False
        error = 0
        while (not(done)):
            error = 0
            points_per_cluster = [0.0 for i in range(k)]
            new_means = [[0 for j in range(len(normalized[0]))] for i in range(k)]
            for i in range(len(normalized)):
                #Masukin poin ke kluster
                cluster_id = 0
                min_distance = distance(normalized[i], means[0])
                for j in range(1,k):
                    dis = distance(normalized[i], means[j])
                    if(dis < min_distance):
                        min_distance = dis
                        cluster_id = j
                calc_result[i] = cluster_id
                points_per_cluster[cluster_id] += 1.0
                error += min_distance
                #Menambahkan rata2 kluster
                for j in range(len(normalized[0])):
                    new_means[cluster_id][j] += normalized[i][j]
            #Itung rata-rata
            for i in range(len(new_means)):
                if(points_per_cluster[i]>0):
                    for j in range(len(new_means[0])):
                        new_means[i][j] /= points_per_cluster[i]
            
            #Lakukan terus sampai ga berubah
            done = True
            for i in range(k):
                for j in range(len(normalized[0])):
                    done = (done and (means[i][j] == new_means[i][j]))
                    means[i][j] = new_means[i][j]
            
        print(error)
        if(min_error < 0):
            min_error = error
            result = calc_result


                    
    
    data["cluster"] = result