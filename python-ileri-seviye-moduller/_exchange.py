import requests
import json

api_url = 'https://api.exchangerate.host/latest?base='

bozulan_doviz=input("Bozulan döviz türü : ")
alınan_doviz=input("alınan döviz türü : ")


miktar=int(input(f"Ne kadar {bozulan_doviz} bozdurmak istiyorsun : "))
result=requests.get(api_url+bozulan_doviz)
result=json.loads(result.text)
print(result)

print("1 {0} ={1} {2}".format(bozulan_doviz,result["rates"][alınan_doviz],alınan_doviz))
print("1 {0} {1} ={2} {3}".format(miktar,bozulan_doviz,int(miktar)*result["rates"][alınan_doviz],alinan_doviz))