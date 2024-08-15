def push_front_pf(dq,x):
    dq.appendleft(x)
    

#Function to push element x to the back of the deque.
def push_back_pb(dq,x):
    dq.append(x)
    
#Function to return element from front of the deque.
def front_dq(dq):
    if not dq: return -1
    return dq[0]
    
#Function to pop element from back of the deque.
def pop_back_ppb(dq):
    if dq:
        dq.pop()
