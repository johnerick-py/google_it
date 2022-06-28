

# Remember our Person class from the last video? [Lembra da nossa aula Pessoa do último vídeo?]
# Let’s add a docstring to the greeting method. [Vamos adicionar uma docstring ao método de saudação.]  How about, 
# “Outputs a message with the name of the person”. [Que tal, “Exibe uma mensagem com o nome da pessoa”.] 

class Person:
  def __init__(self, name):
    self.name = name
  def greeting(self):
    ''' Outputs a message with the name of the person '''
    print("Hello! My name is {name}.".format(name=self.name)) 

help(Person)


# Here is your output:
# Help on class Person in module submission:

# class Person(builtins.object)
#  |  Methods defined here:
#  |  
#  |  __init__(self, name)
#  |      Initialize self.  See help(type(self)) for accurate signature.
#  |  
#  |  greeting(self)
#  |      Outputs a message with the name of the person
#  |  
#  |  ----------------------------------------------------------------------
#  |  Data descriptors defined here:
#  |  
#  |  __dict__
#  |      dictionary for instance variables (if defined)
#  |  
#  |  __weakref__
#  |      list of weak references to the object (if defined)


# Excellent! You’ve mastered the art of providing info using
# docstrings!