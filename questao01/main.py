from asyncore import write
import rsa

# gerar as chaver publica e privada
# devemos armazanar as chaver para possamos importa
# para uso em outrar partes do código na forma de arquivo
def generateKeys():
# criar um arquivo chamado de public.pem
# salvar os valores das chaves em então 
# criar um fluxo de arquivo chamdo de f
    public_key, private_key = rsa.newkeys(1024)
    with open("public.pem", "wb") as f:
        f.write(public_key.save_pkcs1("PEM"))

    with open("private.pem", "wb") as f:
        f.write(private_key.save_pkcs1("PEM"))

# criadas as chaves, a função vai ler as chaves geradas
def loadKeys(): 
    with open("public.pem", "rb") as f:
        public_key = rsa.PublicKey.load_pkcs1(f.read())

    with open("private.pem", "rb") as f:
        private_key = rsa.PrivateKey.load_pkcs1(f.read())
    return private_key, public_key

# função para criptografar a mensagem
# passando a mensagem e a chave pulica
def encrypt(message, public_key):
    return rsa.encrypt(message.encode('ascii'), public_key)

# função para descriptografar
# pasando a texto cifrado e a chave privada
def decrypt(ciphertext, private_key):
    return rsa.decrypt(ciphertext, private_key)

def main():
    
    private_key, public_key = loadKeys()

    # exibir a mensagem criptografada
    ciphertext = encrypt("Esse texto vai ser criptografado", public_key)

    plaintext = decrypt(ciphertext, private_key)
    
    print("\n")
    print(ciphertext)
    print("\n")
    print(plaintext)

main()


    