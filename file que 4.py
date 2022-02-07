state_data=open("question4.txt","r")
for i in range (30):
    c=state_data.readline()
    print(c)
    if "delhi" in c:
        delhi=open("delhi.txt","a")
        delhi.write(c)
    elif "shimla" in c:
        d=open("shimla.txt","a")
        d.write(c)
    else:
        o=open("other.txt","a")
        o.write(c)