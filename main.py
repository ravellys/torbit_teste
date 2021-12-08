from match import testar_match
from otimizar import otimizar_termos

"""
termos de busca podem ter signo de inclusão (I) ou exclusão (E)
termos de busca podem ser tipo palavras (P) ou tipo frase (F)
"""

termos = [
    {"signo": "I", "tipo": "F", "termo": "grande são paulo"},
    {"signo": "I", "tipo": "F", "termo": "são paulo"},
    {"signo": "I", "tipo": "P", "termo": "vacina covid"},
    {"signo": "I", "tipo": "P", "termo": "calendário vacina covid"},
    {"signo": "E", "tipo": "P", "termo": "futebol"},
    {"signo": "E", "tipo": "P", "termo": "gripe"},
    {"signo": "E", "tipo": "P", "termo": "vacina gripe"}
]


if __name__ == '__main__':
    termos_otimizados = otimizar_termos(termos)
    print(termos_otimizados)
    texto = 'olá grande paulo! vamos jogar futebol'
    print('testar match:', testar_match(termos, texto))
