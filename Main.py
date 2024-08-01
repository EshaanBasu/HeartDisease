import pandas as pd
import numpy as np
import os

hd = pd.read_table('heart_2020_cleaned.csv', sep = ',')
# print(hd['BMI'].mean())

# function for getting yes/no proportions
def getData(data):
    noCount = 0
    yesCount = 0
    for i in range(len(data)):
        if data[i] == 'Yes':
            yesCount = yesCount + 1
        if data[i] == 'No':
            noCount = noCount + 1
    return np.array([[data.name, yesCount, noCount, (yesCount/(yesCount + noCount))]])

# function for getting numerical data
def getStats(data):
    statList = np.array([[data.name, data.mean(), data.median() , data.mode(), data.min(), data.max(), data.max() - data.min() , data.std(), data.var(), data.quantile(.25), data.quantile(.75)]], dtype = object)
    return statList

# getting y/n data
def binData(datfram):
    binArr = np.empty((1,4), dtype = object)
    for col in datfram.columns.values.tolist():
        if datfram[col][0] == 'Yes' or hd[col][0] == 'no':
            #print(col)
            currData1 = getData(datfram[col])
            binArr = np.concatenate((binArr, currData1), axis = 0)
            #print(currData1)
    binDF = pd.DataFrame(binArr, columns = ['stat','yes', 'no', 'percent yes'])
    binDF = binDF.drop(0, axis = 'rows')
    return binDF


# getting numercal data
def numData(datfram):
    statArr = np.empty((1,11), dtype = object)
    for col in datfram.columns.values.tolist():
        if isinstance(datfram[col][0], float):
            currData2 = getStats(datfram[col])
            statArr = np.concatenate((statArr, currData2), axis = 0)
    
    statDF = pd.DataFrame(statArr, columns = ['measurement','mean', 'median', 'mode', 'min', 'max', 'range','std', 'var', '25th percentile', '75th percentile'])
    statDF = statDF.drop(0, axis = 'rows')
    return statDF



def dataGiven(colName, option):
    newDF = hd[hd[colName] == option]
    newDF = newDF.reset_index(drop=True)
    return(newDF)


# Null value analysis
for col in hd.columns.values.tolist():
    for entry in hd[col]:
       if entry is None:
           print(col + ': ' + entry)

# writing CSVs
#Correlation Matrix Folder
corrFolderPath = '/home/eshaanbasu/PycharmProjects/HeartStatistics/CorrelationMatrices'
mainFolderPath = (corrFolderPath, 'mainCM.csv')
HeartDiseaseCorrFile = os.path.join(corrFolderPath, 'HeardDiseaseCM.csv')
SmokingCorrFile = os.path.join(corrFolderPath,'Smoking.csv')
AlcoholCorrFile = os.path.join(corrFolderPath,'AlcoholCM.csv')
StrokeCorrFile = os.path.join(corrFolderPath,'StrokeCM.csv')
DiffWalkCorrFile = os.path.join(corrFolderPath,'DiffWalkingCM.csv')
SexCorrFile = os.path.join(corrFolderPath,'SexCM.csv')

# CMmain = hd.corr(numeric_only= True)
# CMmain.to_csv((mainFolderPath))

CMsex = dataGiven('Sex', 'Male').corr(numeric_only= True)
CMsex.to_csv((SexCorrFile))

CMhd = dataGiven('HeartDisease', 'Yes').corr(numeric_only= True)
CMhd.to_csv((HeartDiseaseCorrFile))

CMsmoking = dataGiven('Smoking', 'Yes').corr(numeric_only= True)
CMsmoking.to_csv((SmokingCorrFile))

CMalcohol = dataGiven('AlcoholDrinking', 'Yes').corr(numeric_only= True)
CMalcohol.to_csv((AlcoholCorrFile))

CMstroke = dataGiven('Stroke', 'Yes').corr(numeric_only= True)
CMstroke.to_csv((StrokeCorrFile))

CMdw = dataGiven('DiffWalking', 'Yes').corr(numeric_only= True)
CMdw.to_csv((DiffWalkCorrFile))

# Condtional Data

condFolderPath = '/home/eshaanbasu/PycharmProjects/HeartStatistics/ConditionalData'

mainQual = os.path.join(condFolderPath, 'mainCQ.csv')
mainNum = os.path.join(condFolderPath, 'mainCN.csv')
numData(hd).to_csv(mainNum)
binData(hd).to_csv(mainNum)

mainQual = os.path.join(condFolderPath, 'mainCQ.csv')
mainNum = os.path.join(condFolderPath, 'mainCN.csv')
numData(hd).to_csv(mainNum)
binData(hd).to_csv(mainNum)

# pairwise correlation
numData(dataGiven('Sex', 'Male')).to_csv(os.path.join(condFolderPath, 'male.csv'))
numData(dataGiven('Sex', 'Female')).to_csv(os.path.join(condFolderPath, 'female.csv'))

numData(dataGiven('HeartDisease', 'Yes')).to_csv(os.path.join(condFolderPath, 'yHeartDiseasecsv'))
numData(dataGiven('HeartDisease', 'No')).to_csv(os.path.join(condFolderPath, 'nHeartDisease.csv'))

numData(dataGiven('AlcoholDrinking', 'Yes')).to_csv(os.path.join(condFolderPath, 'yAlcoholDrinking.csv'))
numData(dataGiven('AlcoholDrinking', 'No')).to_csv(os.path.join(condFolderPath, 'nAlcoholDrinking.csv'))

numData(dataGiven('Smoking', 'Yes')).to_csv(os.path.join(condFolderPath, 'ySmoking.csv'))
numData(dataGiven('Smoking', 'No')).to_csv(os.path.join(condFolderPath, 'nSmoking.csv'))

numData(dataGiven('Stroke', 'Yes')).to_csv(os.path.join(condFolderPath, 'yStroke.csv'))
numData(dataGiven('Stroke', 'No')).to_csv(os.path.join(condFolderPath, 'nStroke.csv'))

numData(dataGiven('DiffWalking', 'Yes')).to_csv(os.path.join(condFolderPath, 'yDiffWalking.csv'))
numData(dataGiven('DiffWalking', 'No')).to_csv(os.path.join(condFolderPath, 'nDiffWalking.csv'))

