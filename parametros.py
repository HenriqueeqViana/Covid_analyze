#parâmetros retirados de  https://github.com/csdegraaf/CoronaVirusModel
#Adaptado por HenriqueeqViana 
class Params:
    def __init__(self, c, n, sigma, gamma, r_zero):
        self.c = c
        self.N = n
        self.sigma = sigma
        self.gamma = gamma
        self.r_zero = r_zero