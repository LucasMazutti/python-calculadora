#####CALCULADORA.py

def somar(a,b):
	return a + b
def subtraçao(a,b):
	return a - b
def multiplicaçao(a,b):
	return a * b
def divisao(a,b):
	if b == 0:
		print('Erro: Divisão por zero.')
		return None
	return a / b
	
def exibir_menu():
	print('\nEscolha uma das operações, por favor!')
	print('1 - operação de soma','+')
	print('2 - operação de subtração','-')
	print('3 - operação de multiplicação','*')
	print('4 - operação de divisão','/')
	
while True:
	exibir_menu()
	escolha = input("escolha uma das operações (1,2,3,4) ou 'sair' para encerrar:")
	
	if escolha.lower() == 'sair':
		print('retornando ao menu principal')
		break 
	if escolha not in ['1','2','3','4']:
		print('operação não aceita')
		continue
	try:
		num1 = float(input('Digite o primeiro número:'))
		num2 = float(input('Digite o segundo número'))
	except ValueError:
		print('Número não aceito, tente novamente.')
		continue
	if escolha == '1':
		resultado = somar(num1,num2)
	elif escolha == '2':
		resultado = subtraçao(num1,num2)
	elif escolha == '3':
		resultado = multiplicaçao(num1,num2)
	elif escolha == '4':
		resultado = divisao(num1,num2)
	
	print(f'Resultado:{resultado}')   ##### consultar para ver sse temos algum erro no código, 
	##provavelmente que sim 
