from enum import Enum
from typing import Optional


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

    @classmethod
    def from_str(cls, level: Optional[str]) -> Optional["InsultLevel"]:
        """
        Converte uma string para ``InsultLevel``.

        Aceita ``"light"``, ``"medium"``, ``"heavy"``.
        ``None`` retorna ``None``.
        """
        if level is None:
            return None
        try:
            return cls(level.lower())
        except ValueError:
            raise ValueError(
                f"Nível '{level}' inválido. Use: light, medium, heavy."
            ) from None
