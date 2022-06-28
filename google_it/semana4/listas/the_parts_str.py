# Want to give it a go yourself? 
# [Quer dar uma chance você mesmo?]
# Be my guest! [Seja meu convidado!]
# Modify the first_and_last function so that it returns True if the first letter of the string is the same as the last
# letter of the string, False if they’re different.
# [Modifique a função first_and_last para que ela retorne True se a primeira letra da string for
# igual à última letra da string, False se forem diferentes.]
# Remember that you can access characters using message[0] or message[-1].
# [Lembre-se de que você pode acessar os personagens usando message[0] ou message[-1].] 
# Be careful how you handle the empty string, which should return True since nothing is equal to nothing.
# [Tenha cuidado como você lida com a string vazia, que deve retornar True, pois nada é igual a nada.] 


def first_and_last(message):

    var = message
    
    while var != "":
        if var[0] == var[-1]:
            return True
        elif var[0] != var[-1]:
            return False
    if var == "":
            return True

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))