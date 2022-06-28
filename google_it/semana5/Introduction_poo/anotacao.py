# Depois de ter o dicionário, use este código para gerar a imagem da nuvem de palavras:

cloud = wordcloud.WordCloud()
cloud.generate_from_frequencies(frequencies)
cloud.to_file("myfile.jpg")

# Coisas para lembrar 
# Antes de processar qualquer texto, você precisa remover todos os sinais de pontuação.
# Para fazer isso, você pode percorrer cada linha de texto, caractere por caractere, usando o método isalpha() .
# Isso verificará se o caractere é ou não uma letra.

# Para dividir uma linha de texto em palavras, você pode usar o método split() .

# Antes de armazenar palavras no dicionário de frequência,
# verifique se elas fazem parte do conjunto de palavras "desinteressante"
# (por exemplo: "a", "o", "para", "se"). Faça isso definir um parâmetro para
# sua função para que você possa alterá-lo, se necessário.

# Arquivo de entrada
# Para o arquivo de entrada, você precisa fornecer um arquivo que contenha apenas texto.
# Para o texto em si, você pode copiar e colar o conteúdo de um site de sua preferência.
# Ou você pode usar um site como o Project Gutenberg para encontrar livros disponíveis online.
# Você pode ver que nuvens de palavras você pode obter de livros famosos,
# como uma peça de Shakespeare ou um romance de Jane Austen.