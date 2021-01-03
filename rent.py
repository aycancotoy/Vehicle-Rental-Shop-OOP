# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 17:00:51 2021

@author: Aycan ÇOTOY

ANA BÖLÜM(Kiralama Bölümü)
"""

import datetime

# parent class
class VehicleRent:
    
    def __init__(self,stock):
        self.stock = stock
        self.now = 0
    
    def displayStock(self): # stokta kaç var?
        """
            Toplam araç sayısı
        """
        #kiralamak için uygun araç sayısı
        print("{} araç kiralamaya uygun".format(self.stock))
        return self.stock
    
    def rentHourly(self, n): # saatlik kiralama
        """
            Saatlik Kiralama
        """
        if n <= 0:
            print("0'dan büyük rakam girmelisiniz")
            return None
        elif n > self.stock:
            print("Üzgünüz {} araç kiralamaya uygun".format(self.stock))
            return None
        else:
            self.now = datetime.datetime.now()
            print("Toplam {} araç  {} saatliğine kiralandı".format(n,self.now.hour))
            
            self.stock -= n  
            
            return self.now
            
    
    def rentDaily(self, n):
        """
            Günlük Kiralama
        """
        if n <= 0:
            print("0'dan büyük rakam girmelisiniz")
            return None
        elif n > self.stock:
            print("Üzgünüz {} araç kiralamaya uygun".format(self.stock))
            return None
        else:
            self.now = datetime.datetime.now()
            print("Toplam {} araç {} günlüğüne kiralandı".format(n,self.now.hour))
            
            self.stock -= n 
            
            return self.now
        
    def returnVehicle(self, request, brand): #kiraladığı aracı geri getirdi. Şimdi fatura kesilcek.
        """
            Fatura Kes
        """
        car_h_price = 10
        car_d_price = car_h_price*8/10*24
        bike_h_price = 5
        bike_d_price = bike_h_price*7/10*24
        
        rentalTime, rentalBasis, numOfVehicle = request
        bill = 0

        if brand == "car":
            if rentalTime and rentalBasis and numOfVehicle:
                self.stock += numOfVehicle  #stock'a araç geri ekleniyor.
                now = datetime.datetime.now()
                rentalPeriod = now - rentalTime
                
                if rentalBasis == 1: #hourly
                    bill = rentalPeriod/3600*car_h_price*numOfVehicle
                elif rentalBasis == 2: #daily
                    bill = rentalPeriod/(3600*24)*car_d_price*numOfVehicle
                
                if (2 <= numOfVehicle): # discount için
                    print("Ekstra olarak 20% indirim kazandınız")
                    bill = bill*0.8
                    
                print("Arabayı geri getirdiğiniz için teşekkürler")
                print("Ücret: $ {}".format(bill))
                return bill
            
        elif brand == "bike":
            if rentalTime and rentalBasis and numOfVehicle:
                self.stock += numOfVehicle  #stock'a araç geri ekleniyor.
                now = datetime.datetime.now()
                rentalPeriod = now - rentalTime
                
                if rentalBasis == 1: #hourly
                    bill = rentalPeriod/3600*bike_h_price*numOfVehicle
                elif rentalBasis == 2: #daily
                    bill = rentalPeriod/(3600*24)*bike_d_price*numOfVehicle
                
                if (4 <= numOfVehicle): # discount için
                    print("Ekstra olarak 20% indirim kazandınız")
                    bill = bill*0.8
                    
                print("Bisikleti geri getirdiğiniz için teşekkürler")
                print("Ücret: $ {}".format(bill))
                return bill  
        
        else:
            print("Araç Kiralamadınız")
            return None
                
        
    
#child class 1
class CarRent(VehicleRent):
    
    global discount_rate
    discount_rate = 15
    
    def __init__(self, stock):
        super().__init__(stock)
    
    def discount(self, b):
        """
            Ücret 
        """
        bill = b - (b*discount_rate)/100
        return bill
    
#child class 2
class BikeRent(VehicleRent):
            
    def __init__(self, stock):
        super().__init__(stock)
    
# parent class customer
class Customer:
    
    def __init__(self):
        self.bikes = 0
        self.rentalBasis_b = 0
        self.rentalTime_b = 0
        
        self.cars = 0
        self.rentalBasis_c = 0
        self.rentalTime_c = 0
    
    def requestVehicle(self, brand):
        """
            Müşteri araba ya da bisiklet talep etsin.
        """
        if brand == "bike":
            bikes = input("Kaç adet bisiklet kiralamak istersiniz?")
            
            try:
                bikes = int(bikes)
            except ValueError:
                print("Sadece rakam giriniz")
                return -1
            
            if bikes < 1:
                print("0'dan büyük rakam giriniz.")
                return -1
            else:
                self.bikes = bikes
            return self.bikes         
            
        elif brand == "car":
            cars = input("Kaç adet bisiklet kiralamak istersiniz?")
           
            try:
                cars = int(cars)
            except ValueError:
                print("Sadece rakam giriniz")
                return -1
            
            if cars < 1:
                print("0'dan büyük rakam giriniz.")
                return -1
            else:
                self.cars = cars
            return self.cars  
            
        else:
            print("Araç talep hatası")
        
    
    def returnVehicle(self, brand):
        """
            Bisikleti veya arabayı iade et.
        """
        if brand == "bike":
            if self.rentalTime_b and self.rentalBasis_b and self.bikes:
                return self.rentalTime_b, self.rentalBasis_b, self.bikes
            else:
                return 0,0,0
            
        elif brand == "car":
            if self.rentalTime_c and self.rentalBasis_c and self.cars:
                return self.rentalTime_c, self.rentalBasis_c, self.cars
            else:
                return 0,0,0
        
        else:
            print("Return vehicle Error")
    

       