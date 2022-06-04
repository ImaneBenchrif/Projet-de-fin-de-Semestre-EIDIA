# pip install pandas
# pip install openpyxl
import pandas as pd

# Question 1: 1- Importer le fichier « WaterQuality.xlsx »
def Question1(filename):
    df = pd.read_excel(filename)
    return df

# Question 2: 2- Moyenne arithmétique pondérée (WAWQI)
def WAWQI(Ci,wi,Si):
    Wi=wi/45
    Qi = ((Ci/Si)*100)
    WQI=Wi*Qi
    return WQI

def WAWQIpH(Cph,wi):
    Wi = wi / 45
    Qi=(Cph-8.5)/(6.5-8.5)
    WQIph = Wi * Qi
    return WQIph

def Question2(df,year):
    df = df.loc[df['Year'] == year]  # pour chaque point (P1→P9) <=> Year = 2016
    myList = [(df.Temperature, 30, 1), (df.DCO, 90, 3), (df.DBO5, 3, 4), (df.O2_DISSOUS, 5, 5),
              (df.CONDUCTIVITE, 1000, 4), (df.MES, 20, 2), (df.TURBIDITE, 5, 2), (df.NITRITE, 0.5, 5),
              (df.NITRATE, 50, 5), (df.AMMONIUM, 0.5, 5), (df.PHOSPHATE, 5, 5)]

    WAWQI1 = WAWQIpH(df.pH,4)
    for i in myList:
        WAWQI1 = WAWQI1 + WAWQI(i[0],i[2],i[1])

    df['WAWQI'] = WAWQI1

    return df[['Year','POINTS','WAWQI']]

# Question 3 : 3- Ajouter une colonne à df qui contient la qualité pour chaque point.
def Quality_results(WAWQi):
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

def Question3(df,year):
    df = Question2(df,year)
    list_des_qualites = [Quality_results(x) for x in df['WAWQI']]
    df['QualiteWAWQI'] = list_des_qualites
    return df


# Question 4 : 4-Importer une autre fois le fichier « WaterQuality.xlsx » avec le module pandas,nommer le df1
def Question4(filename):
    df1 = pd.read_excel(filename)
    return df1

# Question 5: Moyenne Géométrique pondérée (WGWQI)
def WGWQI(Ci,wi,Si):
    Wi = wi / 45
    Qi=  ((Ci / Si) * 100)
    WGWQi=Qi**Wi
    return WGWQi

def WGWQIph(Cph,wi):
    Wi = wi / 45
    Qi = (Cph - 8.5) / (6.5 - 8.5)
    WGWQiph=Qi**Wi
    return WGWQiph

def Question5(df1,year,):
    df1 = df1.loc[df1['Year'] == year]  # pour chaque point (P1→P9) <=> Year = 2016
    myList = [(df1.Temperature, 30, 1), (df1.DCO, 90, 3), (df1.DBO5, 3, 4), (df1.O2_DISSOUS, 5, 5),
              (df1.CONDUCTIVITE, 1000, 4), (df1.MES, 20, 2), (df1.TURBIDITE, 5, 2), (df1.NITRITE, 0.5, 5),
              (df1.NITRATE, 50, 5), (df1.AMMONIUM, 0.5, 5), (df1.PHOSPHATE, 5, 5)]

    WGWQI1 = WGWQIph(df1.pH,4)
    for i in myList:
        WGWQI1 = WGWQI1 * WGWQI(i[0],i[2],i[1])

    df1['WGWQI'] = WGWQI1

    return df1[['Year','POINTS','WGWQI']]

# Question 6 : 6- Ajouter une colonne à df qui contient la qualité pour chaque point.
def Quality_results_WGWQI(WGWQi):
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

def Question6(df1,year):
    df1 = Question5(df1,year)
    list_des_qualites = [Quality_results_WGWQI(x) for x in df1['WGWQI']]
    df1['QualiteWGWQI'] = list_des_qualites
    return df1


# Question 7 : 7- Importer une autre fois le fichier « WaterQuality.xlsx » avec le module pandas, nommer le df2
def Question7(filename):
    df2 = pd.read_excel(filename)
    return df2

# Question 8 : L’indice Oregon de Qualité de l’eau (OWQI)
def SI(Ci,wi,Si):
    Wi=wi/45
    Qi = ((Ci / Si) * 100)
    SII= Wi*Qi
    return 1/(SII)**2

def SIph(Cph,wi):
    Wi=wi/45
    Qi = (Cph - 8.5) / (6.5 - 8.5)
    SIiph= Wi*Qi
    return 1/(SIiph)**2

def Question8(df2,year,):
    df2 = df2.loc[df2['Year'] == year]  # pour chaque point (P1→P9) <=> Year = 2016
    myList = [(df2.Temperature, 30, 1), (df2.DBO5, 3, 4), (df2.O2_DISSOUS, 5, 5),
              (df2.NITRATE, 50, 5), (df2.AMMONIUM, 0.5, 5), (df2.PHOSPHATE, 5, 5),(df2.FC,594,5)]

    SIph1 = SIph(df2.pH,4)
    for i in myList:
        SIph1 = SIph1 + SI(i[0],i[2],i[1])

    OWQI = (8/SIph1)**(1/2)
    df2['OWQI'] = OWQI

    return df2[['Year','POINTS','OWQI']]

# Question 9 : 6- Ajouter une colonne à df qui contient la qualité pour chaque point.
def Quality_results_OWQI(OWQI):
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

def Question9(df2,year):
    df2 = Question8(df2,year)
    list_des_qualites = [Quality_results_OWQI(x) for x in df2['OWQI']]
    df2['QualiteOWQI'] = list_des_qualites
    return df2

def Question10(df,year):
    df3 = Question3(df,year)
    df6 = Question6(df,year)
    df3.index = df6.index
    df3[['WGWQI', 'QualiteWGWQI']] = df6[['WGWQI', 'QualiteWGWQI']]
    df9 = Question9(df, year)
    df3.index = df9.index
    df3[['OWQI', 'QualiteOWQI']] = df9[['OWQI', 'QualiteOWQI']]
    df10 = df3
    return df10

