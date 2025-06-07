def somar( vl_1, vl_2):
    p1 = int(vl_1)
    p2 = int(vl_2)
    resul = p1 + p2
    return resul

def subtrai( vl_1, vl_2):
    p1 = int(vl_1)
    p2 = int(vl_2)
    resul = p1 - p2
    return resul



vl1 = input("digite valor 1 ")

vl2 = input("digite valor 2 ")

contat ={"vl_1":somar(vl1,vl2), 
         "vl_2":subtrai(vl1,vl2)}


print(contat.values())