def process_phrase(phrase):
    """
    Processa uma frase fornecida pelo usuário, realizando diversas operações.

    Args:
        phrase: A frase a ser processada.

    Returns:
        Uma string formatada com os resultados das operações, ou uma mensagem de erro.
    """
    if not phrase:
        return "Erro: A frase não pode estar vazia."

    num_chars = len(phrase)
    words = phrase.split()
    num_words = len(words)
    longest_word = max(words, key=len, default="")

    reversed_chars = phrase[::-1]
    reversed_words = " ".join(reversed(words))

    upper_phrase = phrase.upper()
    lower_phrase = phrase.lower()

    words_tuple = tuple(words)

    return f"""
    Análise da Frase:

    1. Número de caracteres: {num_chars}
    2. Número de palavras: {num_words}
    3. Maior palavra: {longest_word}
    4. Frase invertida (caracteres): {reversed_chars}
    5. Frase invertida (palavras): {reversed_words}
    6. Frase em maiúsculas: {upper_phrase}
    7. Frase em minúsculas: {lower_phrase}
    8. Tupla de palavras: {words_tuple}
    """

# Exemplo de uso
user_phrase = input("Digite uma frase: ")
result = process_phrase(user_phrase)
result
