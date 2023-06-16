import json

def write():
    with open('data\org.json', 'r') as f:
        ex5=json.load(f)
    for i in ex5:
        if i['id'] == '0003':
            x=i['batters']['batter']
            x.append({"id":"1003","type":"coffee"})
            print(x)
    with open("data\org_out.json",'w') as f:
        json.dump(ex5,f,indent=4)

def read():
    write()
    with open('data\org_out.json', 'r') as f:
        ex5=json.load(f)
    f.close()
    return ex5
       