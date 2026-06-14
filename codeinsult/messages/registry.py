from codeinsult.messages.base import BaseMessageProvider

_registry: dict[str, BaseMessageProvider] = {}


def register_provider(provider_cls: type[BaseMessageProvider]) -> None:
    """
    Registra um novo provider de idioma.

    Exemplo:
        class EnUSProvider(BaseMessageProvider):
            ...

        register_provider(EnUSProvider)
    """
    if not issubclass(provider_cls, BaseMessageProvider):
        raise TypeError(f"{provider_cls} must be a subclass of BaseMessageProvider")
    _registry[provider_cls.lang_code()] = provider_cls()


def get_provider(lang: str) -> BaseMessageProvider:
    """Retorna o provider para o idioma especificado."""
    if lang not in _registry:
        raise ValueError(
            f"Idioma '{lang}' não encontrado. "
            f"Idiomas disponíveis: {list(_registry.keys())}. "
            f"Use register_provider() para adicionar um novo idioma."
        )
    return _registry[lang]


def available_languages() -> list[str]:
    """Lista os idiomas disponíveis."""
    return list(_registry.keys())
