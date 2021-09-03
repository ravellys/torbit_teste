import re
from unicodedata import normalize


def normalizar(valor: str) -> str:
    valor = normalize('NFKD', valor).encode('ISO-8859-1', 'ignore').decode('ASCII')
    valor = re.sub('[^A-Za-z0-9]+', ' ', valor)
    return valor.lower()
