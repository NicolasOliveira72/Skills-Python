import hashlib

line = "="
print(line*30)
# Algoritmos disponíveis:
'''print(hashlib.algorithms_available) '''

print(line*30)
# Algoritmos disponíveis de acordo com o so:
'''print(hashlib.algorithms_guaranteed)'''

# SHA256() para criptografar uma string:

algo = hashlib.sha3_256()
print(algo.digest())
print(line*30)
sms = "É necessário ter desejado a morte para valorizar a vida".encode()
algo.update(sms)
print(algo.hexdigest())

