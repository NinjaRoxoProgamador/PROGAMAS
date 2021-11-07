
import wikipedia
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time




def SIGLA():
 print(wikipedia.suggest(f'{pergunta}'))
 return pergunta
def PESQUISAR():
      
    pergunta = input('')
    resposta = wikipedia.summary(f"{pergunta}", sentences=1) 
    
    return resposta
print('O que voce vai fazer')
print('1 = Abreviações')
print('2 = Pesquisar algo')
n1 = input('')
if n1 == '1':
    pergunta = input('')
    SIGLA()
if n1 == '2':
    wikipedia = PESQUISAR()   
    print(wikipedia)