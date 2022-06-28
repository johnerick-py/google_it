# Want to try some string methods yourself?
# [Quer experimentar alguns métodos de string você mesmo?]  Give it a go! [Dê uma chance!] 


# Fill in the gaps in the initials function so that it returns the initials of the words contained in the phrase received,
# in upper case.
# [Preencha as lacunas na função iniciais para que ela retorne as iniciais das palavras contidas na frase recebida,
# em maiúsculas.]  For example: "Universal Serial Bus" should return "USB"; "local area network" should return "LAN”.
# [Por exemplo: 'Universal Serial Bus' deve retornar 'USB'; 'rede de área local' deve retornar 'LAN'.] 


def initials(phrase):
    words = phrase.split()
    result = ""
    for word in words:
        result += word[0]
    return result.upper()

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS