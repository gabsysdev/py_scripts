#Saves columns of datasets separated by blank spaces into sublists inside a list(with float format, line 24).
#file name should be "datasets", and should be something like:
#data1 data2 data3
#data4 data5 data6

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
