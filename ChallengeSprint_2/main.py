# No 2º challenge sprint da disciplina de Cognitive CyberSecurity nós implementaremos na prática um pipeline de cibersegurança, perpassando por prevenção e identificação de fraude e propensão a cancelamento da compra.
#
# PROBLEMA
#
# Imagine que um cliente faça uma compra de um item como, por exemplo, computador ou celular. O item é devidamente entregue, mas o usuário afirma que não. Como podemos garantir a entrega do produto?
#
# ATIVIDADE
#
# Vocês deverão criar uma interface web usando Streamlit e NGROK que simula seu processo de MITIGAÇÃO DE FRAUDE.
#
# ENTREGA
#
# Vocês deverão entregar um pdf com o link para uma documentação resumida e para teste no NGROK.
#
# ATENÇÃO
#
# Não é necessário criar um modelo, você pode pensar numa estratégia, por exemplo, de código de recebimento usando Streamlit.

import streamlit as st
import pandas as pd
import csv
import time
from pyngrok import ngrok

http_tunnel = ngrok.connect()

st.set_page_config(page_title="Controle de entrega BASF", page_icon=":shark:")

dados_produtos = pd.DataFrame({
    'id': ['BASF01002', 'BASF02032'],
    'Nome produto': ['Insumos Vermifugos', 'Insumos para lavagem animal'],
    'Quantidade': [1, 1],
    'Preço unitário': ['RS 12.999,00', 'RS 5.270,00'],
    'Valor da compra': ['RS 12.999,00', 'RS 5.270,00'],
    'Data e hora da compra': ['06/15/2022 às 19:30:41', '06/15/2022 às 19:30:41'],
})

dados_comprador = pd.DataFrame({
    'id': ['01002'],
    'Nome': ['Augusto'],
    'Sobrenome': ['Rezende'],
    'RG': ['29.557.865-9'],
    'CPF': ['123.456.789-00'],
    'Empresa': ['Deep Security LTDA'],
    'CNPJ': ['10.782.001/0002-88'],
    'Logradouro': ['Rua dos Agronomos'],
    'Numero': ['05'],
    'Complemento': ['Cj. 101'],
    'CEP': ['98800-000'],
    'Cidade': ['São Paulo'],
    'Estado': ['SP'],
})

def send_form():
    with open('data/dados_recebedor.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)
        if input_buyer_same:
            writer.writerow(['01002', input_code_delivery, ['BASF01002', 'BASF02032'], '01002', 'Augusto', 'Rezende', '29.557.865-9', '123.456.789-00', 'Deep Security LTDA', '10.782.001/0002-88', 'Rua dos Agronomos', '05', 'Cj. 101', '98800-000', 'São Paulo', 'SP', '-23.550520, -46.633308', '06/15/2022 às 19:30:41', digital_sign, file_string])
        else:
            writer.writerow(['01002', input_code_delivery, input_code_delivery, ['BASF01002', 'BASF02032'], '01002', input_receiver_first_name, input_receiver_last_name, input_id_receiver, input_street_receiver, input_number_receiver, input_complement_receiver, input_zipcode_receiver, input_city_receiver, input_state_receiver, '-23.550520, -46.633308', '06/15/2022 às 19:30:41', digital_sign, file_string])


st.title("Registro de entrega BASF")
code_delivery = 'BASF01002XDF'

st.subheader('Dados de compra')
st.write(dados_produtos)

st.subheader('Dados do comprador')
st.write(dados_comprador)

st.subheader('Dados do recebedor')
input_code_delivery = st.text_input("Código da entrega:")

input_buyer_same = st.checkbox('Recebedor é o mesmo que comprador? (Usar dados do comprador)', value=True)

if not input_buyer_same:
    input_receiver_first_name = st.text_input("Nome:")
    input_receiver_last_name = st.text_input("Sobrenome:")

    input_select_receiver = st.selectbox(
        label='Escolha um documento de identificação do recebedor:',
        options=['Selecione um tipo de documento:', 'RG', 'CPF', 'CNPJ'])
    if input_select_receiver == 'RG':
        input_id_receiver = st.text_input("Digite o RG:")
    elif input_select_receiver == 'CPF':
        input_id_receiver = st.text_input("Digite o CPF:")
    elif input_select_receiver == 'CNPJ':
        input_id_receiver = st.text_input("Digite o CNPJ:")

    input_street_receiver = st.text_input("Logradouro:")
    input_number_receiver = st.text_input("Número:")
    input_complement_receiver = st.text_input("Complemento:")
    input_zipcode_receiver = st.text_input("CEP:")
    input_city_receiver = st.text_input("Cidade:")
    input_state_receiver = st.text_input("Estado:")

uploaded_file = st.file_uploader("Selecionar documento", type=['png', 'jpg', 'jpeg'])

digital_sign = st.text_area('Assinatura digital do recebedor', '')

input_agree_delivery = st.checkbox('Li e concordo com os termos de entrega')
input_agree_data_delivery = st.checkbox('Confirmo que todos os dados acima são verdadeiros')

input_button_submit = st.button("Registrar entrega")

if input_button_submit:
    if not input_code_delivery:
        st.error("Por favor, digite o código da entrega")
    if not input_agree_delivery and not input_agree_data_delivery:
        st.error('Você deve aceitar os termos de entrega e de data de entrega')
    else:
        send_form()
        with st.spinner('Enviando, aguarde...'):
            time.sleep(5)
        st.balloons()
        st.success('Entrega registrada com sucesso')