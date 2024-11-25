# import extra.iota
# from sys import path
# path.append('..\\packages')

# print(extra.iota.funI())


# also works
# from sys import path
# path.append('..\\packages')

# from extra.iota import funI
# print(funI())


# from extra.good.best.tau import funT
# import extra.good.best.sigma
# from sys import path

# path.append('..\\packages')


# print(extra.good.best.sigma.funS())
# print(funT())


import extra.good.alpha as alp
import extra.good.best.sigma as sig
from sys import path

path.append('..\\packages')


print(sig.funS())
print(alp.funA())
