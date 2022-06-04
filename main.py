# pip install streamlit
import streamlit as st
from functions import *

Quest1 = "1-Importer le fichier « WaterQuality.xlsx » avec le module pandas, nommer le df et explorer son contenu"
code_Question1 = '''# pip install pandas
import pandas as pd

def Question1(filename):
    df = pd.read_excel(filename)
    return df
     '''

Quest2 = '''2- Calculer pour chaque point (P1→P9) pour les 2 années 2016 et 2017 l’indice WAWQI
selon l’équation décrite dans la section 2.1 A, et ajouter une colonne à df qui contient les
valeurs de WAWQI pour chaque point (Notez que le paramètre FC n’entre pas deans le
calcul)
'''
code_Question2 = '''def WAWQI(Ci,wi,Si):
    Wi=wi/45
    Qi = ((Ci/Si)*100)
    WQI=Wi*Qi
    return WQI

def WAWQIpH(Cph,wi):
    Wi = wi / 45
    Qi=(Cph-8.5)/(6.5-8.5)
    WQIph = Wi * Qi
    return WQIph


def Question2(year):
    df = Question1('WaterQuality1.xlsx')
    df = df.loc[df['Year'] == year]  # pour chaque point (P1→P9) <=> Year = 2016
    myList = [(df.Temperature, 30, 1), (df.DCO, 90, 3), (df.DBO5, 3, 4), (df.O2_DISSOUS, 5, 5),
              (df.CONDUCTIVITE, 1000, 4), (df.MES, 20, 2), (df.TURBIDITE, 5, 2), (df.NITRITE, 0.5, 5),
              (df.NITRATE, 50, 5), (df.AMMONIUM, 0.5, 5), (df.PHOSPHATE, 5, 5)]

    WAWQI1 = WAWQIpH(df.pH,4)

    for i in myList:
        WAWQI1 = WAWQI1 + WAWQI(i[0],i[2],i[1])
        
    df['WAWQI'] = WAWQI1

    return df[['Year','POINTS','WAWQI']]
 '''

Quest3 = '''3- Selon les différents cas décrits dans 2.1 B, donner la qualité qui correspond à chaque
valeur de WAWQI, et ajouter une colonne à df qui contient la qualité pour chaque point.'''
code_Question3 = '''def Quality_results(WAWQi):
    if WAWQi < 50:
        return 'Excellent Water'
    elif WAWQi >= 50 and WAWQi<=100:
        return "Good Water"
    elif WAWQi >= 101 and WAWQi<=200:
        return 'Poor Water'
    elif WAWQi >= 201 and WAWQi<=300:
        return "Very Poor Water"
    elif WAWQi > 300:
        return "Unsuitable for drinking"

def Question3(year):
    df = Question2(year)
    list_des_qualités = [Quality_results(x) for x in df['WAWQI']]
    df['Quality '] = list_des_qualités
    return df '''

Quest4 = '''4-Importer une autre fois le fichier « WaterQuality.xlsx » avec le module pandas, nommer le df1.'''
code_Question4 = '''# pip install pandas
import pandas as pd

def Question4(filename):
    df1 = pd.read_excel(filename)
    return df1'''

Quest5 = '''5- Calculer pour chaque point (P1→P9) pour les 2 années 2016 et 2017 l’indice WGWQI
selon l’équation décrite dans la section 2.2 A, et ajouter une colonne à df1 qui contient les valeurs de WGWQI pour 
chaque point point (Notez que le paramètre FC n’entre pas deans le calcul)'''
code_Question5 = '''def WGWQI(Ci,wi,Si):
    Wi = wi / 45
    Qi=  ((Ci / Si) * 100)
    WGWQi=Qi**Wi
    return WGWQi

def WGWQIph(Cph,wi):
    Wi = wi / 45
    Qi = (Cph - 8.5) / (6.5 - 8.5)
    WGWQiph=Qi**Wi
    return WGWQiph

def Question5(year,):
    df1 = Question4('WaterQuality1.xlsx')
    df1 = df1.loc[df1['Year'] == year]  # pour chaque point (P1→P9) <=> Year = 2016
    myList = [(df1.Temperature, 30, 1), (df1.DCO, 90, 3), (df1.DBO5, 3, 4), (df1.O2_DISSOUS, 5, 5),
              (df1.CONDUCTIVITE, 1000, 4), (df1.MES, 20, 2), (df1.TURBIDITE, 5, 2), (df1.NITRITE, 0.5, 5),
              (df1.NITRATE, 50, 5), (df1.AMMONIUM, 0.5, 5), (df1.PHOSPHATE, 5, 5)]

    WGWQI1 = WGWQIph(df1.pH,4)
    for i in myList:
        WGWQI1 = WGWQI1 * WGWQI(i[0],i[2],i[1])

    df1['WGWQI'] = WGWQI1

    return df1[['Year','POINTS','WGWQI']]'''

Quest6 = '''6- Selon les différents cas décrits dans 2.2 B, donner la qualité qui correspond à chaque
valeur de WGWQI, et ajouter une colonne à df1 qui contient la qualité pour chaque point.'''
code_Question6 = '''def Quality_results_WGWQI(WGWQi):
    if WGWQi >= 90 and  WGWQi <= 100  :
        return "Excellent"
    elif WGWQi >= 70 and WGWQi <= 89:
        return "Good"
    elif WGWQi >= 50 and WGWQi <= 69:
        return 'Medium'
    elif WGWQi >= 25 and WGWQi <= 49:
        return "Bad"
    elif WGWQi >=0 and WGWQi <= 24:
        return "Very Bad"

def Question6(year):
    df1 = Question5(year)
    list_des_qualites = [Quality_results_WGWQI(x) for x in df1['WGWQI']]
    df1['QualiteWGWQI'] = list_des_qualites
    return df1'''

Quest7 = '''7-Importer une autre fois le fichier « WaterQuality.xlsx » avec le module pandas,nommer le df2.'''
code_Question7 = '''# pip install pandas
import pandas as pd

def Question7(filename):
    df2 = pd.read_excel(filename)
    return df2'''

Quest8 = '''8- Calculer pour chaque point (P1→P9) pour les 2 années 2016 et 2017 l’indice OWQI
selon l’équation décrite dans la section 2.3 A, et ajouter une colonne à df2 qui contient les
valeurs de OWQI pour chaque point (Il faut noter que dans pour OWQI, il faut travailler
seulement avec les 8 paramètres comme décrit dans 2.3 A)'''
code_Question8 = '''def SI(Ci,wi,Si):
    Wi=wi/45
    Qi = ((Ci / Si) * 100)
    SII= Wi*Qi
    return 1/(SII)**2

def SIph(Cph,wi):
    Wi=wi/45
    Qi = (Cph - 8.5) / (6.5 - 8.5)
    SIiph= Wi*Qi
    return 1/(SIiph)**2

def Question8(year,):
    df2 = Question7('WaterQuality1.xlsx')
    df2 = df2.loc[df2['Year'] == year]  # pour chaque point (P1→P9) <=> Year = 2016
    myList = [(df2.Temperature, 30, 1), (df2.DBO5, 3, 4), (df2.O2_DISSOUS, 5, 5),
              (df2.NITRATE, 50, 5), (df2.AMMONIUM, 0.5, 5), (df2.PHOSPHATE, 5, 5),(df2.FC,594,5)]

    SIph1 = SIph(df2.pH,4)
    for i in myList:
        SIph1 = SIph1 + SI(i[0],i[2],i[1])

    OWQI = (8/SIph1)**(1/2)
    df2['OWQI'] = OWQI

    return df2[['Year','POINTS','OWQI']]
'''

Quest9 = '''9- Selon les différents cas décrits dans 2.2 B, donner la qualité qui correspond à chaque
valeur de OWQI, et ajouter une colonne à df2 qui contient la qualité pour chaque point'''
code_Question9 = '''def Quality_results_OWQI(OWQI):
    if OWQI >= 90 and OWQI <= 100:
        return "Excellent"
    elif OWQI >= 85 and OWQI <= 89:
        return "Good "
    elif OWQI >= 80 and OWQI <= 84:
        return 'Fair'
    elif OWQI >= 60 and OWQI <= 79:
        return "Poor"
    elif OWQI >= 0 and OWQI <= 59:
        return "Very Poor"

def Question9(year):
    df2 = Question8(year)
    list_des_qualites = [Quality_results_OWQI(x) for x in df2['OWQI']]
    df2['QualiteOWQI'] = list_des_qualites
    return df2'''

Quest10 = '''10. Créer un pandas dataFrame df4 qui contient pour tous les points (P1→P9) pour les 2
années 2016 et 2017 seulment les valeurs des IQE (WAWQI, WGWQI et OWQI) ainsi que
les qualités correspondante.'''
code_Question10 = '''def Question10(df,year):
    df3 = Question3(year)
    df6 = Question6(year)
    df3.index = df6.index
    df3[['WGWQI', 'QualiteWGWQI']] = df6[['WGWQI', 'QualiteWGWQI']]
    df9 = Question9(year)
    df3.index = df9.index
    df3[['OWQI', 'QualiteOWQI']] = df9[['OWQI', 'QualiteOWQI']]
    df10 = df3
    return df10'''

# run straemlit
st.set_page_config(page_title="IQE-EIDIA", page_icon="📊", initial_sidebar_state="expanded")

with st.sidebar:
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("images/eidia_logo.png")
    with col3:
        st.image("images/uemf.jpeg")

    st.title('Préparé par : ')
    st.image("images/Imane_benchrif.jpeg")
    st.write('Imane BENCHRIF')
    st.image("images/imane_amaaz.PNG")
    st.write('Imane AMAAZ')
    st.title('Encadré par : Profs Taha AIT TCHAKOUCHT et Yasser EL MADMOUNE ')


def color_df(val,color):
    color = color if val else '#B3FD5F'
    return f'background-color: {color}'

def color_quality_WAWQI(val):
    color = '#FF4D4D' if val == 'Unsuitable for drinking' else '#FFADAD' if val == 'Very Poor Water' \
        else '#FA8C8C' if val == 'Poor Water' else '#F1F85A' if val == 'Good Water' else '#B3FD5F' if val == 'Excellent Water' else '#BEF8FC'
    return f'background-color: {color}'

def color_quality_WGWQI(val):
    color = '#FF4D4D' if val == 'Very Bad' else '#FFADAD' if val == 'Bad' \
        else '#FFB756' if val == 'Medium' else '#F1F85A' if val == 'Good' else '#BEF8FC'
    return f'background-color: {color}'

def color_quality_OWQI(val):
    color = '#FF4D4D' if val == 'Very Poor' else '#FFADAD' if val == 'Poor' \
        else '#FFB756' if val == 'Fair' else '#F1F85A' if val == 'Good' else '#B3FD5F' if val == 'Excellent' else '#BEF8FC'
    return f'background-color: {color}'

def color_quality_all(val):
    color = '#FF4D4D' if val == 'Very Poor' else '#FFADAD' if val == 'Poor' \
        else '#FFB756' if val == 'Fair' else '#F1F85A' if val == 'Good' else '#B3FD5F' if val == 'Excellent' else '#BEF8FC'
    return f'background-color: {color}'

#placeholder = st.empty()
st.markdown("<h1 style='text-align: center; color: #5AA7A7;'>Projet de fin de Semestre</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: #96D7C6;'>📊  Indices de Qualité de l’Eau (IQE, WQI)</h2>", unsafe_allow_html=True)

option = st.multiselect( "Indices de Qualité de l’Eau (par défaut l'indice WAWQI est sélectionné)",
    options=['WAWQI','WGWQI','OWQI'],
    help="Sélectionnez un indice de qualité de l'eau",
    default=['WAWQI'],
)
if "WAWQI" in option:
    with st.expander(Quest1):
        st.code(code_Question1, language='python')

    uploaded_file = st.file_uploader("Cliquez sur le bouton 'Browse Files' pour importer le fichier « WaterQuality.xlsx »", type=".xlsx",key = 'count0')
    if uploaded_file:
        df = Question1(uploaded_file)
        st.markdown("#### Aperçu des données")
        st.dataframe(df)

    agree = st.checkbox('Importer le fichier « WaterQuality.xlsx » implicitement')

    if agree:
        df = Question1('WaterQuality1.xlsx')
        st.markdown("#### Aperçu des données de df")
        st.dataframe(df)


    if uploaded_file or agree:
        with st.expander(Quest2):
            st.code(code_Question2, language='python')


        ab = st.selectbox("Choisissez 2016 ou 2017 pour calculer l'indice WAWQI", ('2016','2017'),key='key0')
        if ab == '2016':
            year = 2016
        else:
            year = 2017

        df2 = Question2(year)
        st.write("l'indice WAWQI pour l'année choisi : ")
        st.dataframe(df2.style.applymap(color_df, subset=['WAWQI'],color = '#6CBCBF'))

        with st.expander(Quest3):
            st.code(code_Question3, language='python')

        df3 = Question3(year)
        st.dataframe(df3.style.applymap(color_quality_WAWQI, subset=['QualiteWAWQI']))

if "WGWQI" in option:
    with st.expander(Quest4):
        st.code(code_Question4, language='python')

    uploaded_file = st.file_uploader("Cliquez sur le bouton 'Browse Files' pour importer le fichier « WaterQuality.xlsx »", type=".xlsx",key = 'count1')
    if uploaded_file:
        df1 = Question1(uploaded_file)
        st.markdown("#### Aperçu des données")
        st.dataframe(df1)

    agree = st.checkbox('Importer le fichier « WaterQuality.xlsx » implicitement',key='key0')

    if agree:
        df1 = Question1('WaterQuality1.xlsx')
        st.markdown("#### Aperçu des données de df1")
        st.dataframe(df1)


    if uploaded_file or agree:
        with st.expander(Quest5):
            st.code(code_Question5, language='python')


        ab = st.selectbox("Choisissez 2016 ou 2017 pour calculer l'indice WGWQI",('2016','2017'),key='key1')
        if ab == '2016':
            year = 2016
        else:
            year = 2017
        df5 = Question5(year)
        st.write("l'indice WGWQI pour l'année choisi : ")
        st.dataframe(df5.style.applymap(color_df, subset=['WGWQI'],color='#96D7C6'))

        with st.expander(Quest6):
            st.code(code_Question6, language='python')

        df6 = Question6(year)
        st.dataframe(df6.style.applymap(color_quality_WGWQI, subset=['QualiteWGWQI']))

if "OWQI" in option:
    with st.expander(Quest7):
        st.code(code_Question7, language='python')

    uploaded_file = st.file_uploader("Cliquez sur le bouton 'Browse Files' pour importer le fichier « WaterQuality.xlsx »", type=".xlsx",key = 'count2')
    if uploaded_file:
        df2 = Question1(uploaded_file)
        st.markdown("#### Aperçu des données")
        st.dataframe(df2)

    agree = st.checkbox('Importer le fichier « WaterQuality.xlsx » implicitement',key='key2')

    if agree:
        df2 = Question1('WaterQuality1.xlsx')
        st.markdown("#### Aperçu des données de df2")
        st.dataframe(df2)


    if uploaded_file or agree:
        with st.expander(Quest8):
            st.code(code_Question8, language='python')


        ab = st.selectbox("Choisissez 2016 ou 2017 pour calculer l'indice WGWQI",('2016','2017'),key='key2')
        if ab == '2016':
            year = 2016
        else:
            year = 2017
        df9 = Question8(year)
        st.write("l'indice OWQI pour l'année choisi : ")
        st.dataframe(df9.style.applymap(color_df, subset=['OWQI'],color='#5AA7A7'))

        with st.expander(Quest9):
            st.code(code_Question9, language='python')

        df9 = Question9(year)
        st.dataframe(df9.style.applymap(color_quality_OWQI, subset=['QualiteOWQI']))

if 'WAWQI' in option and  'WGWQI' in option and 'OWQI' in option:
    if uploaded_file or agree:
        with st.expander(Quest10):
            st.code(code_Question10, language='python')

        ab = st.selectbox("Choisissez 2016 ou 2017 pour afficher les valeurs des IQE (WAWQI, WGWQI et OWQI) ansi que les qualités correspondante.", ('2016', '2017'), key='key3')
        if ab == '2016':
            year = 2016
        else:
            year = 2017

        df = Question1('WaterQuality1.xlsx')
        df10 = Question10(year)
        st.write("l'indice IQE (WAWQI, WGWQI et OWQI) pour l'année choisi : ")
        st.dataframe(df10)

