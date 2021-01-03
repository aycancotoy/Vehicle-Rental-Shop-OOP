# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 19:22:13 2021

@author: Aycan ÇOTOY - Araç Kiralama Programı - TÜRKÇE

ARA YÜZ BÖLÜMÜ(Görünen Bölüm)
"""
from rent import CarRent, BikeRent, Customer

bike = BikeRent(100)
car = CarRent(10)
customer = Customer()

main_menu = True

while True:
    
    if main_menu:
        print("""
              ***** ARAÇ KİRALAMA MERKEZİ*****
              A. Bisiklet Menüsü
              B. Araba Menüsü 
              Q. Çıkış
              """)
        main_menu = False
        
        choice = input("Seçiminizi Girin: ")
        
    if choice == "A" or choice == "a":
        
        print("""
              ***** BİSİKLET MENÜSÜ *****
              1. Müsait Durumdaki Bisiklet Sayısı
              2. Bisikleti saatlik kiralama $5
              3. Bisikleti günlük kiralama  $84
              4. Bisikleti Teslim Et
              5. Ana Menüye Dön
              6. Programı Kapat.
              """)
        choice = input("Seçiminizi Girin:  ")
        
        try:
            choice = int(choice)
        except ValueError:
            print("Bu bir sayı değil")
            continue
        
        if choice == 1:
            bike.displayStock()
            choice = "A"
        elif choice == 2:
            customer.rentalTime_b = bike.rentHourly(customer.requestVehicle("bike"))
            customer.rentalBasis_b = 1
            main_menu = True
            print("---------------")
        elif choice == 3:
            customer.rentalTime_b = bike.rentDaily(customer.requestVehicle("bike"))
            customer.rentalBasis_b = 2
            main_menu = True
            print("---------------")
        elif choice == 4:
            customer.bill = bike.returnVehicle(customer.returnVehicle("bike"),"bike")
            customer.rentalBasis_b, customer.rentalTime_b, customer.bikes = 0,0,0
            main_menu = True
            print("---------------")
        elif choice == 5:
            main_menu = True
        elif choice == 6:
            break
        else:
            print("Yanlış giriş. Lütfen belirtilen [1-6] aralıktaki sayıyı girininiz.")
            main_menu = True
            
    elif choice == "B" or choice == "b":
        
        print("""
              ***** CAR MENU *****
              1. Müsait Durumdaki Araba Sayısı
              2. Arabayı saatlik kiralama $10
              3. Arabayı günlük kiralama  $192
              4. Bisikleti Teslim Et
              5. Ana Menüye Dön
              6. Programı Kapat.
              """)
        choice = input("Enter choice: ")
        
        try:
            choice = int(choice)
        except ValueError:
            print("It is not integer")
            continue
        
        if choice == 1:
            car.displayStock()
            choice = "B"
        elif choice == 2:
            customer.rentalTime_c = car.rentHourly(customer.requestVehicle("car"))
            customer.rentalBasis_c = 1
            main_menu = True
            print("---------------")
        elif choice == 3:
            customer.rentalTime_c = car.rentDaily(customer.requestVehicle("car"))
            customer.rentalBasis_c = 2
            main_menu = True
            print("---------------")
        elif choice == 4:
            customer.bill = car.returnVehicle(customer.returnVehicle("car"),"car")
            customer.rentalBasis_c, customer.rentalTime_c, customer.cars = 0,0,0
            main_menu = True
            print("---------------")
        elif choice == 5:
            main_menu = True
        elif choice == 6:
            break
        else:
            print("Yanlış giriş. Lütfen belirtilen [1-6] aralıktaki sayıyı girininiz.")
            main_menu = True
            
    elif choice == "Q" or choice == "q":
        break
    
    else:
        print("Hatalı giriş! Lütfen sadece (A-B-Q) karekterlerinden birini giriniz")
        main_menu = True
    print("Araç kiralama programını kullandığınız için teşekkür ederiz.")