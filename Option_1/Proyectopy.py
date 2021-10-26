#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
#Codigo para el proyecto final de python, traducir el codigo ensamblador a codigo maquina

#Se ingresa el archivo que se examinara
inputt = input("Ingrese el nombre del archivo con su extension: ")
texto = open(inputt)
binaryList = [] #Lista que guardadara cada una de las converciones.
def comp2(dec):
    bina = bin(dec)
    new = ""
    flag = 0
    for i in range(len(bina)):
        num = bina[i]
        if num == "b":
            flag = 1
        elif flag == 1:
            if num == "1":
                num = "0"
            elif num == "0":
                num = "1"
            new += num
        else:
            pass
    nu = int(new, 2) + 1
    com2 = bin(nu)
    flag1 = 0
    new1 = ""
    for i in range(len(com2)):
        num1 = com2[i]
        if num1 == "b":
            flag1 = 1
        elif flag1 == 1:
            new1 += num1
    if len(new) != len(new1):
        while len(new) != len(new1):
            new1 = "0" + new1
    return new1


def decimal_a_binario(numero_decimal):
    numero_binario = 0
    multiplicador = 1

    while numero_decimal != 0:
        # se almacena el módulo en el orden correcto
        numero_binario = numero_binario + numero_decimal % 2 * multiplicador
        numero_decimal //= 2
        multiplicador *= 10

    return numero_binario


def agregar_ceros3b(numero_binario):
    tamaño = len(str(numero_binario))
    #se toma el valor del tamaño de el numero de la entrada
    num = str(numero_binario)
    #se agregan los ceros asta los 3 bits
    while tamaño < 3:
        num = "0" + num
        tamaño += 1
    return num


def agregar_ceros14b(numero_binario): 
    tamaño = len(str(numero_binario))
    num = str(numero_binario)
    while tamaño < 14:
        num = "0" + num
        tamaño += 1
    return num


def quitar_negativo(negativo):
    neg = negativo
    if negativo < 0:
        neg = neg * -1
    else:
        pass
    return neg

        
def agregar_ceros8b(numero_binario):
    tamaño = len(str(numero_binario))

    num = str(numero_binario)

    while tamaño < 8:
        num = "0" + num
        tamaño += 1
    return num


def agregar_unos8b(numero_binario):
    tamaño = len(str(numero_binario))

    num = str(numero_binario)

    while tamaño < 8:
        num = "1" + num
        tamaño += 1
    return num

           
def agregar_unos14b(numero_binario):
    tamaño = len(str(numero_binario))

    num = str(numero_binario)

    while tamaño < 14:
        num = "1" + num
        tamaño += 1
    return num


def create_output_file(list):
    file = open(inputt.split('.')[0]+"-output.txt", "w")
    for item in binaryList:
        file.write(item+"\n")
    file.close

#def deci_com2(nums):

find = 1
def separador(tex):
    findline = []
    for line in tex:
    
    #print(findpos)
    #se separan el string de la linea para poder eliminar datos no deseados
        lineS = list(line.split(","))

    #se utliza el for para examinar los datos de uno por uno
        flag = 0  #se agrega un flag para saber si se agrega un elemento a la lista
        for i in range(len(lineS)):

            i = i + flag # se agrega flag a i por agregar un elemento a la lista
        
        # Se evalua si hay un tab y se elimina, se agrega el valomodificado
        # Se realiza lo smismo en todos los if, pero diferente elemento
            if "\t" in lineS[i]:
                new = lineS[i].replace("\t", "")
                lineS.pop(i)
                lineS.insert(i, new)
            if "\n" in lineS[i]:
                new2 = lineS[i].replace("\n", "")
                lineS.pop(i)
                lineS.insert(i, new2)
            if " " in lineS[i]:
                new1 = lineS[i].replace(" ", "")
                lineS.pop(i)
                lineS.insert(i, new1)
            if ":" in lineS[i]:
                rep = lineS[i]
            #lineS[i] = rep
            #rep = rep[0]
                susti = ""
                susti1 = ""
                stop = 1
                for e in range(len(rep)):
                    if rep[e] != ":" and stop == 1:
                        susti = susti + rep[e]
                    elif rep[e] != ":" and stop == 0:
                        susti1 = susti1 + rep[e]
                    else:
                        stop = 0
                lineS.pop(0)  
                lineS.insert(0, susti1)
                lineS.insert(0, susti)
                flag = 1
           
        findline.append(lineS[0])
    return findline


adres = separador(texto)

texto = open(inputt)
# se genera un bucle para revisar linea por linea el contenido del archivo
for line in texto:
    
    #print(findpos)
    #se separan el string de la linea para poder eliminar datos no deseados
    lineS = list(line.split(","))

    #se utliza el for para examinar los datos de uno por uno
    flag = 0  #se agrega un flag para saber si se agrega un elemento a la lista
    for i in range(len(lineS)):

        i = i + flag # se agrega flag a i por agregar un elemento a la lista
        
        # Se evalua si hay un tab y se elimina, se agrega el valomodificado
        # Se realiza lo smismo en todos los if, pero diferente elemento
        if "\t" in lineS[i]:
            new = lineS[i].replace("\t", "")
            lineS.pop(i)
            lineS.insert(i, new)
        if "\n" in lineS[i]:
            new2 = lineS[i].replace("\n", "")
            lineS.pop(i)
            lineS.insert(i, new2)
        if " " in lineS[i]:
            new1 = lineS[i].replace(" ", "")
            lineS.pop(i)
            lineS.insert(i, new1)
        if ":" in lineS[i]:
            rep = lineS[i]
            #lineS[i] = rep
            #rep = rep[0]
            susti = ""
            susti1 = ""
            stop = 1
            for e in range(len(rep)):
                if rep[e] != ":" and stop == 1:
                    susti = susti + rep[e]
                elif rep[e] != ":" and stop == 0:
                    susti1 = susti1 + rep[e]
                else:
                    stop = 0
            lineS.pop(0)  
            lineS.insert(0, susti1)
            lineS.insert(0, susti)
            flag = 1
        
    if len(lineS) >= 5:#se evalua que el valor de las lista no sea mayor a 4
     #   findpos.append(lineS[0])
        lineS.pop(0)#si es mayor se quita el primer objeto en la lista
        
    else:
      #  findpos.append("1")
        pass

    if "add" in lineS:
        
        CAT = "0000"
        s = 1
        z = 0
        while s < 4:
            bi = lineS[s]
            if len(bi) == 2 and "x" in bi:
                if z == 0:
                    db = decimal_a_binario(int(bi[1])) 
                    z = 1
                elif z == 1:
                    bb = decimal_a_binario(int(bi[1]))
                    z = 2
                elif z == 2: 
                    bc = decimal_a_binario(int(bi[1]))
                    CAT = CAT + agregar_ceros3b(bb) + agregar_ceros3b(bc) + agregar_ceros3b(db) + "00000"
            s += 1
        print("salida binaria = ",CAT)
        binaryList.append(CAT)
    elif "addi" in lineS:
        
        CAT = "0001"
        s = 1
        z = 0
        while s < 4:
            bi = lineS[s]
            if len(bi) == 2 and "x" in bi:
                if z == 0:
                    db = decimal_a_binario(int(bi[1])) 
                    z = 1
                elif z == 1:
                    bb = decimal_a_binario(int(bi[1]))
                    CAT = CAT + agregar_ceros3b(bb) + agregar_ceros3b(db)
            elif len(bi) == 4 and "x" in bi:
                dc = int(bi,16)
                cc = decimal_a_binario(dc)
                CAT = CAT + agregar_ceros8b(cc)
            elif "1" or "-1" in bi:
                
                if bi == "-1":
                    CAT = CAT + "11111111"
                else:
                    CAT = CAT + "00000001"
            s += 1
        
        print("salida binaria = ",CAT)
        binaryList.append(CAT)
    elif "and" in lineS:
        
        CAT = "0010"
        s = 1
        z = 0
        while s < 4:
            bi = lineS[s]
            if len(bi) == 2 and "x" in bi:
                if z == 0:
                    db = decimal_a_binario(int(bi[1])) 
                    z = 1
                elif z == 1:
                    bb = decimal_a_binario(int(bi[1]))
                    z = 2
                elif z == 2: 
                    bc = decimal_a_binario(int(bi[1]))
                    CAT = CAT + agregar_ceros3b(bb) + agregar_ceros3b(bc) + agregar_ceros3b(db) + "00000"
            s += 1
        print("salida binaria = ",CAT)
        binaryList.append(CAT)
    elif "andi" in lineS:
        
        CAT = "0011"
        s = 1
        z = 0
        while s < 4:
            bi = lineS[s]
            if len(bi) == 2 and "x" in bi:
                if z == 0:
                    db = decimal_a_binario(int(bi[1])) 
                    z = 1
                elif z == 1:
                    bb = decimal_a_binario(int(bi[1]))
                    CAT = CAT + agregar_ceros3b(bb) + agregar_ceros3b(db)
            elif len(bi) == 4 and "x" in bi:
                dc = int(bi,16)
                cc = decimal_a_binario(dc)
                CAT = CAT + agregar_ceros8b(cc)
            elif "1" or "-1" in bi:
                
                if bi == "-1":
                    CAT = CAT + "11111111"
                else:
                    CAT = CAT + "00000001"
            s += 1
        
        print("salida binaria = ",CAT)
        binaryList.append(CAT)
    elif "beq" in lineS:
        
        CAT = "0100"
        s = 1
        z = 0
        while s < 4:
            bi = lineS[s]
            if len(bi) == 2 and "x" in bi:
                if z == 0:
                    db = decimal_a_binario(int(bi[1])) 
                    z = 1
                elif z == 1:
                    bb = decimal_a_binario(int(bi[1]))
                 
            if bi in adres:
                ad = adres.index(bi)#representa la posicion que sera binario
                ad = ad + 1
                if ad < find:#find representa la posicion actual de la linea
                    #pasar ad a binario y complemento 2
                    comp = comp2(ad)
                    CAT = CAT + agregar_ceros3b(db)+ agregar_ceros3b(bb) + agregar_unos8b(comp)
                else:
                    num = decimal_a_binario(ad)
                    CAT = CAT + agregar_ceros3b(db)+ agregar_ceros3b(bb) + agregar_ceros8b(comp)
            else:
                pass
            s += 1
        
        print("salida binaria = ",CAT)
        binaryList.append(CAT)
    elif "bne" in lineS:
        
        CAT = "0101"
        s = 1
        z = 0
        while s < 4:
            bi = lineS[s]
            if len(bi) == 2 and "x" in bi:
                if z == 0:
                    db = decimal_a_binario(int(bi[1])) 
                    z = 1
                elif z == 1:
                    bb = decimal_a_binario(int(bi[1]))

            if bi in adres:
                ad = adres.index(bi)#representa la posicion que sera binario
                ad = ad + 1
                if ad < find:#find representa la posicion actual de la linea
                    #pasar ad a binario y complemento 2
                    comp = comp2(ad)
                    CAT = CAT + agregar_ceros3b(db)+ agregar_ceros3b(bb) + agregar_unos8b(comp)
                else:
                    num = decimal_a_binario(ad)
                    CAT = CAT + agregar_ceros3b(db)+ agregar_ceros3b(bb) + agregar_ceros8b(comp)
            else:
                pass
            s += 1
        
        print("salida binaria = ",CAT)
        binaryList.append(CAT)
    elif "j" in lineS:
        
        CAT = "0110"
        if len(lineS) == 3:
            s = 2
            s1 = 3
        else:
            s = 1
            s1 = 2
        z = 0
        while s < s1:
            bi = lineS[s]
            if bi in adres:
                ad = adres.index(bi)#representa la posicion que sera binario
                ad = ad + 1
                if ad < find:#find representa la posicion actual de la linea
                    #pasar ad a binario y complemento 2
                    comp = comp2(ad)
                    CAT = CAT + agregar_unos14b(comp)
                else:
                    num = decimal_a_binario(ad)
                    CAT = CAT + agregar_ceros14b(num)
            else:
                pass
                
            s += 1
        
        print("salida binaria = ",CAT)
        binaryList.append(CAT)
    elif "jal" in lineS:     
        CAT = "0111"
        if len(lineS) == 3:
            s = 2
            s1 = 3
        else:
            s = 1
            s1 = 2
        z = 0
        while s < s1:
            bi = lineS[s]
            if bi in adres:
                ad = adres.index(bi)#representa la posicion que sera binario
                ad = ad + 1
                if ad < find:#find representa la posicion actual de la linea
                    #pasar ad a binario y complemento 2
                    comp = comp2(ad)
                    CAT = CAT + agregar_unos14b(comp)
                else:
                    num = decimal_a_binario(ad)
                    num1 = decimal_a_binario(15)
                    CAT = CAT + agregar_ceros14b(num)
            else:
                pass
                
            s += 1
        
        print("salida binaria = ",CAT)
        binaryList.append(CAT)
    elif "jr" in lineS:
    
        CAT = "1010"
        if len(lineS) == 3:
            s = 2
            s1 = 3
        else:
            s = 1
            s1 = 2
        z = 0
        while s < s1:
            bi = lineS[s]
            if len(bi) == 2 and "x" in bi:
                if z == 0:
                    db = decimal_a_binario(int(bi[1])) 
                    CAT = CAT + agregar_ceros3b(db) + "00000000000"

            s += 1
        
        print("salida binaria = ",CAT)
        binaryList.append(CAT)
    elif "lb" in lineS:
        
        CAT = "1011"
        s = 1
        z = 0
        while s < 4:
            bi = lineS[s]
            if len(bi) == 2 and "x" in bi:
                if z == 0:
                    db = decimal_a_binario(int(bi[1])) 
                    z = 1
                elif z == 1:
                    bb = decimal_a_binario(int(bi[1]))
                    CAT = CAT + agregar_ceros3b(bb) + agregar_ceros3b(db) + agregar_ceros8b(decabin)
            elif len(bi) == 1:
                decabin = decimal_a_binario(int(bi))
            s += 1
        
        print("salida binaria = ",CAT)
        binaryList.append(CAT)
    elif "or" in lineS:
        
        CAT = "1100"
        s = 1
        z = 0
        while s < 4:
            bi = lineS[s]
            if len(bi) == 2 and "x" in bi:
                if z == 0:
                    db = decimal_a_binario(int(bi[1])) 
                    z = 1
                elif z == 1:
                    bb = decimal_a_binario(int(bi[1]))
                    z = 2
                elif z == 2: 
                    bc = decimal_a_binario(int(bi[1]))
                    CAT = CAT + agregar_ceros3b(bb) + agregar_ceros3b(bc) + agregar_ceros3b(db) + "00000"
            s += 1 
        
        print("salida binaria = ",CAT)
        binaryList.append(CAT)
    elif "sb" in lineS:
    
        CAT = "1101"
        s = 1
        z = 0
        while s < 4:
            bi = lineS[s]
            if len(bi) == 2 and "x" in bi:
                if z == 0:
                    db = decimal_a_binario(int(bi[1])) 
                    z = 1
                elif z == 1:
                    bb = decimal_a_binario(int(bi[1]))
                    CAT = CAT + agregar_ceros3b(bb) + agregar_ceros3b(db) + agregar_ceros8b(decabin)
            elif len(bi) == 1:
                decabin = decimal_a_binario(int(bi))
            s += 1
        
        print("salida binaria = ",CAT)
        binaryList.append(CAT)
    elif "sll" in lineS:
        
        CAT = "1110"
        s = 1
        z = 0
        while s < 4:
            bi = lineS[s]
            if len(bi) == 2 and "x" in bi:
                if z == 0:
                    db = decimal_a_binario(int(bi[1])) 
                    z = 1
                elif z == 1:
                    bb = decimal_a_binario(int(bi[1]))
                    z = 2
                elif z == 2: 
                    bc = decimal_a_binario(int(bi[1]))
                    CAT = CAT + agregar_ceros3b(bc) + agregar_ceros3b(bb) + agregar_ceros3b(db) + "00000"
            s += 1
            
        
        print("salida binaria = ",CAT)
        binaryList.append(CAT)
    elif "srl" in lineS:
        
        CAT = "1111"
        s = 1
        z = 0
        while s < 4:
            bi = lineS[s]
            if len(bi) == 2 and "x" in bi:
                if z == 0:
                    db = decimal_a_binario(int(bi[1])) 
                    z = 1
                elif z == 1:
                    bb = decimal_a_binario(int(bi[1]))
                    z = 2
                elif z == 2: 
                    bc = decimal_a_binario(int(bi[1]))
                    CAT = CAT + agregar_ceros3b(bc) + agregar_ceros3b(bb) + agregar_ceros3b(db) + "00000"
                s += 1
            
        
        print("salida binaria = ",CAT)
        binaryList.append(CAT)

    else:
        print("falla en la matrix")
    
    find += 1


create_output_file(binaryList)