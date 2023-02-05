import time


class Temporizador:
    def __init__(self):
        self.tempo_inicial = self.tempo_final = 0
    
    def marcar(self):
        self.tempo_inicial = time.time()
    
    def pegar(self):
        self.tempo_final = time.time()
        return self.tempo_final - self.tempo_inicial
    
    def acabar(self, segundos):
        if self.pegar() >= segundos:
            return True
        
        return False
