(lambda t: [t.append(int(input())) for i in range(int(input()))] and t.sort() or (print(t[len(t)//2]) if len(t)%2 else print((t[len(t)//2-1]+t[len(t)//2])/2)))([])
