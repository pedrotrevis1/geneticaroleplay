import random
import time
import streamlit as st

cruz1_3 = [
'31 ',
'32 ',
'32 ',
'30 ',
'31 ',
'29 ',
'28 ',
'31 '
]

cruz1_1 = [
'9 ',
'8 ',
'8 ',
'11 ',
'9 ',
'11 ',
'12 ',
'9 '
]

cruz2_3 = [
'71 ',
'139 ',
'386 ',
'109 ',
'767 ',
'887 ',
'193 ',
'157 '
]

cruz2_1 = [
'21 ',
'37 ',
'94 ',
'39 ',
'233 ',
'345 ',
'79 ',
'44 '
]

interesseAnterior = [
'...',
'As maçãs',
'O milharal',
'As ervilhas do jardim',
'As moscas da cozinha',
'As formigas do jardim',
'O bolor dos alimentos',
'Os coelhos dos campos'
]

coisas=[
'maçãs ',
'grãos de milho ',
'ervilhas ',
'moscas ',
'larvas de formiga ',
'bolores ',
'coelhos '
]

carac=[
'vermelhas ',
'verdes',
'pequeninos ',
'grandes e arredondados',
'amarelas ',
'verdes',
'com olhos brancos ',
'com olhos vermelhos',
'compridas ',
'arredondadas',
'brancos ',
'marrons',
'rajados ',
'vermelhos'
]

c1 = random.randint(0,7)
c2 = random.randint(0,7)

st.title('Descobrindo a Genética')
st.caption('Parabéns! Então pelo jeito vocês já desvendaram que algumas características ficam em "recesso" enquanto outras "dominam"!')

st.write('Vocês já tem uma suspeita da razão pela qual aquela primeira geração resultado do cruzamento das linhagens puras foi a de iguais a um dos pais. '+'\n')
time.sleep(4)

st.session_state.interesse = st.selectbox('O que vocês observaram na etapa anterior?',interesseAnterior,index=0)

if st.session_state.interesse == interesseAnterior[1]:
    st.session_state.coisasA = coisas[0]
    st.session_state.carac1 = carac[0]
    st.session_state.carac2 = carac[1]
elif st.session_state.interesse == interesseAnterior[2]:
    st.session_state.coisasA = coisas[1]
    st.session_state.carac1 = carac[2]
    st.session_state.carac2 = carac[3]
elif st.session_state.interesse == interesseAnterior[3]:
    st.session_state.coisasA = coisas[2]
    st.session_state.carac1 = carac[4]
    st.session_state.carac2 = carac[5]
elif st.session_state.interesse == interesseAnterior[4]:
    st.session_state.coisasA = coisas[3]
    st.session_state.carac1 = carac[6]
    st.session_state.carac2 = carac[7]
elif st.session_state.interesse == interesseAnterior[5]:
    st.session_state.coisasA = coisas[4]
    st.session_state.carac1 = carac[8]
    st.session_state.carac2 = carac[9]
elif st.session_state.interesse == interesseAnterior[6]:
    st.session_state.coisasA = coisas[5]
    st.session_state.carac1 = carac[10]
    st.session_state.carac2 = carac[11]
elif st.session_state.interesse == interesseAnterior[7]:
    st.session_state.coisasA = coisas[6]
    st.session_state.carac1 = carac[12]
    st.session_state.carac2 = carac[13]

if st.session_state.interesse == '...':
    st.stop()

time.sleep(3)
st.write('Cruzando os indivíduos desta primeira geração de "filhos", vocês ficam espantados ao ver que nasceram '+cruz1_3[c1]+st.session_state.coisasA+st.session_state.carac1+'e '+cruz1_1[c1]+st.session_state.carac2+'! Igual aos "avós"! '+'\n')
time.sleep(4)
st.write('Vocês resolvem refazer esta etapa, cruzando mais indivíduos desta primeira geração, mas agora esperando mais tempo para obter uma prole ainda maior. '+'\n')
time.sleep(3)
st.write('Do resultado deste teste, vocês encontram '+cruz2_3[c2]+st.session_state.coisasA+st.session_state.carac1+'e '+cruz2_1[c2]+st.session_state.carac2+'!'+'\n'+'\n')
time.sleep(4)
st.subheader('Como é possível que as características que sumiram na primeira geração tenham ressurgido agora com os "netos" dos indivíduos originais?'+'\n')
st.subheader('Quais conclusões vocês tiram sobre a relação entre pais e filhos na passagem de características durante o cruzamento? (Como as características são passadas dos pais para os filhos?)')