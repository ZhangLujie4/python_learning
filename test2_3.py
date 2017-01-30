"""try:
    with open('missing.txt',"w")as data:
        print("It's...",file=data)
except IOError as err:
    print('File error:'+str(err))"""

"""try:
    data=open('its.txt',"w")
    print("It's...",file=data)
except IOError as err:
    print('File error:'+str(err))
finally:
    if 'data' in locals():
        data.close()"""
import os
os.getcwd()
os.chdir("F:\chapter3")
#with open('sketch.txt') as mdf:
#   print(mdf.readline())
import nester
man=['hyftftf','hugytftyftrdftr','hgfrd','lkjhyutfreseaqwasdc',"gfdsdsdsa",'kjhgffdgfd']
#man_file=open('man_data.txt','w')
try:
    with open('man_data.txt','w') as man_file:
        nester.print_lol(man,fh=man_file)
except IOError as err:
    print('File error:'+str(err))
#千万要记住文件的关闭，不然会出现无法预期的错误
#有多个参数时的赋值！！！！！！
import pickle
try:
    with open('man_data.txt',"wb")as man_file:
        pickle.dump(man,man_file)
except IOError as err:
    print('File error:'+str(err))
except pickle.PickleError as perr:
    print('Pickling error:'+str(perr))
new_man=[]
try:
    with open('man_data.txt','rb')as man_file:
        new_man=pickle.load(man_file)
except IOError as err:
    print('File error:'+str(err))
except pickle.PickleError as perr:
    print('Pickling error:'+str(perr))
nester.print_lol(new_man)
print(new_man[0])
#输出第一行
print(new_man[-1])
#输出最后一行
