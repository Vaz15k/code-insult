from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Dict, List, Optional

from config import InsultLevel


@dataclass
class MessageCatalog:
    """
    Catálogo de mensagens para um idioma.

    Estrutura:
        messages[status_code][InsultLevel] = [lista de frases]
    """

    lang: str
    lang_name: str
    messages: Dict[int, Dict[InsultLevel, List[str]]] = field(default_factory=dict)
    default_messages: Dict[InsultLevel, List[str]] = field(default_factory=dict)

    def get_messages(self, status_code: int, level: Optional[InsultLevel]) -> List[str]:
        """
        Retorna as mensagens para um status code e nível.
        Se level for None, retorna mensagens de TODOS os níveis.
        Se não houver mensagens específicas, retorna as padrão.
        """
        if level is None:
            # Coleta mensagens de todos os níveis
            code_msgs = self.messages.get(status_code, {})
            msgs: List[str] = []
            for lvl in InsultLevel:
                msgs.extend(code_msgs.get(lvl, []))
            if not msgs:
                for lvl in InsultLevel:
                    msgs.extend(self.default_messages.get(lvl, []))
            return msgs

        code_msgs = self.messages.get(status_code, {})
        msgs = code_msgs.get(level, [])
        if not msgs:
            msgs = self.default_messages.get(level, [])
        return msgs

    def has_messages(self, status_code: int, level: Optional[InsultLevel]) -> bool:
        """Verifica se existem mensagens para o status e nível."""
        if level is None:
            code_msgs = self.messages.get(status_code, {})
            return any(code_msgs.get(lvl, []) for lvl in InsultLevel)
        return bool(self.messages.get(status_code, {}).get(level, []))


class BaseMessageProvider(ABC):
    """
    Provider abstrato — cada idioma implementa um provider concreto.

    Para adicionar um novo idioma:

        class EnUSProvider(BaseMessageProvider):
            @property
            def catalog(self) -> MessageCatalog:
                return _EN_US_CATALOG
    """

    @property
    @abstractmethod
    def catalog(self) -> MessageCatalog:
        """Retorna o catálogo de mensagens para este idioma."""
        ...

    @classmethod
    @abstractmethod
    def lang_code(cls) -> str:
        """Código do idioma (ex: 'pt_BR', 'en_US')."""
        ...

    def get_messages(self, status_code: int, level: Optional[InsultLevel]) -> List[str]:
        return self.catalog.get_messages(status_code, level)
