def find_factor_pairs(n):
    """Find all pairs of integers (a, b) such that a * b = n."""
    pairs = []
    # Only need to check up to square root of n to avoid duplicate pairs
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            pairs.append((i, n // i))
    return pairs

# Find all factor pairs of 234
number = 234
factor_pairs = find_factor_pairs(number)

# Print the results
print(f"All pairs of numbers that multiply to {number}:")
for i, (a, b) in enumerate(factor_pairs, 1):
    print(f"{i}. {a} × {b} = {a * b}")

# Also include negative number pairs
negative_pairs = [(-a, -b) for a, b in factor_pairs[1:]]  # Skip (1, 234) to avoid duplication
if negative_pairs:
    print("\nNegative number pairs:")
    for i, (a, b) in enumerate(negative_pairs, len(factor_pairs) + 1):
        print(f"{i}. {a} × {b} = {a * b}")

print("\nTotal number of unique ordered pairs:", len(factor_pairs) * 2 - 1)  # -1 because (1,234) and (-1,-234) are the same when ordered
