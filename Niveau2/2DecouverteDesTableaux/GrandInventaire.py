(lambda t: [(lambda i: t[i].append(t[i][-1]+int(input())))(int(input())-1) for _ in range(int(input()))] and [print(i[-1]) for i in t])([[0] for i in range(10)])
