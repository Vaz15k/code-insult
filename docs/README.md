# CodeInsult

> **Turn errors into laughter.** A Python library that maps HTTP status codes to funny, sarcastic, and offensive messages — from "cult reference" to "heavy insult" levels.

> **English 🇺🇸** | [Português 🇧🇷](docs/README.pt.md)

[![PyPI](https://img.shields.io/pypi/v/codeinsult?color=blue)](https://pypi.org/project/codeinsult/)
[![Python](https://img.shields.io/pypi/pyversions/codeinsult)](https://www.python.org/)
[![Downloads](https://img.shields.io/pypi/dm/codeinsult)](https://pypi.org/project/codeinsult/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

---

## Installation

```bash
pip install codeinsult
```

> *Requires Python 3.11 or higher.*

---

## Usage

```python
import codeinsult

# Get a message for a status code
print(codeinsult.insult(404))
# "404: O recurso sumiu. Como meias na máquina de lavar."

# With severity level ("light", "medium", "heavy")
print(codeinsult.insult(500, level="heavy"))
# "DEU MERDA NO SERVIDOR! Não foi você, foi a gente. Mas foi você também."

# A completely random message
print(codeinsult.random_insult())
# "418 I'm a Teapot: Sou um bule, não uma cafeteira. Respeita minha profissão!"

# Configure global defaults
codeinsult.set_defaults(lang="pt_br", level="light")
print(codeinsult.insult(401))
# "401 Unauthorized: Você não vai passar! — Gandalf, Servidor Edition."
```

---

## Severity Levels

| Level      | Description                                                  | Example                                                                             |
| ---------- | ------------------------------------------------------------ | ----------------------------------------------------------------------------------- |
| `LIGHT`  | References to movies, series, books, and memes. No swearing. | *"404: Procurei em toda galáxia e não achei. — Baby Yoda."*                    |
| `MEDIUM` | Sarcasm and irony. Mildly offensive language.                | *"500: O servidor teve um treco. Tenta de novo quando ele se recuperar."*         |
| `HEAVY`  | Heavy insults, with explicit swear words and profanity.      | *"400: QUE REQUEST DE MERDA É ESSE? Nem o Google Tradutor salva essa bagunça!"* |

---

## Development

```bash
# Clone the repository
git clone https://github.com/Vaz15k/code-insult.git
cd code-insult

# Install dev dependencies
pip install -e ".[dev]"

# Run the tests
pytest tests/ -v
```

---

## Contributing

Contributions are very welcome! Some ideas:

- 🗣️ **Add new languages** — Spanish, French, etc.
- 💬 **Add more phrases** for existing status codes (Be Creative)
- 🐛 **Fix bugs** or improve documentation
- 📦 **New status codes** that don't have messages yet

To contribute:

1. Fork the project
2. Create a branch for your feature
3. Add your messages and tests
4. Submit a Pull Request
