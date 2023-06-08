import json 

#yazma
veriler = {}

veriler["kullanicilar"]=[]
veriler["kullanicilar"].append({"kadi":"Mckrakule42","sifre":"12346","mail":"mckarakule@hotmail.com"})
veriler["kullanicilar"].append({"kadi":"Mckrakule42","sifre":"12346mm","mail":"karabela4@hotmail.com"})

with open("veriler.json","w",encoding="utf-8") as file :
    json.dump(veriler,file)

#okuma


with open("veriler.json","r") as file :
    veriler =json.load(file)
    # print(veriler["kullanicilar"][0]["sifre"])

    for kullanici in veriler["kullanicilar"]:
        if kullanici["kadi"]=="Mckrakule42":
            print(kullanici["sifre"])

