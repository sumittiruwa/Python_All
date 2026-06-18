scores = [65,23,12,34]

# filter : only passing scores (>=60)

passed = [ s for s in scores if s >= 60]

# transform : nrmalize to 0-1 scale  (ML)

normalized = [s/100 for s in scores]

#both : squared values of passing scores

sq_pass = [s**2 for s in scores if s>=60]

print(passed)
print(normalized)
print(sq_pass)
