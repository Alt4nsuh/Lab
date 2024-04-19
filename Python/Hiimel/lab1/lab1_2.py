from collections import deque

def Mysort(arrs):
    daraalal = deque(sorted(arrs))

    return daraalal

arrs = deque([5, 1, 3, 2, 4,9,8])
arrs = Mysort(arrs)

print( arrs)
