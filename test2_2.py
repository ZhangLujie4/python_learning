import os
os.getcwd()
os.chdir('F:\chapter3')
os.getcwd()
try:
    p=open('sketch.txt')

    for each_line in p:
        try:
            (role,line_spoken)=each_line.split(':',1)
            print(role,end='')
            print(' said: ',end='')
            print(line_spoken,end='')
        except ValueError:
            pass
    p.close()
except IOError:
    print('the file is missing!')

try:
    p=open('chapter3.txt')
    for each_line in p:
       try:
           (role,line_spoken)=each_line.split(':',1)
           print(role,end='')
           print(' said: ',end='')
           print(line_spoken,end='')
       except ValueError:
           pass
    p.close()
except IOError:
    print('the file is missing!')
try:
    data=open('missing.txt')
    print(data.readline(),end='')
except IOError as err:
    print('File error:'+str(err))
finally:
    if 'data'in locals():
        data.close()
try:
    with open('its.txt','w') as data:
        print("It's...",file=data)
except IOError as err:
    print('File error:'+str(err))

    



