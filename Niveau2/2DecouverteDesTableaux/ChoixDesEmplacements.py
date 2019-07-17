(lambda t: [(lambda j: t.pop(j)=="NaN" or t.insert(j, i))(int(input())) for i in range(len(t))] and [print(i) for i in t])([0 for i in range(int(input()))])
