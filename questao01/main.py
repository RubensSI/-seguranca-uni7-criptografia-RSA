import rsa

# gerar as chaver publica e privada
# devemos armazanar as chaver para possamos importa
# para uso em outrar partes do código na forma de arquivo


def gerarChaves():

    # criar um arquivo chamado de public.pem
    # salvar os valores das chaves em então
    # criar um fluxo de arquivo chamdo de f

    public_key, private_key = rsa.newkeys(1024)

    with open("./keys/public.pem", "wb") as f:
        f.write(public_key.save_pkcs1("PEM"))

    with open("./keys/private.pem", "wb") as f:
        f.write(private_key.save_pkcs1("PEM"))

# criadas as chaves, a função vai ler as chaves geradas


def carregarChaves():
    with open("./keys/public.pem", "rb") as f:
        public_key = rsa.PublicKey.load_pkcs1(f.read())

    with open("./keys/private.pem", "rb") as f:
        private_key = rsa.PrivateKey.load_pkcs1(f.read())
    return private_key, public_key

# função para criptografar a mensagem
# passando a mensagem e a chave pulica


def criptografar(message, public_key):
    return rsa.encrypt(message.encode('ascii'), public_key)

# função para descriptografar
# pasando a texto cifrado e a chave privada


def descriptografar(texto_cifrado, private_key):
    return rsa.decrypt(texto_cifrado, private_key)


def main():

    gerarChaves()

    private_key, public_key = carregarChaves()

    # recebe a mensagem criptografada
    texto_cifrado = criptografar("Esse texto vai ser criptografado", public_key)

    # recebe a mensagem descriptografada
    texto_decifrado = descriptografar(texto_cifrado, private_key).decode()

    if texto_decifrado:
        print(f'\nTexto criptografado: \n{texto_cifrado}\n')
        print(f'Texto: \n{texto_decifrado}\n')
    else:
        print(f'Não foi possível descriptografar a mensagem.')


main()
