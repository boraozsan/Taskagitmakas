import random
tas='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
kagit = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

makas = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Taş Kağıt Makas Oyununa Hoşgeldiniz!")

kullanici_secim=int(input("Taş yapmak için 0, Kağıt yapmak için 1, Makas yapmak için 2 yazın.\n"))

bilgisayar_secim=random.randint(0,2)

if kullanici_secim==0:
    print(f"Taş Yaptınız!\n{tas}")
elif kullanici_secim==1:
    print(f"Kağıt Yaptınız!\n{kagit}")
elif kullanici_secim==2:
    print(f"Makas Yaptınız!\n{makas}")

if bilgisayar_secim==0:
    print(f"Bilgisayar Taş Yaptı!\n{tas}")
elif bilgisayar_secim==1:
    print(f"Bilgisayar Kağıt Yaptı!\n{kagit}")
elif bilgisayar_secim==2:
    print(f"Bilgisayar Makas Yaptı!\n{makas}")

if (bilgisayar_secim ==0 and kullanici_secim==1)or (bilgisayar_secim==1 and kullanici_secim==2)or(bilgisayar_secim==2 and kullanici_secim==0):
    print("Kazandın!")
if (bilgisayar_secim ==0 and kullanici_secim==0)or (bilgisayar_secim==1 and kullanici_secim==1)or(bilgisayar_secim==2 and kullanici_secim==2):
    print("Berabere!")
if (bilgisayar_secim ==0 and kullanici_secim==2)or (bilgisayar_secim==1 and kullanici_secim==0)or(bilgisayar_secim==2 and kullanici_secim==1):
    print("Kaybettin!")