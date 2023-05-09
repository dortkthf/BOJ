def solution(arr, idx):
    for i in range(len(arr)):
        if i >= idx and arr[i] == 1:
            return i
    else:
        return -1    
