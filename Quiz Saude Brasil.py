# coding: UTF-8
SCORE = 0 #pontuação

#Tela inicio
print ("\nBem-Vindo ao Quiz Saúde Brasil! \nversão:covid-19 \ndesenvolvido por: Mayron Freitas, Tayane Miranda, Erick Rodrigues \n")
print ("\nVocê responderá 10 perguntas, \ncada uma valendo 100 pontos \nse você errar, perderá 30 pontos.\n\nBOA SORTE!")
input ("\nAperte ENTER para começar")
nome = input ("\n\nQual seu nome?")
print ("\nOlá," + nome + "\nVamos inciar o quiz!") 
input ("\nAperte ENTER para começar")

#lista de perguntas
lista_perguntas = [
    {
    'pergunta':'1- Pessoas sem sintomas podem transmitir o covid-19?',
    'resposta_correta': 'b',
    'respostas':[
        { 'opção': 'A',
        'descrição':'Sim'  },

        {  'opção': 'B',
            'descrição': 'Não' }
     ]
    },
    {
    'pergunta':'2- Como a covid-19 é transmitida',
    'resposta_correta': 'd',
    'respostas':[
        { 'opção': 'A',
        'descrição':'De uma pessoa para outra '  },

        {  'opção': 'B',
            'descrição': 'Através de gotículas de saliva ou muco' },
        
        {  'opção': 'C',
            'descrição': 'Aperto de mãos ou compartilhar objeto' },

        {  'opção': 'D',
            'descrição': 'Todas estão corretas' }
     ]
    },
    {
    'pergunta':'3- LoLó e cocaína podem matar o coronavírus?',
    'resposta_correta': 'b',
    'respostas':[
        { 'opção': 'A',
        'descrição':'Verdadeiro'  },

        {  'opção': 'B',
            'descrição': 'Falso' },
     ]
    },
    {
    'pergunta':'4- O que é COVID-19?',
    'resposta_correta': 'a',
    'respostas':[
        { 'opção': 'A',
        'descrição':'É um vírus que pode causar doenças em animas ou humanos '  },

        {  'opção': 'B',
            'descrição': 'É um vírus que só pode ser contraído por animais.' },
     ]
    },
    {
    'pergunta':'5- Produtos da China podem conter o covid-19 ?',
    'resposta_correta': 'b',
    'respostas':[
        { 'opção': 'A',
        'descrição':'Sim'  },

        {  'opção': 'B',
            'descrição': 'Não' },
     ]
    },
    {
    'pergunta':'6- De onde surgiu o COVID-19?',
    'resposta_correta': 'c',
    'respostas':[
        { 'opção': 'A',
        'descrição':'África'  },

        {  'opção': 'B',
            'descrição': 'Alemanha' },
        
        {  'opção': 'C',
            'descrição': 'China' },

        {  'opção': 'D',
            'descrição': 'Brasil' }
     ]
    },
    {
    'pergunta':'7- Já existe uma vacina para COVID-19',
    'resposta_correta': 'b',
    'respostas':[
        { 'opção': 'A',
        'descrição':'Verdadeiro'  },

        {  'opção': 'B',
            'descrição': 'Falso' },
     ]
    },
     {
    'pergunta':'8- O que fazer para se prevenir do covid-19 ?',
    'resposta_correta': 'd',
    'respostas':[
        { 'opção': 'A',
        'descrição':'Lavar as mãos diariamente '  },

        {  'opção': 'B',
            'descrição': 'Trocar aperto de mãos ' },
        
        { 'opção': 'C',
            'descrição': 'Evitar aglomeração'},

        { 'opção': 'D',
            'descrição': 'A e C estão corretas'},
     ]
    },
    {
    'pergunta':'9- Quais são os sintomas da covid-19?',
    'resposta_correta': 'c',
    'respostas':[
        { 'opção': 'A',
        'descrição':'Falta de ar, dor e confusão nasal'  },

        {  'opção': 'B',
            'descrição': 'Confusão nasal, dor e pressão no peito' },
        
        { 'opção': 'C',
            'descrição': 'Pressão no peito, dor, Febre e Falta de ar'},
     ]
    },
    {
    'pergunta':'10- Chá de erva-doce pode matar o Covid-19?',
    'resposta_correta': 'b',
    'respostas':[
        { 'opção': 'A',
        'descrição':'Verdadeiro'  },

        {  'opção': 'B',
            'descrição': 'Falso' },
     ]
    },
]
#pergunta
for pergunta in lista_perguntas:
   print("\nPergunta: %s \n" % pergunta['pergunta'])
   
   #opções de respostas
   for resposta in pergunta['respostas']:
       print( "%s) %s\n" % (resposta['opção'], resposta['descrição']) )
       
  #resposta do usuário
   resposta_escolhida = input("\nResposta: ")

   if resposta_escolhida.lower() == pergunta['resposta_correta'].lower():
       SCORE = SCORE + 100 
   else:
       SCORE = SCORE - 30
       
print("\nPerguntas finalizadas.\n" + (nome)+ ',' + "sua pontuação é: %i" % SCORE)

input ("\n\nAperte ENTER para visualizar o RANKING\n")

#ranking
from operator import itemgetter

ranking = list()
ranking = open('ranking.txt', 'a')
ranking.write("Jogador:"' '+ nome + ' ' + "Score: %i" % SCORE + '\n')
ranking.close()

print("\n---RANKING---\n")

ranking = sorted(open('ranking.txt','r'))

for linha in ranking:
       print (linha)

input("\n\nAperte ENTER para finalizar o GAME\n")



