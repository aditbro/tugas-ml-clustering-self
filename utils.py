import math
import seaborn as sn
import pandas as pd
import matplotlib.pyplot as plt
import statistics

def manhattan_distance(x1, x2):
    total = 0
    for i in range(len(x1)):
        total += x1[i] - x2[i]

    return abs(total)

def euclidean_distance(x1, x2):
    total = 0
    for i in range(len(x1)):
        total += (x1[i] - x2[i])**2

    return math.sqrt(total)

def most_frequent(List): 
    return max(set(List), key = List.count) 

def calculate_accuracy(predicted, expected):
    equal_result = 0
    for i in range(len(predicted)):
        if(predicted[i] == expected[i]):
            equal_result += 1

    return equal_result/len(predicted)*100

def show_confusion_matrix(data=[], labels=None):
    if(not labels):
        labels = [i for i in range(len(data[0]))]
    df_cm = pd.DataFrame(data)
    sn.set(font_scale=1.4)#for label size
    sn.heatmap(df_cm, annot=True,annot_kws={"size": 16})# font size

    # plt.show()

def build_confusion_matrix(predicted, expected, class_num=None):
    class_num = class_num if class_num else len(predicted)
    confusion_matrix = [[0 for x in range(class_num)] for x in range(class_num)]

    for key in predicted:
        for i in range(len(predicted[key])):
            confusion_matrix[expected[key][i]][predicted[key][i]] += 1

    return confusion_matrix

def build_conf_mat_from_bare(predicted, expected, classes):
    confusion_matrix = [[0 for x in range(len(classes))] for x in range(len(classes))]

    for i in range(len(predicted)):
        confusion_matrix[expected[i]][predicted[i]] += 1

    return confusion_matrix

def build_class_mapping(class_data, classifier):
    mapping = {}
    for key in class_data:
        modus = statistics.mode([classifier.predict(x) for x in class_data[key]])
        mapping[key] = modus

    return mapping