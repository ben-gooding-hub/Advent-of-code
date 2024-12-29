from time import time
def timeMethod(method, dp: int = 2):
    t0 = time()
    method()
    t1 = time()
    format = "{0:."+ str(dp) +"f}"
    print(f"Execution time: {format.format(t1-t0)}")
