"""ML Practice: Exponential Moving Average (Smoothing / Model Weights)"""


def ema_series(values, alpha=0.3):
    smoothed = [values[0]]
    for v in values[1:]:
        smoothed.append(alpha * v + (1 - alpha) * smoothed[-1])
    return smoothed


def ema_update(current_avg, new_value, decay=0.99):
    return decay * current_avg + (1 - decay) * new_value


if __name__ == "__main__":
    losses = [2.5, 2.3, 2.6, 2.1, 1.9, 2.0, 1.7, 1.8, 1.5, 1.6]

    smoothed = ema_series(losses, alpha=0.3)
    print("Raw losses:     ", losses)
    print("EMA (alpha=0.3):", [round(v, 3) for v in smoothed])

    shadow_weight = 0.0
    for step, raw_weight in enumerate([1.0, 1.05, 0.98, 1.10, 1.02]):
        shadow_weight = ema_update(shadow_weight if step else raw_weight, raw_weight, decay=0.9)
        print(f"step {step}: raw={raw_weight}, shadow(EMA)={shadow_weight:.4f}")
