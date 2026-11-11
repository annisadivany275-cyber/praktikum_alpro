nama = input("Masukkan nama anda: ")
input_nilai = int(input("Masukkan nilai nada: "))

if input_nilai >= 60: 
    print(nama, "anda dinyatakan lulus")
    status = "Lulus"
else : 
    print(nama, "anda dinyatakan tidak lulus")
    status = "Tidak lulus"

if input_nilai >= 90:
   grade = "A"

elif input_nilai >= 80:
   grade = "B"

elif input_nilai >= 70:
   grade = "C"

elif input_nilai >= 60:
   grade = "D"

elif input_nilai >= 50:
   grade = "E"

print (nama, "mendapat predikat", grade)