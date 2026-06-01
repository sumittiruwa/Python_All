
def count_positive_labels(labels):
    count = 0

    for label in labels:
        if label == 1:
            count += 1

    return count

labels = [1, 0, 1, 1, 0, 1, 0, 0, 1, 1]


positive_count = count_positive_labels(labels)


percentage = (positive_count / len(labels)) * 100


print("Number of clspositive labels:", positive_count)
print("Percentage of positive labels:", percentage, "%")