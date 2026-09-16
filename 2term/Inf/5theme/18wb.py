import random

def task1():
    print("Y = (not S and D0) or (S and D1)")
    # Y = (not S and D0) or (S and D1)

def task2():
    def mux(D0, D1, S):
        return int((not S and D0) or (S and D1))

    for D0 in [0,1]:
        for D1 in [0,1]:
            for S in [0,1]:
                print(D0, D1, S, mux(D0,D1,S))
    # 0 0 0 0
    # 0 0 1 0
    # 0 1 0 0
    # 0 1 1 1
    # 1 0 0 1
    # 1 0 1 0
    # 1 1 0 1
    # 1 1 1 1

def task3():
    def mux4(D, S1, S0):
        i = S1*2 + S0
        return D[i]

    for D in [(0,0,0,0),(0,0,0,1),(0,0,1,0),(0,0,1,1)]:
        for S1 in [0,1]:
            for S0 in [0,1]:
                print(D, S1, S0, mux4(D,S1,S0))
    # ((0, 0, 0, 0), 0, 0, 0)
    # ((0, 0, 0, 0), 0, 1, 0)
    # ((0, 0, 0, 0), 1, 0, 0)
    # ((0, 0, 0, 0), 1, 1, 0)
    # ((0, 0, 0, 1), 0, 0, 0)
    # ((0, 0, 0, 1), 0, 1, 0)
    # ((0, 0, 0, 1), 1, 0, 0)
    # ((0, 0, 0, 1), 1, 1, 1)
    # ((0, 0, 1, 0), 0, 0, 0)
    # ((0, 0, 1, 0), 0, 1, 0)
    # ((0, 0, 1, 0), 1, 0, 1)
    # ((0, 0, 1, 0), 1, 1, 0)
    # ((0, 0, 1, 1), 0, 0, 0)
    # ((0, 0, 1, 1), 0, 1, 0)
    # ((0, 0, 1, 1), 1, 0, 1)
    # ((0, 0, 1, 1), 1, 1, 1)

def task4():
    class RS:
        def __init__(self):
            self.Q = 0
        def update(self, S, R):
            if S==1 and R==0: self.Q=1
            elif S==0 and R==1: self.Q=0
            elif S==1 and R==1: return "ERR"
            return self.Q

    rs = RS()
    for S in [0,1]:
        for R in [0,1]:
            print(S,R,rs.update(S,R))
    # 0 0 0
    # 0 1 0
    # 1 0 1
    # 1 1 ERR

def task5():
    class D:
        def __init__(self):
            self.Q = 0
        def update(self, Dv):
            self.Q = Dv
            return self.Q

    d = D()
    for x in [0,1,1,0]:
        print(x, d.update(x))
    # 0 0
    # 1 1
    # 1 1
    # 0 0

def task6():
    class JK:
        def __init__(self):
            self.Q = 0
        def update(self, J,K):
            if J==0 and K==0: pass
            elif J==0 and K==1: self.Q=0
            elif J==1 and K==0: self.Q=1
            else: self.Q = 1-self.Q
            return self.Q

    jk = JK()
    for J in [0,0,1,1]:
        for K in [0,1]:
            print(J,K,jk.update(J,K))
    # 0 0 0
    # 0 1 0
    # 0 0 0
    # 0 1 0
    # 1 0 1
    # 1 1 0
    # 1 0 1
    # 1 1 0

def task7():
    def mux(D0,D1,S):
        return (not S and D0) or (S and D1)

    def f(x,y,z):
        return mux(y, not y, x) ^ z

    for x in [0,1]:
        for y in [0,1]:
            for z in [0,1]:
                print(x,y,z,int(f(x,y,z)))
    # 0 0 0 0
    # 0 0 1 1
    # 0 1 0 1
    # 0 1 1 0
    # 1 0 0 1
    # 1 0 1 0
    # 1 1 0 0
    # 1 1 1 1

def task8():
    def f(x,y,z):
        return (x and y) or (x and z)
    def simp(x,y,z):
        return x and (y or z)

    for x in [0,1]:
        for y in [0,1]:
            for z in [0,1]:
                print(x,y,z,int(f(x,y,z)),int(simp(x,y,z)))
    # 0 0 0 0 0
    # 0 0 1 0 0
    # 0 1 0 0 0
    # 0 1 1 0 0
    # 1 0 0 0 0
    # 1 0 1 1 1
    # 1 1 0 1 1
    # 1 1 1 1 1

def task9():
    class Node:
        def __init__(self, func, inputs):
            self.func = func
            self.inputs = inputs

    def AND(a,b): return a and b
    def OR(a,b): return a or b

    def eval_scheme(x,y):
        n1 = AND(x,y)
        n2 = OR(x,y)
        return n1,n2

    for x in [0,1]:
        for y in [0,1]:
            print(x,y,eval_scheme(x,y))
    print(True)
    # 0 0 (0, 0)
    # 0 1 (0, 1)
    # 1 0 (0, 1)
    # 1 1 (1, 1)
    # True

def task10():
    class D:
        def __init__(self):
            self.Q=0
        def update(self,Dv):
            prev=self.Q
            self.Q=Dv
            return prev,self.Q

    d=D()
    inputs=[random.randint(0,1) for _ in range(10)]
    for t,inp in enumerate(inputs):
        prev,new=d.update(inp)
        print(t,inp,prev,new,new)
    print(True)