import random 

# result = dir(random)

# result=help(random)

result =random.random()

result =int(random.random()*100)
result=random.uniform(10,100)
result=int(random.uniform(10,100))

result=random.randint(10,454)

names =["yasin","yazgülü","karaca","beşaltı"]
result=names[random.randint(0,len(names))]
result=random.choice(names)
result=list(range(10))
random.shuffle(result)

liste =list(range(100))
result=random.sample(liste,3)

print(result)