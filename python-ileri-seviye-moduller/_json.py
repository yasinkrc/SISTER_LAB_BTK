import json

#Dict

# person={"name":"Ali","languages":["Python","C#"]}
# result=person["name"]
# result=person["languages"][1]
# print(result)


""" JSON string to Dictionary """
person_string='{"name":"Ali","languages":["Python","C#"]}'
person_dict ={"name":"ali","languages":["python","C#" ,"C++","java","javascript"]}


person_dict=json.loads(person_string)

result=json.dumps(person_dict,indent=4,sort_keys=True)
print(result)
# result=json.loads(person_string)
# result=result["name"]
# result=result["languages"]
# print(type(result))
# print(result)

# with open("person.json","r") as f :
#     data=json.load(f)
#     print(data["name"])
#     print(data["languages"])

"""   Dictionary  to JSON string """

# person_dict ={
#       "name":"ali",
#       "languages":["python","C#" ,"C++","java","javascript"]

# }

# result=json.dumps(person_dict)
# print(type(result))
# print(result)

# with open("person.json","w") as f :
#     json.dump(person_dict,f)



