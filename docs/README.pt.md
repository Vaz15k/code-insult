# CodeInsult

> **Transforme erros em risadas.** Uma biblioteca Python que mapeia códigos de status HTTP para mensagens engraçadas, sarcásticas e ofensivas — do nível "referência cult" ao "insulto pesado".

> [English 🇺🇸](docs/README.md) | **Português 🇧🇷**

[![PyPI](https://img.shields.io/pypi/v/codeinsult?color=blue)](https://pypi.org/project/codeinsult/)
[![Python](https://img.shields.io/pypi/pyversions/codeinsult)](https://www.python.org/)
[![Downloads](https://img.shields.io/pypi/dm/codeinsult)](https://pypi.org/project/codeinsult/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

---

## Instalação

```bash
pip install codeinsult
```

> *Requer Python 3.11 ou superior.*

---

## Uso

```python
import codeinsult

# Mensagem para um status code
print(codeinsult.insult(404))
# "404: O recurso sumiu. Como meias na máquina de lavar."

# Com nível de severidade ("light", "medium", "heavy")
print(codeinsult.insult(500, level="heavy"))
# "DEU MERDA NO SERVIDOR! Não foi você, foi a gente. Mas foi você também."

# Mensagem completamente aleatória
print(codeinsult.random_insult())
# "418 I'm a Teapot: Sou um bule, não uma cafeteira. Respeita minha profissão!"

# Configurar padrões globais
codeinsult.set_defaults(lang="pt_br", level="light")
print(codeinsult.insult(401))
# "401 Unauthorized: Você não vai passar! — Gandalf, Servidor Edition."
```

---

## Níveis de severidade

| Nível     | Descrição                                                     | Exemplo                                                                             |
| ---------- | --------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `LIGHT`  | Referências a filmes, séries, livros e memes. Sem palavrões. | *"404: Procurei em toda galáxia e não achei. — Baby Yoda."*                    |
| `MEDIUM` | Sarcasmo e ironia. Linguagem levemente ofensiva.                | *"500: O servidor teve um treco. Tenta de novo quando ele se recuperar."*         |
| `HEAVY`  | Insultos pesados, com palavrões e xingamentos explícitos.     | *"400: QUE REQUEST DE MERDA É ESSE? Nem o Google Tradutor salva essa bagunça!"* |

---

## Desenvolvimento

```bash
# Clonar o repositório
git clone https://github.com/Vaz15k/code-insult.git
cd code-insult

# Instalar dependências de desenvolvimento
pip install -e ".[dev]"

# Rodar os testes
pytest tests/ -v
```

---

## Contribuindo

Contribuições são muito bem-vindas! Algumas ideias:

- 🗣️ **Adicionar novos idiomas** — espanhol, francês, etc.
- 💬 **Adicionar mais frases** para status codes existentes (Seja Criativo)
- 🐛 **Corrigir bugs** ou melhorar a documentação
- 📦 **Novos status codes** que ainda não têm mensagens

Para contribuir:

1. Faça um fork do projeto
2. Crie uma branch para sua feature
3. Adicione suas mensagens e testes
4. Envie um Pull Request
