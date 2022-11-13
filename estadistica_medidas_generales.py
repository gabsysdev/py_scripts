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

def getResults(list, i):
    media=CalcularMedia(list)
    mediana=CalcularMediana(list)
    promedio=CalcularPromedio(list)
    desvio=CalcularDesvioEstandar(list, media)
    pearson=desvio/media
    print("Dataset", i, ":")
    print("elementos en el set: ", len(list), " min: ", min(list), " max: ", max(list), " rango: ", max(list)-min(list), " promedio: ", promedio, " desvio: ", desvio, " media: ", media, " mediana: ", mediana, " coeficienteVariacion: ", pearson)
    print("")

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

list=DatasetsSplitter()
i=1
for dataset in list:
    getResults(dataset,i)
    i+=1
