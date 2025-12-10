# Módulo Regex:

import re

# Verificando os indices iniciais e finais da string:

'''text = "Aprendendo python"
x = re.search(r'endo', text)
print(f"Indice Final: {x.start()}")
print(f"Índice Inicial: {x.end()}")'''

# Verificando se a string possui o ponto:

'''site = 'https://python.com'
match = re.search(r'\.', site)
print(match)'''

# Buscando a lista de caracteres dentro de uma frase:

text = "Aprendendo python"
lists = "[a-g]"
vr2 = re.findall(lists, text)
print(vr2)
