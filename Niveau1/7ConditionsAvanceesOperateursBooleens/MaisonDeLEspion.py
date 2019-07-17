(lambda ad,af,od,of: print(sum([max(0, (ad<=int(input())<=af) + (od<=int(input())<=of) - 1) for i in range(int(input()))])))(int(input()), int(input()), int(input()), int(input()))
