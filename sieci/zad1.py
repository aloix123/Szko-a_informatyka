def getdata():# automatyczne wczytanie mam w pliku input.txt jak coś
    x=input("podaj adress ip")
    print()
    y=input("podaj maskę")
    return x,y
byte_lengh=8
def rotatestring(regularword):
    return regularword[::-1]
def change_from_decimal_tobinary_list(binarynumber):
    dividet_number_list_of_decimal=list(map(int,binarynumber.split(".")))
    result_number=[]
    global  byte_lengh
    for partnumber in dividet_number_list_of_decimal:
        numberformer=""
        part_number_copy=partnumber
        for bit in range(byte_lengh):
            restdivizion=part_number_copy%2
            numberformer+=str(restdivizion)
            part_number_copy=part_number_copy//2
        numberformer=rotatestring(numberformer)
        result_number.append(numberformer)

    return result_number
def Test():

    assert change_from_decimal_tobinary_list("192.168.1.145")==['11000000', '10101000', '00000001', '10010001']
    assert change_from_decimal_tobinary_list("255.255.255.128") == ['11111111', '11111111', '11111111', '10000000']

    #print("Tests OK")
def comparemaskwithadressip(adressip, mask):
    global byte_lengh
    resultNetworkadress=[]
    numberparts=8
    indexparts=4
    for index in range(indexparts):
        indexnumber=""

        for bitindex in range(numberparts):
            if adressip[index][bitindex]=='1' and mask[index][bitindex]=='1':
                indexnumber+="1"
            else:
                indexnumber += "0"

        resultNetworkadress.append(indexnumber)

    return resultNetworkadress
def makefinalstring(messege,finaldecimallist):
    return f"{messege}{finaldecimallist[0]}.{finaldecimallist[1]}.{finaldecimallist[2]}.{finaldecimallist[3]}"
def change_frombinary_to_decimal(binarynumber):
    resultlist=[]

    for numberpart in binarynumber:
        partlen = 7
        startfactor=0
        numberform=0
        while partlen>-1:
            if numberpart[partlen]=='1':
                numberform+=2**startfactor
            startfactor+=1
            partlen-=1
        resultlist.append(numberform)
    return resultlist

def getNetworkAdress(adressip,mask):

    binary_adress_ip = change_from_decimal_tobinary_list(adressip)
    binary_mask = change_from_decimal_tobinary_list(mask)

    networkadress = comparemaskwithadressip(binary_adress_ip, binary_mask)
    finalnumber = change_frombinary_to_decimal(networkadress)
    finalstring = makefinalstring("adres sieci: ",finalnumber)
    print(finalstring)
    return 0
def getBroadcast(adressip,mask):
    binary_adress_ip = change_from_decimal_tobinary_list(adressip)
    binary_mask = change_from_decimal_tobinary_list(mask)
    resultbrodcastbinarylist=setbroadcast(binary_adress_ip,binary_mask)
    finalnumber = change_frombinary_to_decimal(resultbrodcastbinarylist)
    finalstring = makefinalstring("adres rozgłoszeniowy: ", finalnumber)
    print(finalstring)
    return 0
def setbroadcast(adressip, mask):
    resultBroadcastlist=[]
    for part in range(4):
        newbroadcastpart = ""
        for index in range(byte_lengh):

            if mask[part][index]=='1':
                newbroadcastpart+=adressip[part][index]
            elif mask[part][index] == '0':
                newbroadcastpart += "1"
        resultBroadcastlist.append(newbroadcastpart)


    return resultBroadcastlist
def count0FromMask(mask):
    resultnumber=0
    for part in mask:
        for bit in part:

            if bit=="0":
                resultnumber+=1
    return resultnumber

def showFirstHostIp(mask):
    newmask=list(mask.split("."))
    newmask[3]=str(int(newmask[3])+1)
    print(makefinalstring("pierszy host: ",newmask))
    return 0
def showLastHostIp(mask):
    newmask = list(mask.split("."))
    newmask[3] = "254"
    print(makefinalstring("ostatni host: ", newmask))
    return 0
def countNumbersOfHost(mask):
    binary_mask = change_from_decimal_tobinary_list(mask)
    print("liczba hostów: "+str(2**count0FromMask(binary_mask)-2))
    return 0
adressip, mask = getdata()
print()
Test()
getNetworkAdress(adressip,mask)
getBroadcast(adressip, mask)
countNumbersOfHost(mask)
showFirstHostIp(mask)
#TODO zad 2 ,3 i spraw żę nie będziesz potrzebował tworzyć i kopjować funkcji