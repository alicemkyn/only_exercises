# while True:
#     a = int(input("sayi girin:"))
#     i = 1
#     top = 0
#     while i < a:
#         if a % i == 0:
#             top += i
#         i += 1
#     if top == a :
#         print ("Perfect")
#     else:
#         print("Not Perfect")
    
# while True:
#     a = int(input("sayi"))
#     top = 0
#     for i in range(1,a):
#         if a % i == 0:
#             top += i
#     if top == a:
#         print("Perfecto !!")
#     else:
#         print("Neehhh")
    
# while True:
#     a_str = input(" sayi ")
#     len_a = len(a_str)
#     a_int = int(a_str)
#     kalan = 0
#     toplam = 0
#     real_a = a_int
#     while a_int > 0:
#         kalan = a_int % 10
#         toplam += kalan ** len_a
#         a_int //= 10
#     if toplam == real_a:
#         print("armstrong number")
#     else:
#         print("NOT ARMSTRONG")


# while True:
#     a = int(input("enter the range u wanna check"))      
#     for i in range(1,a):
#         top = 0
#         for j in range(1,i):
#             if i % j == 0:
#                 top += j
#         if top == i:
#             print(i)
#     if top != i:
#         print ("no powers inside the range")



# a = int(input("Range gir Armstrong icin:"))
# print(a,"a kadar bakilacak....")
# for i in range(1,a):
#     b = str(i)
#     len_b = len(b)
#     i_intreal = int(b)
#     total = 0
#     remain = 0
#     while i > 0:
#         remain = i % 10
#         total += remain ** len_b
#         i //= 10
#     if total == i_intreal:
#         print(i_intreal)
# if total != i_intreal:
#     print("There is no any Armstrong Number in given range")


# for i in range(11):
#     print("{}".format(i) * i)


# a = 0
# for i in range(101):
#     a += i 
# print(a)
            
            
# for i in range(1,11):
#     for j in range(1,11):
#         print(f"{i}x{j}={i*j}")



# s = "A man , a plan , a canal: Panama"
# s_low = s.lower() 
# s_low = "".join(i for i in s_low if i.isalnum())
# print(s_low)
# if s_low == s_low[::-1]:
#     print("is palindrome")
# else:
#     print("Not palindrome")


# while True:

#     input("Faktoriyel hesaplamasi icin aralik deger istenecektir lutfen ayri ayri gireceksiniz devam icin bir tusa basin")
#     a = int(input("range in ilk aralik degerini giriniz"))
#     b = int(input("range in ikinci araligini giriniz"))
#     ttl = 1
#     for i in range(a,b+1):
#         ttl *= i
#     print(ttl,"Faktoriyel toplam")


#Fibonacci Numbers
# a = 1
# b = 1
# liste = []
# rng_int = int(input("sonlanmasini istediginiz degeri giriniz"))
# for i in range(1,rng_int):
#     a,b = b,a+b
#     liste.append(b)
# print(liste)



#Prime Numbers

# for i in range(1,100):
#     for j in range(2,i+1):
#         if i % j == 0:
#             if i == j:
#                 print(i)
#             break



# while True:
#     ttl = 0
#     a = int(input("enter a number to see if it is a perfect one !"))
#     for i in range(1,a):
#         if a % i == 0:
#             ttl += i
#     if ttl == a :
#         print("Perfecto")
#     else:
#         print("not perfect"
# 
# while True:
#     a = int(input("enter the range first value to check all power numbers "))
#     b = int(input("enter the last value of range"))
    
#     liste = []
#     for i in range(a,b):
#         ttl = 0
#         for j in range(1,i):
#             if i % j == 0:
#                 ttl += j
#         if ttl == i:
#             liste.append(i)
#     print(liste)
    

# # belirli bir aralikta armstrong sayilarini bulma
# while True:
#     rn1 = int(input("Enter first value of range"))
#     rn2 = int(input("Enter the last value of range"))
#     for i in range(rn1,rn2):
#         a = str(i)
#         a_len = len(a)
#         b = int(a)
#         b2 = b
#         kalan = 0
#         us = 0
#         while b > 0:
#             kalan = b % 10
#             us += kalan ** a_len
#             b //= 10
#         if us == b2 :
#             print (b2)


# while True:
#     a = int(input("To check the number if it is a prime one enter one"))
#     if a == 1 or a == 0:
#             print(f"{a} asal sayi olamaz")
    
#     for i in range(2,(a+1)):
#         if a % i == 0:
#             if a == i:
#                 print(a,"Asal bir sayidir")
#             else:
#                 print(a,"Asal bir sayi degildir")
#             break




# a = (123123,2312312,3412421,444123)
# newlist = []
# liste = [str(x) for x in a]

# for i in liste:
#     for j in str(i)[::2]:
#         newlist.append(j*2)
# print(newlist)


#TC NO
# l = 20
# digit = 333852669
# while l > 1:
#     digit += 29999
#     total= 0
#     total1 = 0
#     tenth = int()
#     eleventh = int()
#     a = str(digit)
#     liste = [digit]
#     for i in a[::2]:
#         total += int(i)
#     total *= 7
#     for j in a[1::2]:
#         total1 += int(j)
#     tenth = (total - total1) % 10
#     liste.append(tenth)
#     total = 0
#     for i in liste:
#         for j in str(i):
#             total += int(j)
#     eleventh = total % 10
#     liste.append(eleventh)
#     a = "".join(str(x) for x in liste )
#     print(a)
#     l -=  1