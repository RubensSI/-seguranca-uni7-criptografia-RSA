from asyncore import write
import rsa

# gerar as chaver publica e privada
public_key, private_key = rsa.newkeys(1024)

# devemos armazanar as chaver para possamos importa
# para uso em outrar partes do código na forma de arquivo

# criar um arquivo chamado de public.pem
# salvar os valores das chaves em então 
# criar um fluxo de arquivo chamdo de f

# with open("public.pem", "wb") as f:
#     f.write(public_key.save_pkcs1("PEM"))

# with open("private.pem", "wb") as f:
#     f.write(private_key.save_pkcs1("PEM"))

# criadas as chaves, a função vai ler as chaves geradas 
with open("public.pem", "rb") as f:
    public_key = rsa.PublicKey.load_pkcs1(f.read())

with open("private.pem", "rb") as f:
    private_key = rsa.PrivateKey.load_pkcs1(f.read())

# mensagem a ser criptografada
mensagem = "Hello my passwold is neural_nine999"

mensagem_criptografada = rsa.encrypt(mensagem.encode(), public_key)

# exibir a mensagem criptografada
print(mensagem_criptografada)

# escrever a mensagem em um arquivo para depois fazewr a leitura
# with open("encrypted.message", "wb") as f:
#     f.write(mensagem_criptografada)

# ler mansawgem do arquivo gerado
mensagem_criptografada = open("encrypted.message", "rb").read()

# descriptografar a mensagem usando decrypt do RSA
plaintext = rsa.decrypt(mensagem_criptografada, private_key)

print(plaintext)


    