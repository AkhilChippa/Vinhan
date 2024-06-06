from typing import List
from collections import Counter

def find_duplicates(arr: List[int]) -> List[int]:
    
    counter = Counter(arr)
    duplicates = [num for num, count in counter.items() if count > 1]
    return duplicates
arr = [1, 2, 3, 2, 4, 5, 5, 6, 2]
duplicates = find_duplicates(arr)
print(duplicates)  # [2, 2, 5]