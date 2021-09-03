from typing import List
from normalize import normalizar

SEPARADOR = ' '


def verificar_palavra(termo: str, texto: str) -> bool:
    """
    termo: 1 ou mais palavras separadas por espaços
    texto: texto em análise
    return: bool -> termo satisfeito se todas as palavras são encontradas no texto,
     não importa a ordem nem a proximidade
    """
    for palavra in termo.split(SEPARADOR):
        if palavra not in texto:
            return False
    return True


def verificar_frase(termo: str, texto: str) -> bool:
    """
    termo: 2 ou mais palavras separadas por espaços
    texto: texto em análise
    return: bool -> termo satisfeito se a frase inteira é encontrada no texto
    """
    if termo in texto:
        return True
    return False


def testar_match(termos: List[dict], texto: str) -> bool:
    """
    retornar False se algum termo de busca de exclusão é satisfeito
    retornar True se algum termo de busca de inclusão é satisfeito
    retornar False se nenhum termo é satisfeito
    """

    buscar_termo: dict = {
        "P": verificar_palavra,
        "F": verificar_frase
    }

    texto_normalizado: str = normalizar(texto)
    for termo in termos:
        termo_normalizado: str = normalizar(termo['termo'])

        verificar_termo: bool = buscar_termo[termo['tipo']](
            termo=termo_normalizado, texto=texto_normalizado
        )

        if termo['signo'] == 'E' and verificar_termo:
            return False
        elif termo['signo'] == 'I' and verificar_termo:
            return True

    return False
