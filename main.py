import csv
import pandas as pd
from src.dbscan import *
from src.kmeans import *

filename = input("Filename train data: ")
data = pd.read_csv(filename)

print("Daftar metode: ")
print("1. DBScan")
print("2. KMeans")
print("3. KMedoids")
method = int(input("No metode: "))
if method == 1:
    e = float(input("eps (0-1): "))
    min_pts = int(input("min_pts: "))
    dbscan(data, e, min_pts)
    data.to_csv("output_dbscan.csv")
elif method == 2:
    k = int(input("Masukkan k: "))
    kmeans(data, k)
    data.to_csv("output_kmeans.csv")
elif method == 3:
    k = int(input("Masukkan k: "))
    print("halo")

