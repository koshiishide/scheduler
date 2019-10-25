def d2b(dec):
	return format(dec, "b").zfill(42)

def makedata():
	b=""
	for i in range(0,42):
    	b=b+"0"
    	if i !=41:
        	b=b+","
	return b

def make_countlist(a):
    list=[]
    char=""
    for i in a:
        if i !=",":
            char = char+str(i)
        else:
            list.append(int(char))
            char=""
    return list            

def makeOrg(list_data,userdata):
    c=""
    count=0
    for i in list_data:
        if userdata[count] == "1":
            c=c+str(i+1)
            c=c+","
        else:
            c=c+str(i)
            c=c+","
        count=count+1
    return c
