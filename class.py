class Livro:
    __id = 0
    
    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor = autor
        self.__meuID = Livro.__id
        self.__disponibilidade = True
        self.__emprestadoPara = []
        Livro.__id += 1

        def get_titulo(self):
            return self.__titulo
        
        def set_titulo(self, novoTitulo):
            self.__titulo = novoTitulo

        def get_autor(self):
            return self.__autor
        
        def set_autor(self, novoAutor):
            self.__autor = novoAutor

        def get_Id(self):
            return self.__id

        def get_Disponibilidade(self):
            return self.__disponibilidade

        def set_Disponibilidade(self, novaDisponibilidade):
            self.__disponibilidade = novaDisponibilidade

        def emprestarLivro(usuario):
            self.__emprestadoPara.append(usuario)
            self.set_Disponibilidade(False)    

class Usuario:
    def __init__(self, nome, matricula, livrosEmprestados):
        self.nome = nome
        self.__matricula = matricula
        self.emprestados = livrosEmprestados
        self.__listaDeEmprestimo = []
    
    def emprestarLivro(self, livro):
        self.__listaDeEmprestimo.append(livro)

    def devolverLivro(self, livro):
        self.__listaDeEmprestimo.remove(livro)

class Biblioteca:
    def __init__(self):
        self.__listaDeLivros = []        
    
    def adicionarLivroAoAcervo(self, livro):
        self.__listaDeLivros.append(livro)
    
    def emprestar_livro(livro, usuario):
        if (livro.getDisponibilidade == True):            
            usuario.emprestarLivro(livro)
            livro.emprestarLivro(usuario)


    def devolver_livro(self, livro):
