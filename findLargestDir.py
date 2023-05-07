import os
import sys
import pathlib
import heapq
from hurry.filesize import size

def main(n,root):
    dirSize = []
    root = pathlib.Path(root)
    heapq.heapify(dirSize)
    for dir in root.glob('*'):
        print(dir)
        sizes = 0
        for f in dir.glob('**/*'):
            if f.is_file():
                bytes = f.stat().st_size
                sizes += bytes
        heapq.heappush(dirSize, (-1*sizes,dir))
    d = list(dirSize)
    l = len(d)
    for i in range(int(n)):
        if i >= l:
            return
        p = heapq.heappop(dirSize)
        print(size(p[0]*-1), ': ', p[1])
    return

if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise Execption("Input the nth number of largest directories and path of the root directory")
        #python findLargestDir.py 10 C:/"Program Files (x86)"
    n = sys.argv[1]
    root = sys.argv[2]
    if int(n) <= 0:
        n = 10
    main(n,root)
