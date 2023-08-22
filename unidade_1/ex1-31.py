dias = ['domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado'] 
##^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
##isso é uma lista, é um assunto mais posterior
diaescolhido = int(input('Digite o numero do dia da semana: '))
if diaescolhido >= 1 and diaescolhido <= 7:
    print(dias[diaescolhido - 1])
else:
    print('Dia inválido')