def get_all_sums(arr):
    sums = [0]  # Start with a sum of 0 (empty subset)
    for num in arr:
        new_sums = []
        for s in sums:
            new_sums.append(s + num)
        sums.extend(new_sums)
    return sums

def count_combinations(N, K, pieces):
    # Split the pieces into two halves
    first_half = pieces[:N // 2]
    second_half = pieces[N // 2:]
    
    # Generate all possible sums for both halves
    first_sums = get_all_sums(first_half)
    second_sums = get_all_sums(second_half)
    
    # Count valid combinations where sum1 + sum2 equals K
    count = 0
    for sum1 in first_sums:
        for sum2 in second_sums:
            if sum1 + sum2 == K:
                count += 1
    
    return count

# Input
N, K = map(int, input().split())
pieces = list(map(int, input().split()))

# Output the result
print(count_combinations(N, K, pieces))
