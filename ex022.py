from posixpath import split


nome = input("Digite seu nome completo: ").strip()
print(f'Seu nome em letras maíusculas: {nome.upper()}')
print(f'Seu nome em letras minúsculas: {nome.lower()}')
separa = nome.split()
print(f'Seu primeiro nome tem ao todo {len(separa[0])} letras')
