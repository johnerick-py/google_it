# Você pode ter uma situação em que duas classes diferentes estão relacionadas, mas não há herança acontecendo.
# Isso é chamado de composição -- onde uma classe faz uso do código contido em outra classe.
# Por exemplo, imagine que temos uma classe Package que representa um pacote de software.
# Ele contém atributos sobre o pacote de software, como nome, versão e tamanho.
# Também temos uma classe Repository que representa todos os pacotes disponíveis para instalação.
# Embora não haja relação de herança entre as duas classes, elas estão relacionadas.
# A classe Repository conterá um dicionário ou lista de Pacotes contidos no repositório.
# Vamos dar uma olhada em um exemplo de definição de classe Repository:


class Repository:
      def __init__(self):
          self.packages = {}
      def add_package(self, package):
          self.packages[package.name] = package
      def total_size(self):
          result = 0
          for package in self.packages.values():
              result += package.size
          return result
          
          
# No método construtor, inicializamos o dicionário de pacotes,
# que conterá os objetos de pacote disponíveis nesta instância do repositório.
# Inicializamos o dicionário no construtor para garantir que cada instância da classe
# Repository tenha seu próprio dicionário.

# Em seguida, definimos o método add_package, que recebe um objeto Package como parâmetro e o adiciona ao nosso dicionário,
# usando o atributo package name como chave.

# Finalmente, definimos um método total_size que calcula o tamanho total de todos os pacotes contidos em nosso repositório.
# Este método itera através dos valores em nosso dicionário de repositório e soma os atributos de tamanho de cada objeto de 
# pacote contido no dicionário, retornando o total no final.
# Neste exemplo, estamos fazendo uso de atributos Package dentro de nossa classe Repository. 
# Também estamos chamando o método values() em nossa instância de dicionário de pacotes.
# A composição nos permite usar objetos como atributos, bem como acessar todos os seus atributos e métodos.