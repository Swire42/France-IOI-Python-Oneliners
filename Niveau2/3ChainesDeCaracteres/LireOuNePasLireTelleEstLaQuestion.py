(lambda t: [(lambda c: len(c)>len(t[-1]) and (print(c) or t.append(c)))(input()) for i in range(int(input()))])([""])
