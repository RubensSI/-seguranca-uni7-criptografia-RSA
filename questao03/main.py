import rsa

# função usada para gerar chaves aleatórias
def gerarChaves():

    # criar um arquivo chamado de public.pem
    # salvar os valores das chaves em então
    # criar um fluxo de arquivo chamdo de f

    public_key, private_key = rsa.newkeys(1024)
    
    with open("./keys/public.pem", "wb") as f:
        f.write(public_key.save_pkcs1("PEM"))

    with open("./keys/private.pem", "wb") as f:
        f.write(private_key.save_pkcs1("PEM"))

# gera aquivo de texto
def gerarArquivoTexto():
    message = "Texto que vai ser criptografado!"

    with open(f"./mensagem/texto", "wb") as f:
        f.write(message.encode())

# carregar as chaver
def carregarChaves():
    with open("./keys/public.pem", "rb") as f:
        public_key = rsa.PublicKey.load_pkcs1(f.read())

    with open("./keys/private.pem", "rb") as f:
        private_key = rsa.PrivateKey.load_pkcs1(f.read())
    return private_key, public_key

# criptografar a mensagem
def criptografar(message, public_key):
    return rsa.encrypt(message, public_key)


# comando usado para gerar as chaver puplica e privada
#generateKeys()

# comando usado para gerar a mensagem
#gerarArquivoTexto()

# recuperar as chaves
private_key, public_key = carregarChaves()
mensagem = open("./mensagem/texto", "rb").read()
mensagem_criptografada = criptografar(mensagem, public_key)

assinatura = rsa.sign(mensagem_criptografada, private_key, "SHA-256")

with open("./assinatura/assinatura", "wb") as f:
    f.write(assinatura)

with open(f"./mensagem/texto_assinado", "wb") as f:
    f.write(mensagem_criptografada)
