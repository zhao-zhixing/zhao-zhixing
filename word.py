import jieba
import json
content=open('content.txt','r',encoding='utf-8').read()
all_world=jieba.lcut(content)
count={}
for i in all_world:
    if len(i)==1:
        continue
    else:
        count[i]=count.get(i,0)+1
items = list(count.items())
items.sort(key=lambda d:d[1],reverse=True)
results=[]
for i in range(100):
    result={}
    word,count=items[i]
    result["name"]=word
    result["value"]=count
    results.append(result)



with open("comments.json","w") as f:
    com__json=json.dumps(results,ensure_ascii=False)
    f.write(com__json)