(lambda m,t,i: [i.append(i[-1]+1) or cur+i[-1]*i[-1]>m or t.append(cur+i[-1]*i[-1]) for cur in t] and print(len(t)-1) or print(t[-1]))(int(input()), [0], [0])
