(lambda m,d: [(lambda n: m.append(n) if n>0 else d.append(-n))(int(input())) for i in range(int(input()))]=="NaN" or bool(print(sum(m))) or print(sum(d)))([],[])
