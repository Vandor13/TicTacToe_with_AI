def rec_sum(n):
    # write the insides here!
    # Base Case
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n + rec_sum(n - 1)