from typing import List
from normalize import normalizar


def is_redundante(novo_termo: str, termos_lista: List[str]) -> bool:

    for termo in termos_lista:
        if novo_termo in termo or termo in novo_termo:
            return True
    return False


def otimizar_termos(termos: List[dict]) -> List[dict]:

    lista_termos_normalizados = []
    termos_nao_redundantes = []
    for termo in termos:
        termo_normalizado = normalizar(termo['termo'])

        redundante: bool = is_redundante(termo_normalizado, lista_termos_normalizados)

        if not redundante:
            lista_termos_normalizados.append(termo_normalizado)
            termos_nao_redundantes.append(termo)

    print(lista_termos_normalizados)
    return termos_nao_redundantes




