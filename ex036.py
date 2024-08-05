casa = float(input('Olá, qual o valor da casa: R$'))
salario = float(input('Qual o seu salário: R$'))
anos = int(input('Em quantos anos de financiamneto? '))
pres = casa/(anos*12)
apro = (salario*30/100)
print ('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}.'.format(casa, anos, pres))
if  apro <= pres:
    print('Empréstimo negado! As parcelas não podem execer 30% do seu salário.')
else:
    print('Empréstimo aprovado! O valor dividido vai ser de R${:.2f}, por mês durante {} anos.'.format(pres,anos))

print('Tenha um bom dia!')
