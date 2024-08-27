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


if __name__ == '__main__':
    plainText = "amanhecer no campo e sempre um espetaculo de cores e sons onde anatureza desperta com suavidade"
    chave = "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk"
    chaveDois = "sasdasdasadassfasfsaasdasdaksdajsdasdasdahsdgasdasfddasdassdassdasdasdassdasdasdassdassdasdsada"
    cripto = Criptografia()
    encriptado = cripto.codificar(chave, plainText)
    if e := encriptado['e']:
        if isinstance(e, ValueError):
            exit('Algum caracter especial ou numero no texto')
        elif isinstance(e, IndexError):
            exit('A chave não tem o mesmo tamanho do texto')
        else:
            exit(f'Erro inesperado "{e}"')
    decriptadoErrado = cripto.descodificar(chaveDois, encriptado['y'])
    if e := decriptadoErrado['e']:
        if isinstance(e, ValueError):
            exit('Algum caracter especial ou numero no texto')
        elif isinstance(e, IndexError):
            exit('A chave não tem o mesmo tamanho do texto')
        else:
            exit(f'Erro inesperado "{e}"')
    decriptado = cripto.descodificar(chave, encriptado['y'])
    if e := decriptado['e']:
        if isinstance(e, ValueError):
            exit('Algum caracter especial ou numero no texto')
        elif isinstance(e, IndexError):
            exit('A chave não tem o mesmo tamanho do texto')
        else:
            exit(f'Erro inesperado "{e}"')
    print('-----------------------------------codificação normal-----------------------------------')
    print(encriptado['y'])
    print(decriptadoErrado['p'])
    print(decriptado['p'])
    print('-----------------------------------codificação avançada-----------------------------------')
    dicionario = cripto.codificar_avancado(plainText)
    if e := dicionario['e']:
        if isinstance(e, ValueError):
            exit('Algum caracter especial ou numero no texto')
        elif e:
            exit(f'Erro inesperado "{e}"')
    print(''.join(dicionario['y']))
    print(''.join(dicionario['k']))
    print(''.join(cripto.descodificar(''.join(dicionario['k']), ''.join(dicionario['y']))['p']))
