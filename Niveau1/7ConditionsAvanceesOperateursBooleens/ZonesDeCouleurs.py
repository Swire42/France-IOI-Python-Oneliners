[(lambda a,o: print(["En dehors de la feuille", "Dans une zone rouge", "Dans une zone jaune", "Dans une zone bleue"][(-((60<o<70) and (15<a<45 or 60<a<85)) + 2*(0<a<90 and 0<o<70) + (10<a<85 and 10<o<55) - (25<a<50 and 20<o<45))]))(int(input()), int(input())) for i in range(int(input()))]
