from random import random
from utils import manhattan_distance
from functools import reduce
from operator import add
import pry

class Kmeans():
    def __init__(self, n_clusters):
        self.n_clusters = n_clusters
    
    def fit(self, data):
        self.data = data
        self.init_centroid()
        self.init_clusters()
        self.classify()

    def init_centroid(self):
        self.dimension = len(self.data[0])
        max_val = max([max(x) for x in self.data])
        self.centroid = [[random() * max_val for i in range(self.dimension)] for x in range(self.n_clusters)]
    
    def init_clusters(self):
        self.clusters = [[] for i in range(self.n_clusters)]

    def classify(self):
        prev_centroid = []
        while prev_centroid != self.centroid:
            prev_centroid = self.centroid.copy()
            self.make_new_clusters()
            self.calculate_new_centroid()

    def make_new_clusters(self):
        self.init_clusters()
        for datum in self.data:
            idx = self.predict(datum)
            self.clusters[idx].append(datum)
    
    def calculate_new_centroid(self):
        for i in range(len(self.clusters)):
            cluster = self.clusters[i]
            cluster_len = len(cluster) if len(cluster) > 0 else 1
            
            self.centroid[i] = [0 for x in range(self.dimension)]
            for member in cluster:
                self.centroid[i] = list(map(add, self.centroid[i], member))
            
            self.centroid[i] = list(map(lambda x: x/cluster_len, self.centroid[i]))

    def predict(self, datum):
        min_distance = manhattan_distance(self.centroid[0], datum)
        min_idx = 0

        for i in range(0, self.n_clusters):
            distance = manhattan_distance(datum, self.centroid[i])
            if(distance < min_distance):
                min_distance = distance
                min_idx = i

        return min_idx

