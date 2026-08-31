"""ML Practice: Time Series Forecasting using Simple and Weighted Moving Average"""


def simple_moving_average(series, window):
    return [sum(series[i - window:i]) / window for i in range(window, len(series) + 1)]


def weighted_moving_average(series, weights):
    window = len(weights)
    total_weight = sum(weights)
    return [
        sum(series[i - window + j] * weights[j] for j in range(window)) / total_weight
        for i in range(window, len(series) + 1)
    ]


def forecast_next(series, window):
    return sum(series[-window:]) / window


if __name__ == "__main__":
    sales = [10, 12, 13, 12, 15, 16, 18, 17, 19, 20]

    print("SMA (window=3):", [round(v, 2) for v in simple_moving_average(sales, 3)])
    print("WMA (weights=[1,2,3]):", [round(v, 2) for v in weighted_moving_average(sales, [1, 2, 3])])
    print("Next period forecast:", round(forecast_next(sales, 3), 2))
