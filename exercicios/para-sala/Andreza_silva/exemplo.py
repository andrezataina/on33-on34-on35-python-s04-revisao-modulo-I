def ano_de_nascimento():
    sua_idade = int(input('Digite a sua idade: '))
    ano_atual = int(input('Digite o ano atual: '))
    return ano_atual - sua_idade
print(f'O seu ano de nascimento é {ano_de_nascimento()}')
