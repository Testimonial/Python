import multiprocessing as mp
from datetime import datetime
import concurrent.futures
import numpy as np
import time
 
def tAsk(req):
    for i in range(1000):
        True
 
def rT(subRex):
    with concurrent.futures.ThreadPoolExecutor(max_workers=12) as exe:
        exe.map(tAsk,subRex)
 
def rP():
    with concurrent.futures.ProcessPoolExecutor(max_workers=8) as exe:
        exe.map(rT, tRex)
 
if __name__ == "__main__":
    rows = 8
    cols = 1000000
    tRex = np.ndarray((rows,cols,),dtype=object)
    for i in range(rows):
        for j in range(cols):
            tRex[i][j]={}
            tRex[i][j]["_id"] = (i + 1) * (j + 1)
            tRex[i][j]['Row']=i+1
            tRex[i][j]['Col']=j+1
 
    start = time.perf_counter()
    rP()
    finish = time.perf_counter()
    print(f"Finished in {round(finish-start, 2)} seconds")
