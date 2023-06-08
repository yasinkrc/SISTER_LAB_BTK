""" 
Basit Seviye:
Bir metin içindeki e-posta adreslerini bulan bir program yazmanız gerekmektedir. 
Kullanıcıdan bir metin girişi alacak ve program, metindeki e-posta adreslerini tespit 
edip ekrana yazdıracaktır. 
Örneğin, kullanıcı "Merhaba, benim e-posta adresim example@example.com" gibi bir metin 
girerse, program bu e-posta adresini bulup ekrana yazdıracaktır.
"""
# import re

# def find_emails(text):
#     pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
#     # Yukarıdaki desen, e-posta adreslerini tespit etmek için kullanılır

#     emails = re.findall(pattern, text)
#     # re.findall işlevi, metindeki tüm e-posta adreslerini bir liste olarak döndürür

#     return emails

# # Kullanıcıdan metin girişi alalım
# text = input("Metin girin: ")

# # Metindeki e-posta adreslerini bulalım
# found_emails = find_emails(text)

# # Bulunan e-posta adreslerini ekrana yazdıralım
# if found_emails:
#     print("Bulunan e-posta adresleri:")
#     for email in found_emails:
#         print(email)
# else:
#     print("Metinde e-posta adresi bulunamadı.")

"""
Orta Seviye:
Bir URL doğrulama programı yazmanız gerekmektedir. 
Kullanıcıdan bir URL alacak ve program, bu URL'nin geçerli bir web 
adresi olup olmadığını kontrol edecektir. re modülünü kullanarak, doğru URL formatını ve 
uygun şablonları kontrol edebilirsiniz. Örneğin, kullanıcı "https://www.example.com" gibi 
bir URL girdiğinde program, bu URL'nin geçerli olduğunu doğrulayacaktır.
"""
# import re

# def validate_url(url):
#     pattern = r'^(https?://)?(www\.)?([A-Za-z0-9-]+\.){1,}[A-Za-z]{2,}(/.*)?$'
#     # Yukarıdaki desen, URL'nin doğru formatını kontrol etmek için kullanılır

#     if re.match(pattern, url):
#         return True
#     else:
#         return False

# # Kullanıcıdan URL girişi alalım
# url = input("URL girin: ")

# # URL doğruluğunu kontrol edelim
# if validate_url(url):
#     print("Geçerli bir URL.")
# else:
#     print("Geçersiz URL.")


"""
Zor Seviye:
Bir hesap parolası doğrulama programı yazmanız gerekmektedir. 
Kullanıcıdan bir parola girişi alacak ve program, parolanın belirli şartları karşılayıp 
karşılamadığını kontrol edecektir. re modülünü kullanarak, parolanın belirli bir 
uzunlukta olması, büyük harfler, küçük harfler, rakamlar ve özel karakterler içermesi 
gibi kriterleri kontrol edebilirsiniz. Program, kullanıcıya parolanın güvenli olup 
olmadığına dair bir geri bildirim verecektir.

"""

# import re

# def validate_password(password):
#     if len(password) < 5:
#         return "Parola 5 karakterden uzun olmalıdır."
    
#     if not re.search(r"[a-z]", password):
#         return "Parola en az bir küçük harf içermelidir."
    
#     if not re.search(r"[A-Z]", password):
#         return "Parola en az bir büyük harf içermelidir."
    
#     if not re.search(r"\d", password):
#         return "Parola en az bir rakam içermelidir."
    
#     if not re.search(r"[!@#$%^&*()\-_=+{};:,<.>]", password):
#         return "Parola en az bir özel karakter içermelidir."
    
#     return "Parola güvenli."

# # Kullanıcıdan parola girişini alalım
# password = input("Parola girin: ")

# # Parolanın doğruluğunu kontrol edelim
# result = validate_password(password)

# # Sonucu ekrana yazdıralım
# print(result)

"""  
Problem:
Verilen bir metindeki tüm URL'leri bulmak için re modülünü kullanarak bir program yazmanız 
gerekmektedir. 
Program, kullanıcıdan bir metin girişi alacak ve metindeki tüm URL'leri bulup ekrana 
yazdıracaktır.

Bu problemde size, re modülünü kullanarak bir metindeki URL'leri bulmanızı ve 
çıktıya yazdırmanızı istiyorum. Başarılı bir şekilde tamamladıktan sonra çözümünüzü 
paylaşabilirsiniz
"""
import re

def find_urls_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()

            pattern = r'\b(?:https?://|www\.)\S+\b'
            # Yukarıdaki desen, metindeki URL'leri bulmak için kullanılır

            urls = re.findall(pattern, text)
            return urls
    except FileNotFoundError:
        print("Dosya bulunamadı.")
        return []
    except:
        print("Bir hata oluştu.")
        return []

# Kullanıcıdan dosya yolunu alalım
file_path = input("dosya ismi : ")

# Dosyadaki URL'leri bulalım
result = find_urls_in_file(file_path)

# Bulunan URL'leri ekrana yazdıralım
print("Bulunan URL'ler:")
for url in result:
    print(url)

