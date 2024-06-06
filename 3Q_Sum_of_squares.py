from typing import List
def sum_of_squares(lst: List[int])->int:
    sum_of_square_values=0
    for element in lst:
        sum_of_square_values+=element*element
    return sum_of_square_values

lst=list(map(int,input().split()))
print(sum_of_squares(lst))