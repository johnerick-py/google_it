# Creating new instances of class objects can be a great way to keep track of values using attributes
# associated with the object.
# The values of these attributes can be easily changed at the object level.
# The following code illustrates a famous quote by George Bernard Shaw, using objects to represent people.
# Fill in the blanks to make the code satisfy the behavior described in the quote.

# “Se você tem uma maçã e eu tenho uma maçã e nós trocamos essas maçãs então
# você e eu ainda teremos uma maçã. Mas se você tem uma ideia e eu tenho
# uma ideia e trocamos essas ideias, então cada um de nós terá duas ideias.”
# George Bernard Shaw

# class Person:
#     apples = 0
#     ideas = 0

# johanna = Person()
# johanna.apples = 1
# johanna.ideas = 1

# martin = Person()
# martin.apples = 2
# martin.ideas = 1

# def exchange_apples(you, me):
#     #Aqui, apesar de G.B. Citação de Shaw, nossos personagens começaram com #diferentes quantidades de maçãs para que possamos observar melhor os resultados.
#     #Vamos fazer com que Martin e Johanna troquem TODAS as maçãs um com o outro.
#     #Dica: como você mudaria os valores das variáveis,
#     #para que "você" e "eu" troquem TODAS as maçãs entre si?
#     #Você precisa de uma variável temporária para armazenar um dos valores?
#     #Você pode precisar de mais de uma linha de código para fazer isso, o que está OK.
#     temp= you.apples
#     you.apples = me.apples
#     me.apples = temp
#     return you.apples, me.apples

# def exchange_ideas(you, me):
#     #"você" e "eu" compartilharão nossas ideias um com o outro.
#     #Quais operações precisam ser executadas, para que cada objeto receba
#     #o número de ideias compartilhadas?
#     #Dica: como você atribuiria o número total de ideias para
#     #cada atributo de ideia? Você precisa de uma variável temporária para armazenar
#     #a soma das ideias, ou você consegue encontrar outro caminho?
#     #Use quantas linhas de código forem necessárias aqui.
#     you.ideas = me.ideas + you.ideas
#     me.ideas = you.ideas
#     return you.ideas, me.ideas

# exchange_apples(johanna, martin)
# print("Johanna has {} apples and Martin has {} apples".format(johanna.apples, martin.apples))
# exchange_ideas(johanna, martin)
# print("Johanna has {} ideas and Martin has {} ideas".format(johanna.ideas, martin.ideas))


# Pergunta 3
# The City class
# has the following attributes: name, country (where the city is located), elevation (measured in meters),
# and population (approximate, according to recent statistics). Fill in the blanks of the max_elevation_city
# function to return the name of the city and its country (separated by a comma), when comparing the 3 defined instances
# for a specified minimal population. For example,
# calling the function for a minimum population of 1 million: max_elevation_city(1000000) should return "Sofia, Bulgaria".

# define a basic city class
class City:
	name = ""
	country = ""
	elevation = 0
	population = 0


# create a new instance of the City class and
# define each attribute
city1 = City()
city1.name = "Cusco"
city1.country = "Peru"
city1.elevation = 3399
city1.population = 358052

# create a new instance of the City class and
# define each attribute
city2 = City()
city2.name = "Sofia"
city2.country = "Bulgaria"
city2.elevation = 2290
city2.population = 1241675

# create a new instance of the City class and
# define each attribute
city3 = City()
city3.name = "Seoul"
city3.country = "South Korea"
city3.elevation = 38
city3.population = 9733509


def max_elevation_city(min_population):
	# Initialize the variable that will hold 
# the information of the city with 
# the highest elevation 
	return_city = City()

	# Evaluate the 1st instance to meet the requirements:
	# does city #1 have at least min_population and
	# is its elevation the highest evaluated so far?
	if city1.population >= min_population:
		return_city = city1
	# Evaluate the 2nd instance to meet the requirements:
	# does city #2 have at least min_population and
	# is its elevation the highest evaluated so far?
	if city2.population >= min_population and city2.elevation > return_city.elevation:
		return_city = city2
	# Evaluate the 3rd instance to meet the requirements:
	# does city #3 have at least min_population and
	# is its elevation the highest evaluated so far?
	if city3.population >= min_population and city3.elevation > return_city.elevation:
		return_city = city3

	#Format the return string
	if return_city.name:
		return f"{return_city.name}, {return_city.country}"
	else:
		return ""

print(max_elevation_city(100000)) # Should print "Cusco, Peru"
print(max_elevation_city(1000000)) # Should print "Sofia, Bulgaria"
print(max_elevation_city(10000000)) # Should print ""