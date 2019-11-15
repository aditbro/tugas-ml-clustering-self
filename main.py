from data_loader import load_file
from k_means import Kmeans
from dbscan import DBSCAN
from random import shuffle
from utils import calculate_accuracy
from sklearn.cluster import KMeans
from utils import euclidean_distance
import pry

raw_data = load_file('iris.data')
classes = set([x[-1] for x in raw_data])
class_dict = {}
test_data = {}
train_data = []
for kelas in classes:
    class_dict[kelas] = list(filter(lambda x: x[-1] == kelas, raw_data))
    shuffle(class_dict[kelas])

    test_data[kelas] = [x[:-1] for x in class_dict[kelas][:10]]
    train_data += [x[:-1] for x in class_dict[kelas][10:]]

db_scan = DBSCAN(1, 0.5)
pry()
db_scan.fit(train_data[:10])
db_scan.clusters