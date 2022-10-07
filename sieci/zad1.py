def getdata():
    x=input("podaj adress ip")
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
def makefinalstring(finaldecimallist):
    return f"{finaldecimallist[0]}.{finaldecimallist[1]}.{finaldecimallist[2]}.{finaldecimallist[3]}"
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
Test()
adressip,mask=getdata()
binary_adress_ip=change_from_decimal_tobinary_list(adressip)
binary_mask=change_from_decimal_tobinary_list(mask)


networkadress=comparemaskwithadressip(binary_adress_ip, binary_mask)
finalnumber=change_frombinary_to_decimal(networkadress)
finalstring=makefinalstring(finalnumber)
print(finalstring)

#TODO zad 2 ,3 i spraw żę nie będziesz potrzebował tworzyć i kopjować funkcji