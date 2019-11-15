from utils import euclidean_distance
import pry
class DBSCAN():
    def __init__(self, minpts=1, epsilon=1):
        self.minpts = minpts
        self.epsilon = epsilon

    def fit(self, data):
        self.data = data
        self.data_length = len(data)
        self.visited = [False for x in range(self.data_length)]
        self.clusters = []
        self.init_distance_matrix()
        self.classify()

    def init_distance_matrix(self):
        self.distance_matrix = [[0 for x in range(self.data_length)] for x in range(self.data_length)]

        for i in range(self.data_length):
            for j in range(i, self.data_length):
                self.distance_matrix[i][j] = euclidean_distance(self.data[i], self.data[j])
                self.distance_matrix[j][i] = self.distance_matrix[i][j]

    def classify(self):
        core_point_idx = self.find_next_core_point_idx()

        while(core_point_idx != -1):
            self.create_new_cluster(core_point_idx)
            core_point_idx = self.find_next_core_point_idx()

        self.identify_outliers()

    def create_new_cluster(self, start_idx):
        self.clusters.append([])
        point_queue = [start_idx]

        while(point_queue):
            point_idx = point_queue.pop(0)
            if(self.visited[point_idx]):
                continue
            close_point_count = 0
            self.visited[point_idx] = True
            self.clusters[-1].append(self.data[point_idx])
            temp_q = []

            for j in range(self.data_length):
                if(j != point_idx):
                    if(self.distance_matrix[point_idx][j] <= self.epsilon):
                        close_point_count += 1
                        if(not self.visited[j]):
                            temp_q.append(j)
            if close_point_count >= self.minpts:
                point_queue += temp_q


    def find_next_core_point_idx(self):
        for i in range(self.data_length):
            if(not self.visited[i]):
                if(self.check_if_core_point(i)):
                    return i

        return -1

    def check_if_core_point(self, idx):
        close_point_count = 0

        for j in range(self.data_length):
            if(j != idx):
                if(self.distance_matrix[idx][j] <= self.epsilon):
                    close_point_count += 1

        return(close_point_count >= self.minpts)

    def identify_outliers(self):
        self.clusters.append([])
        for i in range(self.data_length):
            if(not self.visited[i]):
                self.clusters[-1].append(self.data[i])

    def count_close_point(self, x, cluster):
        close_point_count = 0

        for j in range(len(cluster)):
            if(euclidean_distance(x, cluster[j]) <= self.epsilon):
                close_point_count += 1

        return close_point_count

    def predict(self, x):
        max_close_point_count = 0
        max_idx = 0
        
        for i in range(len(self.clusters)):
            close_point_count = self.count_close_point(x, self.clusters[i])
            if(close_point_count > self.minpts):
                return i
            else:
                if(close_point_count > max_close_point_count):
                    max_idx = i
                    max_close_point_count = close_point_count
        
        return max_idx