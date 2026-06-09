"""
Simple NumPy Data Analysis & Stats Project
==========================================
Analyzes a sample student scores dataset with common statistical operations.
"""

import numpy as np

# ── 1. Sample Dataset ──────────────────────────────────────────────────────
np.random.seed(42)
students = np.array([
    "Alice", "Bob", "Carol", "Dave", "Eve",
    "Frank", "Grace", "Hank", "Ivy", "Jake"
])
scores = np.random.randint(50, 100, size=(10, 3))  # 10 students, 3 subjects
subjects = ["Math", "Science", "English"]

print("=" * 50)
print("       STUDENT SCORES ANALYSIS")
print("=" * 50)

# ── 2. Display Raw Data ────────────────────────────────────────────────────
print("\n📋 Raw Scores (Math | Science | English):")
print(f"{'Student':<10}", " | ".join(f"{s:>8}" for s in subjects))
print("-" * 40)
for name, row in zip(students, scores):
    print(f"{name:<10}", " | ".join(f"{v:>8}" for v in row))

# ── 3. Basic Stats Per Subject ─────────────────────────────────────────────
print("\n📊 Statistics Per Subject:")
print(f"{'Metric':<12}", " | ".join(f"{s:>8}" for s in subjects))
print("-" * 40)
stats = {
    "Mean":   np.mean(scores, axis=0),
    "Median": np.median(scores, axis=0),
    "Std Dev": np.std(scores, axis=0),
    "Min":    np.min(scores, axis=0),
    "Max":    np.max(scores, axis=0),
}
for label, values in stats.items():
    print(f"{label:<12}", " | ".join(f"{v:>8.2f}" for v in values))

# ── 4. Per-Student Average ─────────────────────────────────────────────────
averages = np.mean(scores, axis=1)
print("\n🎓 Student Averages:")
ranked = np.argsort(averages)[::-1]
for rank, idx in enumerate(ranked, 1):
    bar = "█" * int(averages[idx] / 5)
    print(f"  {rank}. {students[idx]:<8}  {averages[idx]:5.1f}  {bar}")

# ── 5. Pass / Fail ─────────────────────────────────────────────────────────
PASS_MARK = 70
passed = averages >= PASS_MARK
print(f"\n✅ Passed (avg ≥ {PASS_MARK}): {students[passed].tolist()}")
print(f"❌ Failed (avg < {PASS_MARK}): {students[~passed].tolist()}")

# ── 6. Correlation Between Subjects ───────────────────────────────────────
print("\n🔗 Subject Correlation Matrix:")
corr = np.corrcoef(scores.T)
print(f"{'':>10}", " | ".join(f"{s:>8}" for s in subjects))
print("-" * 40)
for i, subj in enumerate(subjects):
    print(f"{subj:<10}", " | ".join(f"{corr[i, j]:>8.3f}" for j in range(3)))

# ── 7. Outlier Detection (Z-score) ────────────────────────────────────────
print("\n⚠️  Outlier Detection (|Z-score| > 1.5):")
z_scores = np.abs((scores - np.mean(scores, axis=0)) / np.std(scores, axis=0))
outliers = np.argwhere(z_scores > 1.5)
if len(outliers):
    for idx in outliers:
        r, c = idx
        print(f"   {students[r]} - {subjects[c]}: score={scores[r, c]}, z={z_scores[r, c]:.2f}")
else:
    print("   No outliers found.")

print("\n" + "=" * 50)
print("Analysis complete!")