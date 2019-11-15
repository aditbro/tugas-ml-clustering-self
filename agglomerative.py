from functools import reduce
from utils import manhattan_distance

class Agglomerative():
    @classmethod
    def single_link(cls, cluster_a, cluster_b):
        min_distance = 9999999999999

        for a in cluster_a:
            for b in cluster_b:
                distance = manhattan_distance(a, b)
                min_distance = min(distance, min_distance)

        return min_distance

    @classmethod
    def complete_link(cls, cluster_a, cluster_b):
        max_distance = -1

        for a in cluster_a:
            for b in cluster_b:
                distance = manhattan_distance(a, b)
                min_distance = max(distance, min_distance)

        return max_distance

    @classmethod
    def avg_group_link(cls, cluster_a, cluster_b):
        total_a = reduce(lambda a, b: [x[0] + x[1] for x in zip(a, b)], cluster_a, [0 for x in range(len(cluster_a[0]))])
        total_b = reduce(lambda a, b: [x[0] + x[1] for x in zip(a, b)], cluster_b, [0 for x in range(len(cluster_b[0]))])
        avg_a = list(map(lambda x: x/len(cluster_a), total_a))
        avg_b = list(map(lambda x: x/len(cluster_b), total_b))

        return manhattan_distance(avg_a, avg_b)

    @classmethod
    def avg_link(cls, cluster_a, cluster_b):
        total_distance = 0
        counter = 0

        for a in cluster_a:
            for b in cluster_b:
                total_distance += manhattan_distance(a, b)
                counter += 1

        return total_distance/counter

    def __init__(self, n_cluster=2, dist_function=None):
        self.dist_function = dist_function if dist_function else Agglomerative.avg_group_link
        self.n_cluster = n_cluster
    
    def fit(self, data):
        self.data = data
        self.clusters = [[x] for x in self.data]
        self.classify()

    def classify(self):
        while(len(self.clusters) > self.n_cluster):
            a, b = self.find_minimum_distance_index_pair()
            new_cluster = self.clusters[a] + self.clusters[b]
            if(b > a):
                b = b - 1
            self.clusters.pop(a)
            self.clusters.pop(b)
            self.clusters.append(new_cluster)

    def predict(self, data):
        data = [data]
        min_distance_cluster = -1
        min_distace = 99999999999999

        for i in range(len(self.clusters)):
            distance = self.dist_function(data, self.clusters[i])
            if(distance < min_distace):
                min_distance_cluster = i
                min_distace = distance

        return min_distance_cluster

    def find_minimum_distance_index_pair(self):
        min_distance = 9999999999999
        min_i = 0
        min_j = 0

        for i in range(len(self.clusters)):
            for j in range(i, len(self.clusters)):
                if(i != j):
                    distance = self.dist_function(self.clusters[i], self.clusters[j])
                    if(distance < min_distance):
                        min_i = i
                        min_j = j
                        min_distance = distance

        return min_i, min_j
