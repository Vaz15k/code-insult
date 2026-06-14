# codeinsult/__init__.py
from codeinsult.__version__ import __version__
from codeinsult.CodeInsult import insult, random_insult, set_defaults
from codeinsult.config import InsultLevel
from codeinsult.messages.registry import available_languages

__all__ = [
    "__version__",
    "insult",
    "random_insult",
    "set_defaults",
    "available_languages",
    "InsultLevel",
]
