"""ML Practice: Early Stopping During Iterative Training"""


def train_with_early_stopping(train_losses, val_losses, patience=3):
    best_val = float("inf")
    best_epoch = -1
    epochs_without_improvement = 0

    for epoch, (train_loss, val_loss) in enumerate(zip(train_losses, val_losses)):
        if val_loss < best_val:
            best_val = val_loss
            best_epoch = epoch
            epochs_without_improvement = 0
        else:
            epochs_without_improvement += 1

        print(f"epoch {epoch}: train_loss={train_loss:.3f}, val_loss={val_loss:.3f}")

        if epochs_without_improvement >= patience:
            print(f"Early stopping at epoch {epoch} (best epoch was {best_epoch}, best val_loss={best_val:.3f})")
            return best_epoch, best_val

    return best_epoch, best_val


if __name__ == "__main__":
    train_losses = [0.90, 0.70, 0.55, 0.45, 0.38, 0.33, 0.30, 0.28, 0.27, 0.26]
    val_losses = [0.95, 0.75, 0.60, 0.50, 0.48, 0.49, 0.50, 0.52, 0.55, 0.58]

    best_epoch, best_val = train_with_early_stopping(train_losses, val_losses, patience=3)
    print(f"Best model: epoch {best_epoch}, val_loss={best_val:.3f}")
