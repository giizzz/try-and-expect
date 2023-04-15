try:
    dosya = open("yazilimbilimi.txt","r")
except IOError:
    print("Dosya bulunamadı")
finally:
    dosya.close()
