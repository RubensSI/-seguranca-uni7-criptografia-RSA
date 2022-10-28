import rsa

def descriptografar(texto_cifrado, private_key):
    return rsa.decrypt(texto_cifrado, private_key)

def carregarChaves():
    with open("./keys/public.pem", "rb") as f:
        public_key = rsa.PublicKey.load_pkcs1(f.read())

    with open("./keys/private.pem", "rb") as f:
        private_key = rsa.PrivateKey.load_pkcs1(f.read())
    return private_key, public_key

private_key, public_key = carregarChaves()

mensagem = open("./mensagem/texto", "rb").read()