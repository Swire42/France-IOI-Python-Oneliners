(lambda n,mi,ma,t: [(print("Rien à signaler") or (t.append(0) if len(t)<n else 0)) if mi<=int(input())<=ma else print("Alerte !!") for i in t])(int(input()), int(input()), int(input()), [0])
