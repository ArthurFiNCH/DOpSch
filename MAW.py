import csv
import time

with open('employee data.csv') as employeeData:
    decEmpData = csv.reader(employeeData, delimiter = ',')
    EmpNames = []
    EmpSNames = []
    EmpPositions = []
    EmpBDatas = []
    for row in decEmpData:
        EmpName = row[0]
        EmpSName = row[1]
        EmpPosition = row[2]
        EmpBData = row[3]

        EmpNames.append(EmpName)
        EmpSNames.append(EmpSName)
        EmpPositions.append(EmpPosition)
        EmpBDatas.append(EmpBData)

tryy = 0

while True:
    if tryy >=1:
        NameOrSNameOfEmp = input('Czy chcesz przeszukać bazę danych ponownie? Jeśli tak, podaj ponownie imię lub nazwisko pracownika: \n')
        print('==========================================================================')
        if NameOrSNameOfEmp == 'Nie':
            exit('Program zamknięty.')
    elif tryy <1:
        NameOrSNameOfEmp = input('Podaj imię lub nazwisko pracownika: \n')
        print('==========================================================================')

    if NameOrSNameOfEmp in EmpNames:
        EmpNameIndex = EmpNames.index(NameOrSNameOfEmp)
        EmpSurName = EmpSNames[EmpNameIndex]
        EmpPos = EmpPositions[EmpNameIndex]
        EmpBDat = EmpBDatas[EmpNameIndex]
        print('Do podanego przez Ciebie imienia',NameOrSNameOfEmp,'pasują następujące informacje: \n'), time.sleep(2)
        print('Imię:',NameOrSNameOfEmp), time.sleep(1)
        print('Nazwisko:',EmpSurName), time.sleep(1)
        print('Stanowisko:',EmpPos), time.sleep(1)
        print('Data urodzenia:',EmpBDat), time.sleep(1)
        print('==========================================================================')
    elif NameOrSNameOfEmp in EmpSNames:
        EmpSurNameIndex = EmpSNames.index(NameOrSNameOfEmp)
        EmpNameF = EmpNames[EmpSurNameIndex]
        EmpPos = EmpPositions[EmpSurNameIndex]
        EmpBDat = EmpBDatas[EmpSurNameIndex]
        print('Do podanego przez Ciebie nazwiska',NameOrSNameOfEmp,'pasują następujące informacje: \n'), time.sleep(2)
        print('Imię:',EmpNameF), time.sleep(1)
        print('Nazwisko:',NameOrSNameOfEmp), time.sleep(1)
        print('Stanowisko:',EmpPos), time.sleep(1)
        print('Data Urodzenia:',EmpBDat), time.sleep(1)
        print('==========================================================================')
    elif NameOrSNameOfEmp is not EmpNames or EmpSNames or EmpPositions or EmpBDatas:
        print('Takiego imienia lub nazwiska nie ma w bazie danych, spróbuj ponownie...')

    tryy += 1
