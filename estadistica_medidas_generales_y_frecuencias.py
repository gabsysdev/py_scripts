#Processes a file called "datasets", which should contain columns of data
#separated by blank spaces, and calculates general statistics measurements (sample
#lenght, min, max, range, average, standard deviation, mean, median, variant coeficient),
#and frequencies(intervals, absolut, relative, accumulated, accumulated relative)

#Math import to calculate log10
import math

#MEASUREMENTS CALCULATION
def CalcularMedia(list):
    media=0
    for number in list:
        media+=number
    return media/len(list)

def CalcularMediana(list):
    mediana=0
    lenn2=int(len(list)/2)
    lenn=int(lenn2-1)
    list.sort()
    if(len(list)%2==0):
        med1=list[lenn]
        med2=list[lenn2]
        mediana=(med1+med2)/2
    else:
        mediana=list[lenn2]
    return mediana

def CalcularDesvioEstandar(list, media):
    sumatoria=0

    for valor in list:
        sumatoria+=(valor-media)**2
    desvio=sumatoria/(len(list)-1)
    return desvio**0.5

def CalcularPromedio(list):
    total=0
    for valor in list:
        total+=valor
    return total/len(list)

def CalcularMin(list):
    min=9999999999
    for valor in list:
        if valor<min:
            min=valor
    if min==9999999999:
        return -1
    else:
        return min

#FREQUENCIES CALCULATION
def CalcularAbsoluta(intervalo, intervalob, list):
    cant=0
    for valor in list:
        if (valor > intervalo) and (valor <= intervalob):
            cant+=1
    return cant

def CalcularFreqs(list, sturges, tamClase, n):
    print("Intervalo  |  Absoluta   |  Relativa  |  Acumulada  |  AcumuladaRelativa")
    intervalo=min(list)
    intervalob=intervalo+tamClase
    acumulada=0
    relativa=0
    relAcumulada=0
    for i in range(0, sturges):
        if i==sturges-1:
            intervalob=max(list)
        absoluta=CalcularAbsoluta(intervalo, intervalob, list)
        if i==0:
            absoluta+=1
        acumulada+=absoluta
        relativa=100*(absoluta/n)
        relAcumulada+=100*(absoluta/n)
        print(intervalo, "-", intervalob, "|",absoluta, "|","%.2f"%relativa,"%", "|",acumulada, "|","%.2f"%relAcumulada,"%")
        intervalo+=tamClase
        intervalob+=tamClase
        i+=1

def getFreqs(list, n, media, desvio, rango):
    sturges=1+int(3.3*math.log(n,10))
    tamClase=int(rango/sturges)
    print("clases: :", sturges, ", intervalos de: ",tamClase)
    CalcularFreqs(list, sturges, tamClase, n)

    
#EXECUTE STATISTICS MEASUREMENTS AND FREQUENCIES
def getResults(list, i):
    media=CalcularMedia(list)
    mediana=CalcularMediana(list)
    promedio=CalcularPromedio(list)
    desvio=CalcularDesvioEstandar(list, media)
    pearson=desvio/media
    rango=max(list)-min(list)
    tamMuestra=len(list)
    print("Dataset", i, ":")
    #Print medidas generales de la muestra
    print("elementos en el set: ", tamMuestra, " min: ", min(list), " max: ", max(list), " rango: ", rango, " promedio: ", promedio, " desvio: ", desvio, " media: ", media, " mediana: ", mediana, " coeficienteVariacion: ", pearson)
    #print(len(list),min(list),max(list),rango,promedio,desvio,media,mediana,pearson)
    #Print tabla de frecuencias
    getFreqs(list, tamMuestra, media, desvio, rango)
    print("")

    
#FILE PROCESSING AND DATA INGESTING
def DatasetsSplitter():
    list=[]
    splitted=[]
    datasets=0
    with open("datasets") as archivo:
        for linea in archivo:
            splitted=linea.split("\t")
            i=0
            datasets=len(splitted)
            for x in range(0, len(splitted)):
                list.append([])
            break
    splitted=[]
    with open("datasets") as archivo:
        for linea in archivo:
            splitted=linea.split("\t")
            i=0
            for column in splitted:
                list[i].append(int(column))
                i+=1
    return list

#PROCESS ALL DATASETS
def ProcessDataSets():
    list=DatasetsSplitter()
    i=1
    for dataset in list:
        getResults(dataset,i)
        i+=1

#main execution
try:
    ProcessDataSets()
except:
    print("Error al procesar archivo, verifique los datos y formato del archivo datasets")
