from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Definição das classes Pergunta e Resposta
class Pergunta:
    def __init__(self, id, texto):
        self.id = id
        self.texto = texto


class Resposta:
    def __init__(self, id, texto, pergunta_id):
        self.id = id
        self.texto = texto
        self.pergunta_id = pergunta_id


class BancoDeDadosQA:
    def __init__(self):
        self.perguntas = []
        self.respostas = []

    def adicionar_pergunta(self, pergunta):
        self.perguntas.append(pergunta)

    def adicionar_resposta(self, resposta):
        self.respostas.append(resposta)

    def encontrar_resposta(self, pergunta_texto):
        # Verificar se há perguntas e respostas
        if not self.perguntas or not self.respostas:
            return None

        # Criação de uma lista com textos de perguntas e respostas
        textos = [p.texto for p in self.perguntas] + [r.texto for r in self.respostas]

        # Utilizando TF-IDF para representar textos
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(textos)

        # Extraindo o vetor da pergunta do usuário
        pergunta_vector = vectorizer.transform([pergunta_texto])
        respostas_vectors = tfidf_matrix[len(self.perguntas):]  # Vetores de respostas

        # Cálculo da similaridade
        similaridades = cosine_similarity(pergunta_vector, respostas_vectors).flatten()

        # Verificando a melhor correspondência
        melhor_correspondencia = similaridades.argmax()
        if similaridades[melhor_correspondencia] > 0:
            return self.respostas[melhor_correspondencia]
        return None


# Criando o banco de dados de perguntas e respostas
banco = BancoDeDadosQA()

# Adicionando perguntas
banco.adicionar_pergunta(Pergunta(1, "Qual é a capital da França?"))
banco.adicionar_pergunta(Pergunta(2, "Quem escreveu 'Dom Casmurro'?"))

# Adicionando respostas
banco.adicionar_resposta(Resposta(1, "A capital da França é Paris.", 1))
banco.adicionar_resposta(Resposta(2, "Machado de Assis escreveu 'Dom Casmurro'.", 2))

# Loop para permitir que o usuário faça perguntas
while True:
    pergunta_usuario = input("\nDigite sua pergunta (ou 'sair' para encerrar): ")
    if pergunta_usuario.lower() == 'sair':
        print("Encerrando o programa.")
        break

    resposta_encontrada = banco.encontrar_resposta(pergunta_usuario)

    if resposta_encontrada:
        print(f"Resposta encontrada: {resposta_encontrada.texto}")
    else:
        print("Nenhuma resposta encontrada.")
