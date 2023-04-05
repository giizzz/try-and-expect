sayi1 = input("Sayi1:")
sayi2 = input("Sayi2:")
try:
    sayi1 = int(sayi1)
    sayi2 = int(sayi2)
    print(sayi1/sayi2)

except  ValueError:
    print("Lutfen 10 luk tabanda bir sayi giriniz. ")
except ZeroDivisionError:
    print("Bir sayi 0 a bolunmez.")

# ikisi aynı yerde yazılırsa
except(ValueError,ZeroDivisionError):
    print("Bir hata olustu")