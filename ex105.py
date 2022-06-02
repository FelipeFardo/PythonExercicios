def notas(*num, sit=False):
    """
    -> função para analisar notas e situações de vários alunos.
    :param num: uma ou mais notas do aluno(aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situacão
    :return: dicionário com várias informações sobre a situação da turma.
    """
    aluno = {}
    aluno['total'] = len(num)
    aluno['maior'] = max(num)
    aluno['menor'] = min(num)
    aluno['media'] = sum(num)/len(num)
    if sit:
        if aluno['media'] < 5:
            aluno['situacao'] = 'HORRÍVEL'
        elif aluno['media'] < 7:
            aluno['situacao'] = 'RECUPERAVEL'
        elif aluno['media'] < 9:
            aluno['situacao'] = 'BOA'
        else:
            aluno['situacao'] = 'MUITO BOA'
    return aluno


print(notas(5.5, 9.5, 10, 6.5, sit=True))
