import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def init(a,tree,node,start,end):
    if start == end:
        tree[node] = start
    else:
        mid = (start+end)//2
        init(a,tree, node*2, start, mid)
        init(a, tree, node*2+1, mid+1,end)
        if nums[tree[node*2]] > nums[tree[node*2+1]]:
            tree[node] = tree[node*2+1]
        else:
            tree[node] = tree[node*2]

def query(tree,node,start,end,left,right):
    if left > end or right < start:
        return -1
    if left <= start and end <= right:
        return tree[node]
    l = query(tree,node*2, start, (start+end)//2, left, right)
    r = query(tree, node*2+1, (start+end)//2+1, end, left, right)
    if l == -1:
        return r
    elif r == -1:
        return l
    else:
        if nums[l] > nums[r]:
            return r
        else:
            return l

def find(s,e,n):
    global stack
    if n == 1:
        if stack < nums[s]:
            stack = nums[s]
        return
    sm_idx = query(tree,1,0,n2-1,s,e-1)
    if nums[sm_idx]*n > stack:
        stack = nums[sm_idx]*n
    if s == sm_idx:
        find(s+1,e,n-1)
        return
    elif e-1 == sm_idx:
        find(s,sm_idx,n-1)
        return
    find(s,sm_idx,sm_idx-s)
    find(sm_idx+1,e,e-sm_idx-1)
    return

while True:
    nums = list(map(int,input().split()))
    n = nums[0]
    n2 = n
    tree = [0 for i in range(4*n)]
    del nums[0]
    stack = 0
    if n == 0:
        break
    init(nums,tree,1,0,n-1)
    find(0,n,n)
    print(stack)