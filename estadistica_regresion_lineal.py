#Processes a file called "datasets", which should contain columns of data
#separated by blank spaces, and calculates lineal regresion data (slope, intercept,
#covariance, X and Y variances, Pearson correlation coefficient and value estimation
#for Y values corresponding to certain Xi values.

def CalcularPromedio(dataset):
    total=0
    for valor in dataset:
       total+=valor
    return total/len(dataset)

def getPromedios(dataset, xiyi,i,proms):
    promedio=CalcularPromedio(dataset)
    proms.append(promedio)
    for j in range(len(dataset)):
        xiyi[i][j]=float("{:.2f}".format(dataset[j]-promedio))
    print(xiyi[i])

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
                list[i].append(float(column))

                i+=1
    return list

def getRegresion(xiyi, yxx2, tam, covarianza, varianzax, varianzay):
    for m in range(tam):
        varianzay+=float(xiyi[1][m]**2)
    for j in range(tam):
        yxx2[1][j]=float(xiyi[0][j]*xiyi[1][j])
        yxx2[0][j]=float(xiyi[0][j]*xiyi[0][j])
    x=float(sum(yxx2[0]))
    y=float(sum(yxx2[1]))
    print()
    print("yi-y*xi-x, xi-x2")
    print(yxx2[1])
    print(yxx2[0])
    print()
    print("yi-y*xi-x", y)
    print("xi-x2", x)
    pendiente=y/x
    covarianza=y/tam
    varianzax=x/tam
    varianzay/=tam
    print()
    print("covarianza: ", covarianza)
    print("varianza x: ", varianzax)
    print("varianza y: ", varianzay)
    print("coeficiente de correlacion de Pearson: ", covarianza/((varianzax*varianzay)**(1/2)))
    print()
    return pendiente

def ProcessDataSets():
    list=DatasetsSplitter()
    xiyi=list
    yxx2=xiyi
    i=0
    tam=0
    covarianza=0
    varianzay=0
    varianzax=0
    proms=[]
    print("xi-x, yi-y")
    for dataset in list:
        getPromedios(dataset,xiyi,i,proms)
        i+=1
        tam=len(dataset)
    ordenada=0
    pendiente=getRegresion(xiyi, yxx2,tam, covarianza, varianzax, varianzay)
    ordenada=proms[1]-(proms[0]*pendiente)
    print("pendiente: ", pendiente," ordenada: ", ordenada)
    print()
    x=-1
    while(x!=0):
        x=float(input("ingrese valor a estimar (o cero para finalizar): "))
        if x!=0:
            print(ordenada+(pendiente*x))

#main execution
try:
    ProcessDataSets()
except:
    print("Error al procesar archivo, verifique los datos y formato del archivo datasets")
