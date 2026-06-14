import random
from typing import Optional

from codeinsult.config import InsultLevel
from codeinsult.messages.registry import available_languages, get_provider

_default_lang: str = "pt_br"
_default_level: Optional[InsultLevel] = None


def set_defaults(
    *,
    lang: str = "pt_br",
    level: Optional[str] = None,
) -> None:
    """Configura o idioma e nível de severidade padrão globais.

    Args:
        lang: Idioma padrão (ex: ``"pt_br"``).
        level: Nível de severidade padrão (``"light"``, ``"medium"``,
            ``"heavy"``). ``None`` para usar todos os níveis.

    Example:
        >>> codeinsult.set_defaults(lang="pt_br", level="light")
        >>> codeinsult.insult(404)  # usa pt_br + LIGHT
    """
    global _default_lang, _default_level
    if lang not in available_languages():
        raise ValueError(
            f"Idioma '{lang}' não disponível. Disponíveis: {available_languages()}"
        )
    _default_lang = lang
    _default_level = InsultLevel.from_str(level)


def insult(
    status_code: int,
    *,
    level: Optional[str] = None,
    lang: Optional[str] = None,
) -> str:
    """
    Retorna uma mensagem engraçada para o código de status HTTP informado.

    Args:
        status_code: Código de status HTTP (ex: 200, 404, 500).
        level: Nível de severidade (``"light"``, ``"medium"``, ``"heavy"``).
            Se None, usa TODOS os níveis.
        lang: Idioma (ex: ``"pt_br"``). Se None, usa ``"pt_br"``.
    """
    parsed_level = InsultLevel.from_str(level) if level is not None else _default_level
    lang = lang if lang is not None else _default_lang

    provider = get_provider(lang)
    messages = provider.get_messages(status_code, parsed_level)

    if not messages:
        if parsed_level is None:
            messages = []
            for lvl in InsultLevel:
                messages.extend(provider.catalog.default_messages.get(lvl, []))
        else:
            messages = provider.catalog.default_messages.get(
                parsed_level, ["Erro desconhecido."]
            )

    if not messages:
        return f"Status {status_code}: sem mensagem disponível."
    return random.choice(messages)


def random_insult(
    *,
    level: Optional[str] = None,
    lang: Optional[str] = None,
) -> str:
    """
    Retorna uma mensagem aleatória de qualquer status code disponível.

    Args:
        level: Nível de severidade (``"light"``, ``"medium"``, ``"heavy"``).
            Se None, usa TODOS os níveis.
        lang: Idioma (ex: ``"pt_br"``). Se None, usa ``"pt_br"``.
    """
    parsed_level = InsultLevel.from_str(level) if level is not None else _default_level
    lang = lang if lang is not None else _default_lang

    provider = get_provider(lang)
    catalog = provider.catalog

    # Coleta todas as mensagens
    all_msgs: list[str] = []
    if parsed_level is None:
        for code_msgs in catalog.messages.values():
            for lvl in InsultLevel:
                all_msgs.extend(code_msgs.get(lvl, []))
    else:
        for code_msgs in catalog.messages.values():
            all_msgs.extend(code_msgs.get(parsed_level, []))

    if not all_msgs:
        if parsed_level is None:
            for lvl in InsultLevel:
                all_msgs.extend(catalog.default_messages.get(lvl, []))
        else:
            all_msgs = catalog.default_messages.get(parsed_level, ["Nada a declarar."])
    return random.choice(all_msgs)
