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

banco_nivel_4 = [
    ["Qual é o maior país da América do Sul?", "a) Argentina", "b) Brasil", "c) Chile", "b"],
    ["Qual das alternativas é usado exclusivamente no final de frases ou isolado em uma pergunta?", "a) Porquê", "b) Por quê", "c) Por que", "b"],
    ["Quantas arestas tem um prisma quadrangular?", "a) 8", "b) 12", "c) 6", "b"],
    ["Qual é o maior oceano?", "a) Pacífico", "b) Atlântico", "c) Índico", "a"],
    ["Qual destes é um continente?", "a) África", "b) Antártica", "c) San Marino", "a"],
    ["Qual é o país conhecido pelo Monte Fuji?", "a) China", "b) Japão", "c) Coreia do Sul", "b"],
    ["Qual é o país onde fica a torre Eiffel?", "a) França", "b) Itália", "c) Espanha", "a"],
    ["Qual a capital da Rússoa", "a) Moscou", "b) Luxemburgo ", "c) São Petesburgo", "a"],
    ["Qual órgão bombeia sangue?", "a) Coração", "b) Rim", "c) Pancreas", "a"],
    ["Qual destes animais é um mamífero?", "a) Cachorro", "b) Cobra", "c) Sapo", "a"]
]

banco_nivel_5 = [
    ["Quem descobriu a América segundo a história tradicional?", "a) Pedro Álvares Cabral", "b) Cristóvão Colombo", "c) Napoleão Bonaparte", "a"],
    ["Em que ano o Brasil se tornou independente?", "a) 1500", "b) 1822", "c) 1889", "b"],
    ["Quem proclamou a República no Brasil?", "a) Deodoro da Fonseca", "b) Getúlio Vargas", "c) Dom Pedro I", "a"],
    ["Qual era o regime do Brasil antes da República?", "a) Monarquia", "b) Ditadura", "c) Comunismo", "a"],
    ["Qual destes foi imperador do Brasil?", "a) Dom Pedro II", "b) Juscelino Kubitschek", "c) Tancredo Neves", "a"],
    ["A Segunda Guerra Mundial terminou em qual ano?", "a) 1939", "b) 1945", "c) 1964", "b"],
    ["Qual país sofreu os bombardeios de Hiroshima e Nagasaki?", "a) Japão", "b) China", "c) Coreia", "a"],
    ["A Guerra Fria foi principalmente entre quais blocos?", "a) EUA e URSS", "b) Brasil e Argentina", "c) França e Itália", "a"],
    ["Qual civilização construiu as pirâmides de Gizé?", "a) Egípcia", "b) Romana", "c) Grega", "a"],
    ["Qual cidade foi capital do Império Romano?", "a) Roma", "b) Atenas", "c) Paris", "a"]
]

banco_nivel_6 = [
    ["Como se diz 'Eu vou ao restaurante' em inglês", "a) I went to the Restaurant", "b) I will go to the restaurant", "c) I will eat in restaurante", "b"],
    ["Qual poder cria leis?", "a) Legislativo", "b) Executivo", "c) Judiciário", "a"],
    ["Qual poder julga conflitos?", "a) Executivo", "b) Judiciário", "c) Legislativo", "b"],
    ["Qual poder governa e administra?", "a) Executivo", "b) Judiciário", "c) Legislativo", "a"],
    ["O que é uma Constituição?", "a) Lei principal de um país", "b) O pacto político que subordina os poderes públicos às leis", "c) Um imposto", "a"],
    ["Qual destes é um documento de identificação?", "a) Passaporte", "b) CPF", "c) PIS", "a"],
    ["Qual destas linhas imaginárias divide a Terra nos hemisférios Ocidental e Oriental?", "a) Linha do Equador", "b) Meridiano de Greenwich", "c) Trópico de Capricórnio", "a"],
    ["Qual destes países esta no ORIENTE", "a) México", "b) Panamá", "c) Rússia", "c"],
    ["Qual destes órgãos é o principal responsável por filtrar o sangue", "a) Rim", "b) Fígado", "c) Intestino", "a"],
    ["Qual é o planeta mais quente do nosso sistema solar?", "a) Mercúrio", "b) Vênus", "c) Marte", "b"]
]

banco_nivel_7 = [
    ["Qual destes é um exemplo de energia renovável?", "a) Solar", "b) Carvão", "c) Petróleo", "a"],
    ["Quando foi a queda do muro de Berlim?", "a) 1988", "b) 1987", "c) 1989", "c"],
    ["Em qual museu do mundo está exposta a famosa pintura 'Mona Lisa'", "a) Louvre", "b) Museu Da Vinci", "c) Museu Nacional da Holanda", "a"],
    ["Na mitologia grega, qual a criatura que é metade touro e metade homem?", "a) Centauro", "b) Minotauro", "c) Sátiro", "b"],
    ["Qual planeta é conhecido por seus anéis?", "a) Saturno", "b) Mercúrio", "c) Terra", "a"],
    ["Qual destes é uma fonte de água doce?", "a) Rio", "b) Oceano", "c) Mar", "a"],
    ["A Pizza é alimento de qual país", "a) Itália", "b) França", "c) Alemanha", "a"],
    ["Onde foi inventado o Hamburguer?", "a) Novo Hamburgo", "b) Hamburgo", "c) Berlim ", "b"],
    ["Qual destes NÃO é um fenômeno natural?", "a) Chuva", "b) Eletricidade", "c) Terremoto", "a"],
    ["Qual órgão libera Insulina?", "a) Pancreas", "b) Diafragma", "c) Fígado ", "a"]
]