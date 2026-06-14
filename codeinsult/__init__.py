# codeinsult/__init__.py
import codeinsult.messages.pt_br  # noqa: F401, F811
from codeinsult.__version__ import __version__
from codeinsult.CodeInsult import insult, random_insult, set_defaults
from codeinsult.messages.registry import available_languages

__all__ = [
    "__version__",
    "insult",
    "random_insult",
    "set_defaults",
    "available_languages",
]
