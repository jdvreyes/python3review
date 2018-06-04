# wurzel.py

from time import time


def wurzel(x, n=10):
    if n == 1:
        return 1
    else:
        preValue = wurzel(x, n-1)
        return 0.5*(preValue + x/preValue)
        # return 0.5*(wurzel(x, n-1) + x/wurzel(x, n-1))


tic = time()
sqrt= wurzel(2,40)
toc = time()
print("Sqrt of", 2, ": ", sqrt)
print("Running time: ", toc -tic)
