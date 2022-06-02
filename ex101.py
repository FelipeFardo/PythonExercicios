
def voto(anoDeNascimento):
    from datetime import date
    idade = date.today().year - anoDeNascimento
    if 18 <= idade < 70:
        return f"Com {idade} anos: VOTO OBRIGATÓRIO"
    elif idade < 16:
        return f"Com {idade} anos: VOTO NEGADO"
    else:
        return f"Com {idade} anos: VOTO OPCIONAL"


voto = voto(int(input('Qual o seu ano de nascimento? ')))
print(voto)
