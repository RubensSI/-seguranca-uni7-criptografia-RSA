import rsa

def descriptografar(texto_cifrado, private_key):
    return rsa.decrypt(texto_cifrado, private_key)

def carregarChaves():
    try: 
        with open("./keys/public.pem", "rb") as f:
            public_key = rsa.PublicKey.load_pkcs1(f.read())

        with open("./keys/private.pem", "rb") as f:
            private_key = rsa.PrivateKey.load_pkcs1(f.read())
    except:
        print("Não foi possivel carregar o arquivo!")

    return private_key, public_key

def carregarAssinatura():
    try:
        with open("./assinatura/assinatura", "rb") as f:
            assinatura = f.read()
    except:
        print("Não foi possível carregar o arquivo!")
    return assinatura

def main():

    private_key, public_key = carregarChaves()

    assinatura = carregarAssinatura()

    mensagem = open("./mensagem/texto_assinado", "rb").read()

    if rsa.verify(mensagem, assinatura, public_key):
        print(f'Assinatura Válida!')
        texto = descriptografar(mensagem, private_key)
        print(f'Texto: {texto.decode()}')
    else:
        print("Assinatura Válida!")

main()

