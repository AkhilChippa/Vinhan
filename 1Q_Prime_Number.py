def is_prime(n:int)->bool:
    factors=0
    if n<=1:
        return False
    else:
        for i in range(2,n):
            if n%i==0:
                factors+=1
    if factors>0:
        return False
    else:
        return True
n=int(input())
print(is_prime(n))
print("logic ended")
print("end2")