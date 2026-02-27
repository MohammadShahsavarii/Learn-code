# Tuples are like List ( index, slice, ...) But is immutable
# tuples made faster,more optim, need limit ram space, working on it is easier
t1=(1, 2, 3, "sara", 3.1415)
print(t1)       # (1, 2, 3, 'sara', 3.1415)
print(t1[2])    # 3
print(t1[-1])   # 3.1415
print(len(t1))  # 5


result = ("sara", 15)
name, score = result
print(name)     # sara
print(score)    # 15

cordinate =(3, 4)
origin =(0,0)
