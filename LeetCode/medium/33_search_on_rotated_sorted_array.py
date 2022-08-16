def search(nums, target):
    def binary_search(lst, low, hi, target):
        mid = low + ((hi - low) // 2)
        if low > hi:
            return -1
        elif lst[mid] == target:
            return mid

        if lst[low] <= lst[mid]:
            if lst[low] <= target <= lst[mid]:
                return binary_search(lst, low, mid - 1, target)
            else:
                return binary_search(lst, mid + 1, hi, target)
        
        else:
            if lst[mid] <= target <= lst[hi]:
                return binary_search(lst, mid + 1, hi, target)
            else:
                return binary_search(lst, low, mid - 1, target)
    
    id = binary_search(nums, 0, len(nums) - 1, target)
    return id

search([4, 5, 6, 7, 0, 1, 2], 3)