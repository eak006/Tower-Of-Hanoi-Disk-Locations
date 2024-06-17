from typing import Tuple


def whichDiskMovesAndWhere(m:int,n:int)->Tuple[int]:
    if not (1 <= m <= 2**n - 1):
        # Move number must be between 1 and 2**n - 1 inclusive 
        return None
    # The disk that moves on move m is d = 1 + (number of times m is halved until m is odd)
    d = 1 # Assume disks are indexed from 1 to n inclusive (with n being the largest disk)
    m_ = m
    while m_ % 2 == 0:
        m_ >>= 1
        d += 1
    # Let us find the destination tower
    destination = m + 7 # add 7 on to m
    destination %= 6 # calculate (m+7) mod 6
    destination %= 3 # calculate ((m+7) mod 6) mod 3 so that the destination is in {0,1,2}
    # if d does NOT share the same parity as n, we have one more step to perform
    if d%2 != n%2:
        # Add 1 to destination
        destination += 1
        # Mod destination by 3
        destination %= 3
    return (d, destination)

n = 5
print(f"N = {n}")
for m in range(1,2**n):
    print(f"Move {m} = {whichDiskMovesAndWhere(m,n)}")
    
    
