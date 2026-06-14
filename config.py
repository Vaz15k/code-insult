from enum import Enum


class InsultLevel(Enum):
    """
    Níveis de severidade das mensagens.

    LIGHT  — Referências leves a filmes, séries, livros, memes. Sem palavrões.
    MEDIUM — Sarcasmo e ironia. Pode conter linguagem levemente ofensiva.
    HEAVY  — Insultos pesados, com palavrões e xingamentos explícitos.
    """

    LIGHT = "light"
    MEDIUM = "medium"
    HEAVY = "heavy"
