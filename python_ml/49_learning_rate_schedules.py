"""ML Practice: Learning Rate Schedules (Step Decay and Exponential Decay)"""

import math


def step_decay(initial_lr, drop_factor, epochs_per_drop, epoch):
    drops = epoch // epochs_per_drop
    return initial_lr * (drop_factor ** drops)


def exponential_decay(initial_lr, decay_rate, epoch):
    return initial_lr * math.exp(-decay_rate * epoch)


if __name__ == "__main__":
    initial_lr = 0.1

    print("epoch | step decay | exponential decay")
    for epoch in range(0, 20, 2):
        step_lr = step_decay(initial_lr, drop_factor=0.5, epochs_per_drop=5, epoch=epoch)
        exp_lr = exponential_decay(initial_lr, decay_rate=0.15, epoch=epoch)
        print(f"{epoch:5d} | {step_lr:.5f}   | {exp_lr:.5f}")
