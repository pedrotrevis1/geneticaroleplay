import streamlit as st
import random
import time

st.title('Descobrindo a Genética')

import random
import time

grupo1 = [
'monges alemães no século XVIII. ',
'cientistas brasileiros do século XVIII. ', 
'curiosos das Ciências Naturais de um pequeno povoado mexicano do século XIX. ',
'estudantes do departamento de Biologia da grande Universidade de Quito, no Equador, no ano de 1867. ',
'parte de uma tribo semi-nômade atualmente estabelecida próxima de Jargalan, na Mongólia, no final do século XVIII. ',
'fazendeiros que dividem um pedaço de terra no sul da Itália, no início do século XIX. ',
'agrônomos pioneiros dos terrenos próximos a Huánuco, no Peru. ',
'naturalistas ingleses no final do século XVIII. '
]

grupo2 = [
'Na vida não há muito o que fazer além dos afazeres da igreja, e em conversas com seus colegas vocês acabam ficando ',
'É comum vocês realizarem grandes discussões acaloradas nas noites do laboratório, e numa dessas noites vocês se encontram ',
'Amigos de longa data, vocês gostam de realizar pequenos estudos a respeito da vila. Sugerido por um dos colegas, vocês ficam ',
'Num dos estudos em campo vocês estão discutindo os arredores do campus e ficam ',
'É sempre crucial conhecer os arredores do local onde vocês ficarão pelos próximos meses, e ao chegar no local vocês ficam ',
'Como se preocupam muito com seus próprios bocados de terreno, são várias as discussões sobre a natureza e seus arredores. Numa das discussões, vocês se encontram ',
'O ano é 1899, e a virada do século promete grandes novidades tecnológicas e científicas. Destinados a fazer parte destas descobertas, vocês se encontram ',
'Destinados a estudar os povoados próximos e suas relações naturais, vocês se encontram na cidade e, numa das principais discussões vocês ficam '
]






lugar = [
'do monastério. ',
'do laboratório. ',
'do povoado. ',
'da universidade. ',
'da tribo. ',
'das fazendas. ',
'da sede dos agrônomos. ',
'dos povoados. '
]

coisa = [
'cores das maçãs encontradas no pomar ',
'tamanhos dos grãos de milhos dos milharais das regiões próximas ',
'cores das ervilhas encontradas nas plantações próximas ',
'cores dos olhos de moscas que comumente sobrevoam a cozinha ',
'tamanho das larvas de formigas encontradas nos jardins ',
'cores dos bolores que insistem em aparecer nos alimentos esquecidos na cozinha ',
'pelagens dos coelhos que vivem nos campos próximos ',
]

caracCoisa = [
'É possível encontrar maçãs vermelhas e maçãs verdes por todo o pomar. ',
'É possível encontrar grãos de milho pequeninos e grãos grandes e arredondados por todo o milharal. ',
'É possível encontrar ervilhas amarelas e ervilhas verdes nas plantações. ',
'É possível identificar moscas com olhos brancos e moscas com olhos vermelhos pela cozinha. ',
'É possível identificar larvas de formigas compridas e larvas arredondadas pelos jardins. ',
'É possível encontrar bolor branco e bolor marrom nos alimentos da cozinha. ',
'É possível encontrar coelhos rajados e coelhos vermelhos pelos campos. '
]

coisasSao = [
'todas as maçãs que nasceram são vermelhas. ',
'todos os grãos de milho que nasceram são pequeninos. ',
'todas as ervilhas que nasceram são amarelas. ',
'todas as moscas que nasceram possuem olhos brancos. ',
'todas as larvas de formigas que nasceram são compridas. ',
'todos os bolores que cresceram são brancos. ',
'todos os coelhos que nasceram são rajados. '
]

nGrupo = random.randint(0,7)
nCoisa = random.randint(0,6)

st.write('Você e seu grupo são ' + grupo1[nGrupo] +'\n')
time.sleep(4)
st.write(grupo2[nGrupo]+'intrigados pelas diferentes ' + coisa[nCoisa] + lugar[nGrupo]+'\n')
time.sleep(4) 
st.write(caracCoisa[nCoisa]+'\n')
time.sleep(4)
st.write('Vocês resolvem então cruzar estes seres com características diferentes. '+'\n')
time.sleep(4)
st.write('Primeiramente vocês selecionam linhagem completamente puras há várias gerações e ficam surpresos que, deste primeiro cruzamento, '+ coisasSao[nCoisa]+'\n')
time.sleep(4)
st.write('Como é possível que isso aconteça, se os "pais" deste cruzamento possuem características tão diferentes?')