class Criptografia:
    def __init__(self):
        self.alfabeto = [chr(i) for i in range(ord('a'), ord('z') + 1)] + [' ']

    def codificar(self, k: str, p: str) -> list[str]:
        codificado = [
            self.letra_por_posicao(self.get_indice(p[i]) + self.get_indice(k[i]))
            for i in range(len(p))
        ]
        return codificado

    def descodificar(self, k: str, y: str) -> list[str]:
        return [
            self.letra_por_posicao(self.get_indice(y[i]) - self.get_indice(k[i]))
            for i in range(len(y))
        ]

    def str_para_indices(self, string: str) -> list[int]:
        return [self.get_indice(s) for s in string]

    def letra_por_posicao(self, numero: int) -> str:
        # Corrigir o cálculo do índice
        indice = numero % len(self.alfabeto)
        return self.alfabeto[indice]

    def get_indice(self, letra: str) -> int:
        return self.alfabeto.index(letra)



if __name__ == '__main__':
    plainText = "amanhecer no campo e sempre um espetaculo de cores e sons onde anatureza desperta com suavidade"
    chave     = "xkcoaxbkcttawzxdvssmfjdnrbhgrqkhmfrgywknkjjvkjyaxxmkftqluyxjckzsfshfcwqqcztwkwiidxsnfarqshasdae"
    chaveDois = "sasdasdasadassfasfsaasdasdaksdajsdasdasdahsdgasdasfddasdassdassdasdasdassdasdasdassdassdasdsada"
    cripto = Criptografia()
    encriptado = ''.join(cripto.codificar(chave, plainText))
    decriptadoErrado = ''.join(cripto.descodificar(chaveDois, encriptado))
    decriptado = ''.join(cripto.descodificar(chave, encriptado))
    print(cripto.alfabeto)
    print(cripto.str_para_indices(plainText))
    print(encriptado)
    print(decriptadoErrado)
    print(decriptado)
