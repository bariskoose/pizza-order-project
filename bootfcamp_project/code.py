import pandas as pd

class sepet:
    def __init__(self, toplamTutar, pizza, extra):
        self.toplamTutar = toplamTutar
        self.pizza = pizza
        self.extra = extra
    pass

class pizza:
    pass
    def __init__(self, ingredients, cost, size, tur):
        self.ingredients = ingredients
        self.cost = cost
        self.size = size
        self.tur = tur
    

class karisikPizza(pizza):
    
    def __init__(self, cost, size):
        super().__init__("sucuk,salam,zeytin,mısır", cost, size, "Karisik Pizza")
    pass

class margaritaPizza(pizza):
    
    def __init__(self, cost, size):
        super().__init__("peynir,domates sosu", cost, size, "Margarita Pizza")
    pass

class tonbalıklıPizza(pizza):
    
    def __init__(self, cost, size):
        super().__init__("tonbalık,pizzasosu", cost, size, "Tonbalıklı Pizza")
    pass

class dortpeynirliPizza(pizza):
    
    def __init__(self, cost, size):
        super().__init__("4 cesit peynir, pizza sosu", cost, size, "4 Peynirli Pizza")
    pass


class extra():
    def __init__(self, cost, name):
        self.cost = cost
        self.name = name
    pass



#S kucuk- M orta - L buyuk                           


def main():

    pizzatxt = open("pizza.txt", "r")
    print(pizzatxt.read())
    
    cost = 0
    size = ""
    
    print("Boy sec")
    pizzatxt1 = open("pizza.txt")
    
   
    boyutInput = input()
    if(boyutInput=="S"):
        cost = cost + 40
        size = "Kucuk Boy"
    elif(boyutInput == "M"):
        cost = cost + 50
        size = "Orta Boy"
    elif(boyutInput == "L"):
        cost = cost + 60
        size = "Buyuk Boy"
        
    
    print("Pizza turu secin:")
    turSecim = input()
    if(turSecim == "1"):
        pizzaSiparis = karisikPizza(cost, size)
    elif(turSecim == "2"):
        pizzaSiparis = margaritaPizza(cost, size)
    elif(turSecim =="3"):
        pizzaSiparis = tonbalıklıPizza(cost,size)
    elif(turSecim == "4"):
        pizzaSiparis = dortpeynirliPizza(cost,size)
        
    class kecipeyniri(extra):
         def __init__(self, cost, name):
             super().__init__(5,"keci peyniri")
    class misir(extra):
         def __init__(self, cost, name):
             super().__init__(5,"misir" )
    class zeytin(extra):
         def __init__(self, cost, name):
             super().__init__(5,"siyahzeytin")
    class mantarlar(extra):
         def __init__(self, cost, name):
             super().__init__(5,"mantarlar")
    class et(extra):
         def __init__(self, cost, name):
             super().__init__(5,"danaeti")
    class sogan(extra):
         def __init__(self, cost, name):
             super().__init__(5,"soganlar")
         
    
    
    print("Siparisiniz",pizzaSiparis.tur,"icerigi ", pizzaSiparis.ingredients, " " , pizzaSiparis.size, " ", pizzaSiparis.cost,"Tutar")
    
    print("Ekstra malzeme ister misiniz? (0=hayır, 1=evet)")
    
    extram = ""
    secim = input("")
    if(secim == "1"):
        print("Istediğim ekstra no ")
        ekstrasecim = input()
        if (ekstrasecim == "1"):
            extram = kecipeyniri(cost, name)
            extraToplam = 5
        elif (ekstrasecim == "2"):
            extram = misir(cost,name)
            extraToplam = 5
        elif (ekstrasecim == "3"):
            extraToplam = 5
            extram = zeytin(cost,name)
        elif (ekstrasecim == "4"):
            extram = sogan(cost,name)
            extraToplam = 5
        elif (ekstrasecim == "5"):
            extram = mantarlar(cost,name)
            extraToplam = 5
        elif (ekstrasecim == "6"):
            extram = et(cost,name)
            extraToplam = 5            
        elif(secim == "0"):
            extraToplam = 0 
    
    toplam = pizzaSiparis.cost + extraToplam
    musteriSepet = sepet(toplam, pizzaSiparis, extram)
    
    print("Pizza tutar: ", pizzaSiparis.cost)
    print("Siparisiniz",pizzaSiparis.tur,"içeriği ", pizzaSiparis.ingredients, " " , pizzaSiparis.size, " ", pizzaSiparis.cost,"tutar",extraToplam,"ekstralar")
    print("Toplam Tutar:",musteriSepet.toplamTutar)
    
    #sistembilgi = sepet(toplamTutar, pizza, extra)    
#if  __name__ =='__main__':main()

print("Lutfen adinizi giriniz")
name = input("")
print("Tc kimlik numaranızı giriniz")
kimlikno = input("")

print("lUtfen kart numarasını giriniz")
kartno = input("")

print("lütfen kart sifresini giriniz")
kartsifre = input("")


musteribilg = [name,kimlikno,kartno,kartsifre]


df_marks = pd.DataFrame({'Ad': [name],
     'Kimlik numarası': [kimlikno],
     'Banka kart numarası': [kartno],
     'Kart sifresi': [kartsifre],
     'Müsteri siparisi':[sepet]})

writer = pd.ExcelWriter('Order_Database.xlsx')

df_marks.to_excel(writer, 'marks')

writer.save()


if  __name__ =='__main__':main()

# Coded by Baris Kose (github = @bariskoose), Metin Vatansever (github = @metinvs), Omer Turk and Mehmet Demirbilek
