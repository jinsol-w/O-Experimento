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

banco_nivel_8 = [
    ["Qual palavra está escrita corretamente?", "a) Excessão", "b) Exceção", "c) Esceção", "b"],
    ["O que acontece com o tempo para um astronauta que viaja quase à velocidade da luz em relação a quem ficou na Terra?", "a) Tempo passa devagar para o astronauta", "b) Tempo passa rápido para o astronauta", "c) Tempo exatamente igual", "a"],
    ["O que é um sinônimo?", "a) Palavra de escrita igual", "b) Singnificado Oposto", "c) Significado parecido", "c"],
    ["Qual destas partículas subatômicas não possui carga elétrica?", "a) Nêutron", "b) Életron", "c) Próton", "a"],
    ["Qual é a velocidade aproximada da luz no vácuo?", "a) 300.000 km/s", "b) 300.000 km/h", "c) 300.000km/m", "a"],
    ["Qual é o país mais jovem do mundo, tendo declarado sua independência no ano de 2011?", "a) Sudão do sul", "b) Kosovo", "c) Timor-Leste", "a"],
    ["Qual civilização antiga desenvolveu a escrita cuneiforme, considerada uma das primeiras formas de escrita da humanidade?", "a) Egípcia", "b) Suméria", "c) Fenícia", "b"],
    ["Qual é o deserto mais seco do mundo, localizado na América do Sul?", "a) Deserto do Saara", "b) Deserto de Gobi", "c) Deserto do Atacama", "c"],
    ["Qual foi o principal motivo que levou a queda do Império Romano  do Ocidente no ano de 476 d.C?", "a) As invasões bárbaras e a crise interna", "b) A invenção da pólvora pelos inimigos", "c) A ascensão imediata do Império Islâmico", "a"],
    ["Qual criatura marinha possui três corações, nove cérebros e sangue da cor azul?", "a) Polvo", "b) Lula-Gigante", "c) Água-Viva", "a"]
]

banco_nivel_9 = [
    ["Quem foi o primeiro homem a viajar para o espaço em 1961?", "a) Neil Armstrong", "b) Yuri Gagarin", "c) John Glenn", "b"],
    ["Qual o nome do primeiro computador eletrônico digital de propósito geral da história, contruído em 1946?", "a) ENIAC", "b) IBM PC", "c) Macintosh", "a"],
    ["Quem foi a primeira pessoa a ganhar dois Prêmios Nobel em áreas científicas diferentes?", "a) Albert Einsteni", "b) Nikola Tesla", "c) Marie Curie", "c"],
    ["O que são as famosas 'Nuvens de Magalhães' visíveis no céu norturno do hemisfério sul?", "a) Duas galáxias satélites da Via Láctea", "b) Nebulosas onde nascem novos sistemas solares", "c) Tempestades de poeira cósmica no SIstema Solar exterior", "a"],
    ["Qual é o metal cujo símbolo químico é Hg e que permanece em estado líquido em temperatura ambiente?", "a) Magnésio", "b) Mercúrio", "c) Hidrogênio", "b"],
    ["Quem liderou a primeira expedição europeia a atingir o Polo Sul geográfico?", "a) Robert Falcon Scott", "b) Roald Amundsen", "c) Richard Byrd", "b"],
    ["Qual é o elemento natural mais denso e pesado da tabela periódica?", "a) Chumbo", "b) Urânio", "c) Ósmio", "c"],
    ["Na mitologia grega e na obra de Homero, quantos anos durou a famosa Guerra de Troia?", "a) 3 anos", "b) 10 anos", "c) 20 anos", "b"],
    ["Quantos ossos tem um humano adulto?", "a) 312", "b) 150", "c) 206", "c"],
    ["Qual cidade foi destruída pelo Vesúvio em 79 d.C?", "a) Pompeia", "b) Atenas", "c) Esparta", "a"]
]

banco_nivel_10 = [
    ["Qual o nome do meu gato", "a) Nefarinho", "b) Nefarão", "c) Nao tenho gato", "a"],
    ["Qual minha comida favorita", "a) Pizza", "b) Macarrão com Salsicha", "c) Cachorro frio", "b"],
    ["Se eu fosse um animal, qual eu seria", "a) Tubarão", "b) Elefante", "c) Hipopotamo", "a"],
    ["Pra qual time eu torço", "a) Flamengo", "b) Corinthians", "c) Bangu", "c"],
    ["Qual o nome da minha mãe", "a) Nefaria", "b) Nefa", "c) Joana", "c"],
    ["Qual a coisa que eu mais valorizo num amigo", "a) Aparencia", "b) Dinheiro", "c) Personalidade", "c"],
    ["Quais eram minhas incriveis notas no Ensino Medio", "a) 10", "b) 9", "c) 3", "b"],
    ["Quantos filhos eu tenho", "a) 1", "b) 2", "c) 3", "b"],
    ["Qual meu país favorito", "a) Brasil", "b) Coreia do Norte", "c) China", "c"],
    ["O que se deve fazer ao enviar uma mensagem escrita errada no WhatsApp", "a) Mnndar a palavra certa com *", "b) Editar mensagem", "c) Ignorar", "b"]
]

niveis = [
    banco_nivel_1,
    banco_nivel_2,
    banco_nivel_3,
    banco_nivel_4,
    banco_nivel_5,
    banco_nivel_6,
    banco_nivel_7,
    banco_nivel_8,
    banco_nivel_9,
    banco_nivel_10
]