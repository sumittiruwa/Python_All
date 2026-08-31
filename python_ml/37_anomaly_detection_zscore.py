"""ML Practice: Anomaly Detection using Z-Score"""


def z_scores(values):
    mean = sum(values) / len(values)
    variance = sum((v - mean) ** 2 for v in values) / len(values)
    stdev = variance ** 0.5 or 1e-9
    return [(v - mean) / stdev for v in values]


def detect_anomalies(values, threshold=2.5):
    scores = z_scores(values)
    return [values[i] for i in range(len(values)) if abs(scores[i]) > threshold]


if __name__ == "__main__":
    data = [10, 12, 11, 13, 12, 10, 11, 95, 12, 13, -80, 11]

    anomalies = detect_anomalies(data)
    print("Data:", data)
    print("Anomalies detected:", anomalies)
