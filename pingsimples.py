import os ##Importa o módulo ou biblioteca os (integra os programas e 
#recursos do S.O)

print('#' * 60) ##Imprimindo #60 vezes

ip_ou_host = input("Digite o Ip ou host a ser verificado: ")
#Criamos uma variavel que vai receber do usuário um ip

print('-' * 60) ##Imprimindo o - 60 vezes

os.system('ping -n 6 {}'.format(ip_ou_host)) ##Chamando system da biblioteca os - comando ping
#-n numero de pacotes que serão 6 {}

print('-' * 60) ##Imprimindo o - 60 vezes