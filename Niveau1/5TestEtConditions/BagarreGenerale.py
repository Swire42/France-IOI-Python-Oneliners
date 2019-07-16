(lambda a,e: abs(a-e)<=10 or print("La famille", ["Arignon", "Evaran"][a<e], "a un champ trop grand"))(int(input()), int(input()))
