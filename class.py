class Autor:
    def __init__(self, nome, nacionalidade):
        self.__nome = nome
        self.__nacionalidade = nacionalidade
        self.__livrosEscritos = []

    def get_nome(self):
        return self.__nome
    
    def set_nome(self, novoNome):
        self.__nome = novoNome

    def get_nacionalidade(self):
        return self.__nacionalidade
    
    def get_livrosEscritos(self):
        return self.__livrosEscritos

    def criar_livro(self, titulo, autor):
        self.__nomeLivro = titulo
        self.__autor = autor
        self.__livrosEscritos.append(Livro)


class Livro:
    def __init__(self, titulo, autor, ano):
        self.__titulo = titulo
        self.__autor = autor
        self.__ano = ano
        self.__disponibilidade = True
        self.__emprestadoPara = []
        self.__listaDeAutores = []
        
        def adicionarAutores(self, autor):
            self.__listaDeAutores.append(autor)
    
        def removerAutor(self, autor):
        self.__listaDeAutores.remove(autor)

        def consultarAutores(self,):
            for autor in self.__listaDeAutores:

        def get_titulo(self):
            return self.__titulo
        
        def set_titulo(self, novoTitulo):
            self.__titulo = novoTitulo

        def get_autor(self):
            return self.__autor
        
        def set_autor(self, novoAutor):
            self.__autor = novoAutor

        def get_ano(self):
            return self.__ano

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
        self.__bibliotecaAssossiada = None

    def AssossiarBiblioteca(self, biblioteca):
        self.__bibliotecaAssossiada = biblioteca
    
    
    def desassossiarBiblioteca(self):
        self.__bibliotecaAssossiada = None

    def emprestarLivro(self, livro):
        self.__listaDeEmprestimo.append(livro)

    def devolverLivro(self, livro):
        self.__listaDeEmprestimo.remove(livro)

class Biblioteca:
    def __init__(self, nome):
        self.__nome = nome
        self.__listaDeLivros = []
        self.__listaDeUsuarios = []     

    def get_nome(self):
        return self.__nome
    
    def set_nome(self, novoNome):
        self.__nome = novoNome
    
    def adicionarCadastroUsuario(self, usuario):
        self.__listaDeUsuarios.append(usuario)

    def adicionarLivroAoAcervo(self, livro):
        self.__listaDeLivros.append(livro)
    
    def emprestar_livro(livro, usuario):
        if (livro.getDisponibilidade == True):            
            usuario.emprestarLivro(livro)
            livro.emprestarLivro(usuario)


    def devolver_livro(self, livro, usuario):
        if (livro.getDisponibilidade == False):
            usuario.devolverLivro(livro)