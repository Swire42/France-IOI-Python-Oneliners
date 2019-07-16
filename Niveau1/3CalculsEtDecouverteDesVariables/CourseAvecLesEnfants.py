from robot import*
[[droite() for _ in range(i+1)] and ramasser() or [gauche() for _ in range(i+1)] and deposer() for i in range(10)]
