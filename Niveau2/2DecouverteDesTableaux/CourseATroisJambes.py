(lambda t: [t.append(int(input())) for i in range(int(input()))] and t.sort() or [print(t[i], t[-i-1]) for i in range(len(t)//2)])([])
