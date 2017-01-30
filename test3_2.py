import os
os.chdir('F:\chapter3')
with open('james.txt') as jaf:
    data=jaf.readline()
    james=data.strip().split(',')
with open('julie.txt') as juf:
    data=juf.readline()
    julie=data.strip().split(',')
with open('mikey.txt') as mif:
    data=mif.readline()
    mikey=data.strip().split(',')
with open('sarah.txt') as saf:
    data=saf.readline()
    sarah=data.strip().split(',')
print(sorted(james))
print(sorted(julie))
print(sorted(mikey))
print(sorted(sarah))
def sanitize(time_string):
    if '-' in time_string:
        splitter='-'
    elif ':' in time_string:
        splitter=':'
    else:
        return(time_string)
    (mins,secs)=time_string.split(splitter)
    return(mins+'.'+secs)
clean_james=[]
clean_julie=[]
clean_mikey=[]
clean_sarah=[]
for each_item in james:
    clean_james.append(sanitize(each_item))
for each_item in julie:
    clean_julie.append(sanitize(each_item))
for each_item in mikey:
    clean_mikey.append(sanitize(each_item))
for each_item in sarah:
    clean_sarah.append(sanitize(each_item))
print(sorted(clean_james))
print(sorted(clean_julie))
print(sorted(clean_mikey))
print(sorted(clean_sarah))
clean_james=[sanitize(each_t) for each_t in james]
clean_julie=[sanitize(each_t) for each_t in julie]
#clean_mikey=[sanitize(each_t) for each_t in mikey]
clean_sarah=[float(sanitize(each_t)) for each_t in sarah]
print(sorted(clean_james))
print(sorted(clean_julie))
#print(sorted(clean_mikey))
print(sorted([sanitize(t) for t in mikey]))
print(sorted(clean_sarah))

clean=[float(s) for s in clean_james]
print(clean)

mins=[1,2,3]
secs=[m*60 for m in mins]
print(secs)

lower=['I',"dont't",'like','you']
upper=[s.upper() for s in lower]
print(upper)
#用迭代把重复项给删除
julie=sorted([sanitize(t) for t in julie])
unique_julie=[]
for each_t in julie:
    if each_t not in unique_julie:
        unique_julie.append(each_t)
print(unique_julie[0:3])

print(sorted(set([sanitize(t) for t in sarah]))[0:3])#简直画风清奇hhh


#————————————————————————————
def get_coach_data(filename):
    try:
        with open(filename) as f:
            data=f.readline()
        return(data.strip().split(','))
    except IOError as ioerr:
        print('File error:'+str(ioerr))
        return(None)

sarah=get_coach_data('sarah.txt')
print(sarah)

#最终的效果呈现！！！！！！！！！！！！！！！
mikey=get_coach_data('mikey.txt')
print(sorted(set([sanitize(t) for t in mikey]))[0:3])
#倒序排很重要哦！！！！！！
print(sorted(set([sanitize(t) for t in mikey]),reverse=True)[0:3])
#my_list[3:6]指从my_list【3】~my_list【5】




sarah=get_coach_data('sarah2.txt')
(sarah_name,sarah_dob)=sarah.pop(0),sarah.pop(0)
print(sarah_name+"'s fastest times are:"
      +str(sorted(set([sanitize(t) for t in sarah]))[0:3]))
#这里要用str（）不然会报错

sarah=get_coach_data('sarah2.txt')#这局一定要重新写过
sarah_data={}
sarah_data['Name']=sarah.pop(0)
sarah_data['DOB']=sarah.pop(0)
sarah_data['Times']=sarah
print(sarah_data['Name']+"'s fastest times are:"+str(sorted(set([sanitize(t) for t in sarah_data['Times']]))[0:3]))


