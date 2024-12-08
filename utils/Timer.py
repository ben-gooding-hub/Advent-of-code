from time import time
def timeMethod(method, dp: int):
    t0 = time()
    method()
    t1 = time()
    format = "\{:."+ str(dp) +"f\}"
    print(f"Execution time: {format.format(t1-t0)}")
