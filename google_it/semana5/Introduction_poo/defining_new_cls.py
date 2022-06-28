# class Apple:
#     color = ""
#     sabor = ""
    
# obj = Apple()
# obj.color = "red"
# obj.sabor = "doce"
# print(obj.color)
# print(obj.sabor)
# print(obj.sabor.upper())

# golden = Apple()
# golden.color = "yellow"
# golden.sabor = "doce"

class Flower:
  color = ""

rose = Flower()
rose.color = "red"
violet = Flower()
violet.color = "blue"

this_pun_is_for_you = "Roses are {}, Violets are {}, ".format(rose.color, violet.color)

print("Roses are {},".format(rose.color))
print("violets are {},".format(violet.color))
print(this_pun_is_for_you) 