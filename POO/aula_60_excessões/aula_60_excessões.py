class TaerradoError(Exception):
    pass


def testar():
    raise TaerradoError('essa fera ai meu')

testar()