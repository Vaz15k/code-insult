from config import InsultLevel
from messages.base import BaseMessageProvider, MessageCatalog
from messages.registry import register_provider


_STATUS_MESSAGES = {
    # ═══ 2xx — Success ═══════════════════════════════════════════════════════════
    200: {
        InsultLevel.LIGHT: [
            "Tudo certo, nada errado — e isso é raro o suficiente pra comemorar.",
            "Deu bom! Até o Paulo Guedes aprovaria esse request.",
            "200 OK: a paz reina neste reino. Por enquanto.",
            'Como diria o Chapolin: "Não contavam com minha astúcia!" — Funcionou!',
            "Sucesso. Até o Homer Simpson conseguiu. D'oh! ...quer dizer, Woo-hoo!",
            "Status 200: o equivalente digital de um 'bom dia' sincero.",
        ],
        InsultLevel.MEDIUM: [
            "200 OK. Parabéns, você fez o mínimo. Quer um biscoito?",
            "Funcionou. Vai comemorar ou vai continuar programando?",
            "OK. Dessa vez. Mas não se acostume.",
            "Sucesso absoluto. Até parece que foi de propósito.",
        ],
        InsultLevel.HEAVY: [
            "200? CARALHO, FUNCIONOU! Tira print e emoldura essa porra!",
            "Deu certo, cacete! Deve ser bug. Testa de novo.",
            "200 OK, seus lindos! Quem disse que código não presta?",
        ],
    },
    201: {
        InsultLevel.LIGHT: [
            "Criado com sucesso! Dr. Frankenstein ficaria orgulhoso.",
            "201 Created: Nasceu! Já pode registrar no cartório digital.",
            '"É um menino!" — e pesa 2.4 kilobytes.',
        ],
        InsultLevel.MEDIUM: [
            "Criado. Agora é sua responsabilidade. Não me culpe depois.",
            "Recurso criado com sucesso. Já já alguém deleta.",
        ],
        InsultLevel.HEAVY: [
            "CRIADO, PORRA! Parabéns, você deu à luz um JSON!",
        ],
    },
    202: {
        InsultLevel.LIGHT: [
            "202 Accepted: O servidor aceitou... mas vai fazer quando? Só Deus sabe.",
            "Recebido! Agora é sentar e esperar. Tipo processo na justiça brasileira.",
            'Como diz o Guia do Mochileiro: "Não entre em pânico". Mas também não respire aliviado.',
        ],
        InsultLevel.MEDIUM: [
            "Aceito. Mas processar mesmo, só quando o servidor estiver de bom humor.",
            "202: a versão digital do 'vou ver e te aviso'.",
        ],
        InsultLevel.HEAVY: [
            "Aceitou mas não processou. Igual promessa de político em ano eleitoral.",
        ],
    },
    204: {
        InsultLevel.LIGHT: [
            "204 No Content: O silêncio ensurdecedor do servidor. Nada a declarar.",
            "Sem conteúdo. Igual o novo episódio de The Office que você já viu 40 vezes.",
            "Vazio. Como o vácuo do espaço. Bowie estaria orgulhoso.",
        ],
        InsultLevel.MEDIUM: [
            "Nada. Zero. Null. Void. Quer uma mensagem? Não tem.",
            "204: o servidor te deu um ghosting educado.",
        ],
        InsultLevel.HEAVY: [
            "NADA. O servidor respondeu o equivalente a um vácuo no WhatsApp.",
        ],
    },
    # ═══ 3xx — Redirection ══════════════════════════════════════════════════════
    301: {
        InsultLevel.LIGHT: [
            '301: "Não estou mais aqui. Mudei. Supere." — Gandalf, depois de cair no abismo.',
            "Redirecionamento permanente. Como o Michael Scott mudando de emprego. De novo.",
            "Mudou pra sempre. Tipo quando o Orkut virou Facebook.",
        ],
        InsultLevel.MEDIUM: [
            "Mudou permanentemente. Assim como sua sanidade depois desse projeto.",
            "301: pegue suas coisas e vá pra URL nova. Não volte.",
        ],
        InsultLevel.HEAVY: [
            "Mudou de vez, irmão. Para de bater na porta errada!",
        ],
    },
    302: {
        InsultLevel.LIGHT: [
            '302 Found: "Achei, mas não era bem aqui... tenta ali."',
            "Redirecionamento temporário. Igual o Brasil na fila do pão.",
        ],
        InsultLevel.MEDIUM: [
            "Temporariamente movido. Tipo sua motivação às 18h de sexta.",
        ],
        InsultLevel.HEAVY: [
            "Vai pra lá, mas volta depois! Não é mudança, é passeio, cacete!",
        ],
    },
    304: {
        InsultLevel.LIGHT: [
            "304 Not Modified: Tá igualzinho. Nem uma ruga nova.",
            "Não mudou nada. Dorian Gray aprovaria essa resposta.",
        ],
        InsultLevel.MEDIUM: [
            "Não modificado. Igual seu código desde o commit da semana passada.",
            "304: a mesma coisa de sempre. E você esperava algo diferente?",
        ],
        InsultLevel.HEAVY: [
            "Não mudou PORRA NENHUMA. Cache tá aí pra isso, animal.",
        ],
    },
    # ═══ 4xx — Client Error ═════════════════════════════════════════════════════
    400: {
        InsultLevel.LIGHT: [
            "400 Bad Request: O servidor olhou pro seu request e fez cara de Nazaré confusa.",
            '"Isso não é um request, é um atentado à sintaxe." — O servidor, provavelmente.',
            "Bad Request. Nem o ChatGPT entenderia o que você mandou.",
            "400: O request tá tão torto que o Chapolin tropeçaria nele.",
        ],
        InsultLevel.MEDIUM: [
            "Request ruim. Tenta de novo, mas dessa vez com coerência.",
            "400: Seu JSON veio mais quebrado que promessa de ano novo em janeiro.",
            "O servidor entendeu... mas fingiu que não. Faz direito.",
        ],
        InsultLevel.HEAVY: [
            "QUE REQUEST DE MERDA É ESSE? Nem o Google Tradutor salva essa bagunça!",
            "400: Tá de sacanagem? Isso aqui não é request, é lixo digital!",
            "Bicho, teu request tá mais feio que briga de cachorro por comida!",
        ],
    },
    401: {
        InsultLevel.LIGHT: [
            '401 Unauthorized: "Você não vai passar!" — Gandalf, Servidor Edition.',
            "Não autorizado. Senha errada. Ou você, ou sua tia, ou os dois.",
            "401: O servidor pediu identidade e você mostrou a carteirinha do Clube do Bolinha.",
            '"Essa não é a credencial que você está procurando." — Obi-Wan Kenobi',
        ],
        InsultLevel.MEDIUM: [
            "Não autorizado. Nem adianta fazer charme. Cadê o token?",
            "401: sem senha, sem festa. Regras da casa.",
            "Você não tem permissão. Nem o Darth Vader conseguiria acessar sem o token.",
        ],
        InsultLevel.HEAVY: [
            "TU NÃO TEM AUTORIZAÇÃO, ANIMAL! Quer entrar sem crachá? Tá na Disney?",
            "401: Senha errada, seu cabeça de bagre! Quer que eu desenhe um login?",
        ],
    },
    403: {
        InsultLevel.LIGHT: [
            '403 Forbidden: "Isso é território proibido." — Mufasa, apontando pras terras sombrias.',
            "Proibido! Nem o Harry Potter sem capa de invisibilidade entra aqui.",
            "403: O servidor sabe quem você é. Só não gosta de você mesmo.",
            "Acesso negado. Tipo aquele rolê que você não foi convidado.",
        ],
        InsultLevel.MEDIUM: [
            "Proibido. Não é falta de senha — é falta de credenciais. E talvez de caráter.",
            "403: Você até tem senha, mas ninguém aqui vai abrir a porta.",
            "Forbidden. Nem que você fosse o Keanu Reeves. (Ok, talvez ele pudesse.)",
        ],
        InsultLevel.HEAVY: [
            "PROIBIDO, CARALHO! Sai daqui! Nem Jesus Cristo entra sem autorização!",
            "403: Não, não e NÃO! Tá surdo? Volta pro teu setor!",
        ],
    },
    404: {
        InsultLevel.LIGHT: [
            '404 Not Found: "Procurei em toda galáxia e não achei." — Baby Yoda.',
            "404: O recurso sumiu. Como meias na máquina de lavar.",
            "Não encontrado. Igual o Sétimo Sentido da deep web. Simplesmente não existe.",
            '"O que você procura não está aqui." — Yoda, servindo HTTP.',
            "404: Nem a Nazaré conseguiu achar. E olha que ela é confusa, não cega.",
        ],
        InsultLevel.MEDIUM: [
            "404: Não tá aqui. Não tá em lugar nenhum. Para de insistir.",
            "Not Found. Igual a paciência do tech lead depois do deploy de sexta.",
            "404: Isso não existe. E se existiu, já era. Supera.",
            "Perdido como agulha no palheiro. Só que o palheiro também não existe.",
        ],
        InsultLevel.HEAVY: [
            "NÃO ACHEI, PORRA! Para de bater nessa URL que já morreu!",
            "404: TÁ PROCURANDO O QUÊ, DESGRAÇA? Isso aqui já era! Foi de arrasta!",
            "Perdido que nem virgindade em festa de faculdade de TI. Inexiste.",
        ],
    },
    405: {
        InsultLevel.LIGHT: [
            "405: GET onde era pra ser POST. É tipo tentar abrir uma porta empurrando quando era pra puxar.",
            "Método não permitido. Como diria Raul Seixas: 'Tenta outra vez!'",
            "405: 'Não é assim que se faz.' — Joel Santana, explicando HTTP.",
        ],
        InsultLevel.MEDIUM: [
            "Método errado, campeão. GET ≠ POST ≠ PUT ≠ DELETE. Tão difícil?",
            "405: Você tá tentando enfiar um quadrado num buraco redondo.",
        ],
        InsultLevel.HEAVY: [
            "MÉTODO ERRADO, ANIMAL! Quer fazer DELETE num GET? Tá maluco?!",
        ],
    },
    408: {
        InsultLevel.LIGHT: [
            "408 Request Timeout: 'O tempo é uma ilusão.' — Einstein. Mas o timeout é real.",
            "Demorou mais que intervalo do Lula pra responder pergunta de repórter.",
            "Timeout: o servidor cansou de esperar. Foi tomar um café.",
        ],
        InsultLevel.MEDIUM: [
            "Timeout. Demorou tanto que o servidor já viu todas as temporadas de Friends.",
            "408: Você perdeu a janela. Literalmente.",
        ],
        InsultLevel.HEAVY: [
            "DEMOROU, PORRA! O servidor já morreu de velho esperando!",
            "408: Ô lesma, o timeout estourou! Tá usando internet discada?",
        ],
    },
    409: {
        InsultLevel.LIGHT: [
            '409 Conflict: "Só pode haver um!" — Highlander.',
            "Conflito! Dois requests brigando pelo mesmo recurso. Que feio.",
            "409: Briga de foice no escuro. Ninguém ganha.",
        ],
        InsultLevel.MEDIUM: [
            "Conflito de dados. Igual dois devs editando a mesma linha no Git.",
            "409: Alguém chegou primeiro. Aceita que dói menos.",
        ],
        InsultLevel.HEAVY: [
            "CONFLITO, CACETE! Resolve essa treta aí antes de mandar de novo!",
        ],
    },
    410: {
        InsultLevel.LIGHT: [
            '410 Gone: "Foi. Não volta mais." — Thanos, depois do estalo.',
            "Esse recurso já era. Foi de Americanas. Não volta nunca mais.",
            "410: Deletado permanentemente. Igual sua conta do Fotolog.",
        ],
        InsultLevel.MEDIUM: [
            "Gone. Não adianta chorar. O recurso foi morar no céu dos bytes.",
            "410: Isso morreu. Faz um velório e segue a vida.",
        ],
        InsultLevel.HEAVY: [
            "JÁ ERA, PORRA! Foi de arrasta pra cima! Não insiste!",
        ],
    },
    413: {
        InsultLevel.LIGHT: [
            "413 Content Too Large: 'Isso é grande demais até pra mim.' — Seu Madruga.",
            "Payload muito grande. Nem o Flash entregaria isso a tempo.",
            "413: Seu request tá mais pesado que o SPC do brasileiro médio.",
        ],
        InsultLevel.MEDIUM: [
            "Conteúdo grande demais. Isso é um request ou um dump do Instagram?",
            "413: Tá mandando a Wikipedia inteira? Divide isso aí.",
        ],
        InsultLevel.HEAVY: [
            "TA MANDANDO O QUÊ, A BÍBLIA EM JSON?! Divide essa porra!",
        ],
    },
    414: {
        InsultLevel.LIGHT: [
            "414 URI Too Long: A URL tá maior que nome de família real europeia.",
            "Essa URL é mais longa que filme do senhor dos anéis versão estendida.",
        ],
        InsultLevel.MEDIUM: [
            "URI muito longa. Isso é URL ou CPF com dígito verificador?",
        ],
        InsultLevel.HEAVY: [
            "TÁ DE SACANAGEM COM ESSA URL GIGANTE? Isso é request ou bíblia?!",
        ],
    },
    415: {
        InsultLevel.LIGHT: [
            "415 Unsupported Media Type: O servidor não fala esse idioma.",
            '"Isso não é JSON." — O servidor, olhando com desprezo pro seu XML.',
        ],
        InsultLevel.MEDIUM: [
            "Formato não suportado. O servidor não sabe ler hieróglifos.",
            "415: Tá mandando o quê, um .doc do Word 97?",
        ],
        InsultLevel.HEAVY: [
            "QUE FORMATO É ESSE, ANIMAL? Manda JSON ou cai fora!",
        ],
    },
    418: {
        InsultLevel.LIGHT: [
            "418 I'm a Teapot: Sou um bule, não uma cafeteira. Respeita minha profissão!",
            '418: "Sou um bule, pô!" — O servidor, indignado com seu pedido de café.',
            "I'm a teapot. Essa é a melhor resposta HTTP já inventada. Change my mind.",
        ],
        InsultLevel.MEDIUM: [
            "Sou um bule, não um engenheiro de software. Café? Ali na esquina.",
            "418: o servidor decidiu que hoje ele é um bule. Respeita.",
        ],
        InsultLevel.HEAVY: [
            "SOU UM BULE, CARALHO! Quer café? Vai no Starbucks!",
        ],
    },
    422: {
        InsultLevel.LIGHT: [
            "422 Unprocessable: O JSON tá certo, mas a lógica... a lógica é triste.",
            '422: "Faz sentido... mas não." — O servidor, coçando a cabeça.',
        ],
        InsultLevel.MEDIUM: [
            "422: Sintaxe ok, semântica ridícula. Tenta de novo.",
            "Inprocessável. Tipo entender a trama de Dark de primeira.",
        ],
        InsultLevel.HEAVY: [
            "ISSO AÍ NÃO DÁ PRA PROCESSAR, JUMENTO! A sintaxe tá boa, mas a ideia é horrível!",
        ],
    },
    429: {
        InsultLevel.LIGHT: [
            "429 Too Many Requests: Calma, ansioso! O servidor não é sua mãe.",
            '429: "Desacelera, campeão." — Ayrton Senna, se fosse servidor HTTP.',
            "Muitos requests. O servidor tá tipo: 'pera aí, respira, conta até 10'.",
        ],
        InsultLevel.MEDIUM: [
            "Calma aí, Flash. Dá um tempo entre os requests, tá floodando.",
            "429: Você foi bloqueado. Não pelo conteúdo, mas pela insistência chata.",
        ],
        InsultLevel.HEAVY: [
            "PARA DE ESPAMAR, DESGRAÇA! Isso não é boteco, tem limite!",
            "429: Tá achando que aqui é farra? Toma um cooldown e volta depois!",
        ],
    },
    # ═══ 5xx — Server Error ═════════════════════════════════════════════════════
    500: {
        InsultLevel.LIGHT: [
            '500 Internal Server Error: "Houston, nós temos um problema." — Apollo 13.',
            "500: O servidor quebrou. Mas a culpa é do estagiário, sempre.",
            "Erro interno. 'Isso é trabalho pro Chapolin Colorado!'",
            "500: O servidor tá tipo 'não sei o que aconteceu, mas foi feio'.",
        ],
        InsultLevel.MEDIUM: [
            "Erro interno. Alguém commitou no sábado à noite, né?",
            "500: O servidor teve um treco. Tenta de novo quando ele se recuperar.",
            "Internal Server Error. Tradução: 'deu ruim e não sei explicar'.",
        ],
        InsultLevel.HEAVY: [
            "DEU MERDA NO SERVIDOR! Não foi você, foi a gente. Mas foi você também.",
            "500: PUTA QUE PARIU, QUEBROU TUDO! Corre que o servidor explodiu!",
            "Erro interno. Se prepare que o tech lead vai vir xingar todo mundo.",
        ],
    },
    501: {
        InsultLevel.LIGHT: [
            "501 Not Implemented: 'Um dia a gente chega lá.' — Criança Esperança.",
            "Não implementado. Tá no backlog desde 2019.",
            "501: O dev disse que ia fazer. Disse...",
        ],
        InsultLevel.MEDIUM: [
            "Não implementado. A feature ficou no 'vou ver e te aviso' eterno.",
            "501: Isso aqui ainda não existe. Quem sabe no próximo sprint.",
        ],
        InsultLevel.HEAVY: [
            "NÃO FIZEMOS ESSA MERDA AINDA! Tá no Jira, paciência!",
        ],
    },
    502: {
        InsultLevel.LIGHT: [
            "502 Bad Gateway: O intermediário fez besteira. Culpa do meio-campo.",
            "Bad Gateway: o proxy recebeu uma resposta que não entendeu. Tipo eu com física quântica.",
            '502: "O mensageiro foi morto." — Game of Thrones, temporada do proxy.',
        ],
        InsultLevel.MEDIUM: [
            "502: O gateway tomou uma resposta torta e não soube lidar. Terapia já!",
            "Bad Gateway. Nem o servidor, nem o proxy. Os dois a 80km/h.",
        ],
        InsultLevel.HEAVY: [
            "O GATEWAY CAGOU NO PAU! A resposta veio toda errada e ele engoliu!",
        ],
    },
    503: {
        InsultLevel.LIGHT: [
            "503 Service Unavailable: 'Voltei, mas não pra sempre.' — Crashed.",
            "Serviço indisponível. O servidor tirou férias. Mercado Pago feelings.",
            "503: O servidor foi dormir. Tenta amanhã, ou depois, ou nunca.",
        ],
        InsultLevel.MEDIUM: [
            "Indisponível. Deve ser hora do cafezinho do datacenter.",
            "503: O servidor cansou. Todo mundo tem limite.",
        ],
        InsultLevel.HEAVY: [
            "CAIU, PORRA! O servidor foi de base! Liga pro NOC, rápido!",
            "503: Serviço morreu. Quem mandou fazer deploy na sexta-feira?",
        ],
    },
    504: {
        InsultLevel.LIGHT: [
            "504 Gateway Timeout: O proxy cansou de esperar. Foi embora.",
            'Gateway Timeout: "A espera acabou." — Django Livre, versão HTTP.',
            "504: Demorou tanto que o gateway foi ver se tava chovendo.",
        ],
        InsultLevel.MEDIUM: [
            "Timeout no gateway. O proxy esperou, esperou, e disse: 'cansei'.",
            "504: Resposta não veio. O gateway já fez as malas e foi pra casa.",
        ],
        InsultLevel.HEAVY: [
            "O GATEWAY ESPEROU ATÉ CRIAR BARBA E NADA! Timeout, cacete!",
        ],
    },
}

# ── Default / Fallback messages ───────────────────────────────────────────────

_DEFAULT_MESSAGES = {
    InsultLevel.LIGHT: [
        "Resposta inesperada. Mas ei, pelo menos não é 500.",
        '"A vida é como uma caixa de chocolates..." — mas esse status code não é um chocolate bom.',
    ],
    InsultLevel.MEDIUM: [
        "Status code estranho. Você tá inventando código novo?",
        "Isso é um código HTTP ou você tá digitando aleatório?",
    ],
    InsultLevel.HEAVY: [
        "QUE STATUS CODE É ESSE, ANIMAL? Tá tirando da cartola?!",
        "Isso não é HTTP, é hieróglifo. Para de inventar código!",
    ],
}

# ── Catalog ───────────────────────────────────────────────────────────────────

PT_BR_CATALOG = MessageCatalog(
    lang="pt_br",
    lang_name="Português Brasileiro",
    messages=_STATUS_MESSAGES,
    default_messages=_DEFAULT_MESSAGES,
)


class PtBRProvider(BaseMessageProvider):
    """
    Provider de mensagens em Português Brasileiro.
    """

    @property
    def catalog(self) -> MessageCatalog:
        return PT_BR_CATALOG

    @classmethod
    def lang_code(cls) -> str:
        return "pt_br"


register_provider(PtBRProvider)
