def binary_search_upper(lst, target):
    lo, hi = 0, len(lst)
    while lo < hi:
        mid = (lo + hi) // 2
        if lst[mid] <= target:
            lo = mid + 1
        else:
            hi = mid

    return lo


def binary_search_lower(lst, target):
    lo, hi = 0, len(lst)
    while lo < hi:
        mid = (lo + hi) // 2
        if lst[mid] >= target:
            hi = mid
        else:
            lo = mid + 1

    return lo
