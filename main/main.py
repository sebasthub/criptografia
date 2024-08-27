from algoritmo_sebas.cripto_agent import Criptografia


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
