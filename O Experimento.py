import time
import random

nome = input("Digite seu nome ou apelido")

print("=== O Experimento ===")

print("Ei!\n")

print("Acorde", nome)

print("Você: Onde estou?")

print("Nós te sequestramos. Somos do governo e queremos realizar uma seleção nos cidadãos.")

print("Você: O que??? Como assim? O que isso quer dizer?")

print("Nós perdemos a fé na humanidade. A sociedade tem ficado cada vez mais burra...")

print("Eu me chamo Nefário e conduzirei o experimento.")

print("Você receberá perguntas diversas de conhecimentos básicos que todos deveriam ter.")

print("Você precisa acertar no MÍNIMO... 8 para sobreviver.")

print("Você: Sobreviver? Como assim?")

print("Sim. Caso você obtenha um desempenho menor que 8/10...")

print("Você...")

print("Será...")

print("Descartado!")

print("Você: Espere, descartado? O que isso quer dizer?")

print("Que você será 'desvivido'.")

print("Você: O QUÊ!? ESPERA!")

print("Boa sorte!")

print("Você: Não! Calma!")

banco_nivel_1 = [
    ["Qual é a capital do Brasil?", "a) São Paulo", "b) Brasília", "c) Rio de Janeiro", "b"],
    ["Quanto é 2 + 2?", "a) 3", "b) 4", "c) 5", "b"],
    ["Qual é a cor do céu em um dia limpo?", "a) Azul", "b) Verde", "c) Vermelho", "a"],
    ["Quantos dias tem uma semana?", "a) 5", "b) 6", "c) 7", "c"],
    ["Qual animal late?", "a) Gato", "b) Cachorro", "c) Peixe", "b"],
    ["Qual é o contrário de quente?", "a) Frio", "b) Alto", "c) Claro", "a"],
    ["Qual destes é uma fruta?", "a) Alface", "b) Banana", "c) Beterraba", "b"],
    ["Quantos meses tem um ano?", "a) 10", "b) 11", "c) 12", "c"],
    ["Qual parte do corpo usamos para enxergar?", "a) Olhos", "b) Pés", "c) Cotovelos", "a"],
    ["Qual idioma se fala nos Estados Unidos", "a) Inglês ", "b) Português", "c) Espanhol", "a"]
]

banco_nivel_2 = [
    ["Quanto é 9 x 3?", "a) 27", "b) 21", "c) 36", "a"],
    ["Qual a moeda do Brasil", "a) Real", "b) Dolar", "c) Rublo", "a"],
    ["Com que objeto se joga futebol?", "a) Cubo", "b) Disco", "c) Bola", "c"],
    ["Qual o terceiro planeta do Sistema Solar", "a) Mercúrio", "b) Terra", "c) Plutão", "b"],
    ["Qual destes é um número primo?", "a) 7", "b) 12", "c) 15", "a"],
    ["Em que país se fala mandarim?", "a) China", "b) Japão", "c) Brasil", "a"],
    ["Quanto é 81 dividido por 9?", "a) 8", "b) 9", "c) 10", "b"],
    ["Qual órgão responsável por pensar", "a) Pulmão", "b) Coração", "c) Cérebro", "c"],
    ["No centro oeste do Brasil, se predomina qual bioma?", "a) Caatinga", "b) Cerrado", "c) Tundra", "b"],
    ["Quanto é 2 elevado a 3?", "a) 6", "b) 8", "c) 9", "b"]
]

banco_nivel_3 = [
    ["Qual a capital dos Estados Unidos", "a) Nova York", "b) Miami", "c) Washington", "c"],
    ["Qual a modeda da Argentina", "a) Dólar", "b) Pesos", "c) Yuan", "b"],
    ["Qual a fórmula da água", "a) CH20", "b) O2", "c) H20", "c"],
    ["Como é 'casa' em inglês", "a) if", "b) print", "c) home", "c"],
    ["Quem descobriu o Brasil de acordo com a história tradicional?", "a) Pedro Álvares Cabral", "b) Cristóvão Colombo", "c) Juscelino Kubitschek", "a"],
    ["Qual a lei que aboliu a escravidão", "a) Lei dos Farrapos", "b)Lei Áurea ", "c) Lei Felca", "b"],
    ["Qual satélite natural da Terra?", "a) Lua", "b) Sol", "c) Sputnik", "a"],
    ["Qual a grafia correta?", "a) Sobrancelha", "b) Sombrancelha", "c) Sombramcelha", "a"],
    ["Qual destes países fazem fronteira com o Brasil?", "a) Equador", "b) Chile", "c) Paraguai", "c"],
    ["Qual a capital do Japão", "a) Kyoto", "b) Tóquio", "c) Osaka", "b"]
]
