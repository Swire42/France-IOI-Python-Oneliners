(lambda mini,pos: [(lambda n: n<=mini[-1] and (mini.append(n) or pos.append(i+1)))(int(input())) for i in range(int(input()))] and print(pos[-1]))([10000000],[])
