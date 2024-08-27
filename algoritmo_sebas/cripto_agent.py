import random


class Criptografia:
    def __init__(self):
        self.alfabeto = [chr(i) for i in range(ord('a'), ord('z') + 1)] + [' ']


    def codificar(self, k: str, p: str) -> dict[str, str or Exception]:
        try:
            y: list[str] = [
                self.letra_por_posicao(self.get_indice(p[i]) + self.get_indice(k[i]))
                for i in range(len(p))
            ]
            return {'y': ''.join(y), 'e': None}
        except Exception as execao:
            return {'y': None, 'e': execao}


    def codificar_avancado(self, p: str) -> dict[str,list[str] or Exception]:
        k: list[str] = []
        y: list[str] = []
        letras: list[str] = []
        try:
            for char in p:
                letras.append(char)
                caos: int = random.randint(1, 24)
                quantidade: int = letras.count(char)
                letra_chave: int = caos * (quantidade + 1)
                k.append(self.letra_por_posicao(letra_chave))
                y.append(self.letra_por_posicao(self.get_indice(char) + letra_chave))
        except Exception as execao:
            return {'e': execao}
        return { 'y': y, 'k': k, 'e': None}


    def descodificar(self, k: str, y: str) -> dict[str, str or Exception]:
        try:
            p = ''.join([
                self.letra_por_posicao(self.get_indice(y[i]) - self.get_indice(k[i]))
                for i in range(len(y))
            ])
            return {'p': p, 'e': None}
        except Exception as execao:
            return {'p': None, 'e': execao}


    def str_para_indices(self, string: str) -> list[int]:
        return [self.get_indice(s) for s in string]


    def letra_por_posicao(self, numero: int) -> str:
        indice = numero % len(self.alfabeto)
        return self.alfabeto[indice]


    def get_indice(self, letra: str) -> int:
        return self.alfabeto.index(letra)
