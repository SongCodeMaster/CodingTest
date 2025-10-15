import numpy as np

def solution(sizes):
    sizes = [[max(w,h),min(w,h)] for w,h in sizes]
    weight = max(w for w,h in sizes)
    height = max(h for w,h in sizes)
    
    return weight*height