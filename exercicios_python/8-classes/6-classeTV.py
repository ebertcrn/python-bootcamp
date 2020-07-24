class Tv:
    def __init__(self, canal=1, volume=0):
        self.canal = canal
        self.volume = volume
        if self.canal > 10 or self.canal <= 0:
            print('Canal inválido.')
            self.canal = 1

    def aumenta_canal(self):
        if self.canal == 10:
            print('Canal máximo.')
        else:
            self.canal += 1
            print(self.canal)

    def diminui_canal(self):
        if self.canal == 1:
            print('Canal mínimo.')
        else:
            self.canal -= 1
            print(self.canal)

    def aumenta_volume(self):
        if self.volume == 10:
            print('Volume máximo.')
        else:
            self.volume += 1
            print(self.volume)

    def diminui_volume(self):
        if self.volume == 0:
            print('Volume mínimo.')
        else:
            self.volume -= 1
            print(self.volume)

# teste da classe

def funcTesteClasse():
    tv1 = Tv(1,5) # canal, volume
    tv1.aumenta_canal()
    tv1.diminui_canal()

    tv1.aumenta_volume()
    tv1.diminui_volume()

funcTesteClasse()