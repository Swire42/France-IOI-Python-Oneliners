(lambda t: [t.append(t[-1]+1) if int(input())>0 else t.append(t[-1]-1) for i in range(int(input())*2)] and print(max(t)))([0])
