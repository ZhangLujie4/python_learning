import os
os.chdir('F:\chapter3')
def sanitize(time_string):
    if '-' in time_string:
        splitter='-'
    elif ':' in time_string:
        splitter=':'
    else:
        return(time_string)
    (mins,secs)=time_string.split(splitter)
    return(mins+'.'+secs)
"""def get_coach_data(filename):
    try:
        with open(filename) as f:
            data=f.readline()
        temp=data.strip().split(',')
        return({'Name':temp.pop(0),
                'DOB':temp.pop(0),
                'Times':str(sorted(set([sanitize(t) for t in temp]))[0:3])})
    except IOError as ioerr:
        print('File error:'+str(ioerr))
        return(None)
sarah=get_coach_data('sarah2.txt')
print(sarah['Name']+"'s fastest times are:"+sarah['Times'])"""

#python中的类
class Athlete:
    def __init__(self,a_name,a_dob=None,a_times=[]):
        #init前后各有两根下划线，真坑
        #不然就会提示错误TypeError: object() takes no parameters
        self.name=a_name
        self.dob=a_dob
        self.times=a_times
    def top3(self):
        return(sorted(set([sanitize(t) for t in self.times]))[0:3])
    def add_time(self,time_value):
        self.times.append(time_value)
    def add_times(self,list_of_times):
        self.times.extend(list_of_times)
    
def get_coach_data(filename):
        try:
            with open(filename) as f:
                data=f.readline()
                templ=data.strip().split(',')
                return(Athlete(templ.pop(0),templ.pop(0),templ))
        except IOError as ioerr:
            print('File error:'+str(ioerr))
            return(None)
sarah=get_coach_data('sarah2.txt')
print(sarah.name+"'s fastest times are:"+str(sarah.top3()))
vera=Athlete('Vera vi')
vera.add_time('1.31')
print(vera.times)
vera.add_times(['2.22','1-21','2:22'])
print(vera.top3())


#python中类的继承
class AthleteList(list):
    def __init__(self,a_name,a_dob=None,a_times=[]):
        list.__init__([])
        self.name=a_name
        self.dob=a_dob
        self.extend(a_times)
    def top3(self):
        return(sorted(set([sanitize(t) for t in self]))[0:3])
    #数据本身是计时数据，所以不再需要“times”属性
    #我觉得从好多地方都可以看出python的“随意性”，便捷性
vera=Athlete('Vera vi')
vera.add_time('1.31')
print(vera.top3())
vera.add_times(['2.22','1-21','2:22'])
print(vera.top3())
