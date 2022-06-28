# In Python, a dictionary can only hold a single value for
# a given key. To workaround this, our single value can
# be a list containing multiple values. Here we have
# a dictionary called "wardrobe" with items of clothing
# and their colors. Fill in the blanks to print a line
# for each item of clothing with each color,
# for example: "red shirt", "blue shirt", and so on.
i = 0
wardrobe = {"shirt": ["red", "blue", "white"], "jeans": ["blue", "black"]}
print(wardrobe.items())

for roupas, colors in wardrobe.items(): 
    for color in colors: # acessa a chave atraves do valor para poder executar linha a linha separando os itens da lista.
        print("{} {}".format(color, roupas))


# Folha de dicas sobre métodos de dicionário
# Folha de dicas sobre métodos de dicionário
# Definição

# x = {chave1:valor1, chave2:valor2}

# Operações

# len(dicionário) - Retorna o número de itens no dicionário

# para chave no dicionário - Itera sobre cada chave no dicionário

# for key, value in dictionary.items() - Itera sobre cada par de chave e valor no dicionário

# if key in dictionary - Verifica se a chave está no dicionário

# dicionário[chave] - Acessa o item com chave chave do dicionário

# dicionário[chave] = valor - Define o valor associado à chave

# del dictionary[key] - Remove o item com chave chave do dicionário

# Métodos

# dict.get(key, default) - Retorna o elemento correspondente a key, ou default se não estiver presente

# dict.keys() - Retorna uma sequência contendo as chaves no dicionário

# dict.values() - Retorna uma sequência contendo os valores no dicionário

# dict.update(other_dictionary) - Atualiza o dicionário com os itens provenientes do outro dicionário. As entradas existentes serão substituídas; novas entradas serão adicionadas.

# dict.clear() - Remove todos os itens do dicionário