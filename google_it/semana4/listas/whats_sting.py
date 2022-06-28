def double_word(word):
    var = word * 2
    return var + str(len(var))

print(double_word('oi'))
# print(double_word("hello")) # Should return hellohello10
# print(double_word("abc"))   # Should return abcabc6
# print(double_word(""))      # Should return 0