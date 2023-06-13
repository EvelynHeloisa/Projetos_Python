def notas(*num, sit=False):
    """
    Função para analisar notas de vários alunos.
    :param num: Notas, podendo recer várias...
    :param sit: Se True, mostrará a situação (Ruim, Razoável ou Boa) dependendo da média.
    :return: dicionário com as informações sobre o aluno ou notas.
    """
    analise = dict()
    media = sum(num) / len(num)

    analise['Total de Notas'] = len(num)
    analise['Maior'] = max(num)
    analise['Menor'] = min(num)
    analise['Média'] = media

    if media <= 4.0:
        situ = 'RUIM'
    elif media <= 7:
        situ = 'RAZOÁVEL'
    else:
        situ = 'BOA'

    if sit:
        analise['Situação'] = situ

    return analise


resp = notas(6.8, 10, 3.9, 8, sit=True)
print(resp)
#help(notas)
