Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 08:06:12) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
================= RESTART: C:\Users\lenovo\Desktop\test4.py =================
>>> dir()
['AthleteList', '__annotations__', '__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'get_coach_data', 'get_from_store', 'os', 'pickle', 'put_to_store', 'sanitize']
>>> the_files=['sarah.txt','james.txt','mikey.txt','julie.txt']
>>> data=put_to_store(the_files)
>>> data
{'2:58': ['2:39', '2-25', '2-55', '2:54', '2.18', '2:55', '2:55'], '2-34': ['2.34', '2.45', '3.01', '2:01', '2:01', '3:10', '2-22'], '2:22': ['3:01', '3.02', '3:02', '3.02', '3:22', '2.49', '2:38'], '2.59': ['2:11', '2:23', '3-10', '2-23', '3:10', '3.21', '3-21']}
>>> import os
>>> os.chdir('F:\chapter3')
>>> the_files=['sarah.txt','james.txt','mikey.txt','julie.txt']
>>> data=put_to_store(the_files)
>>> data
{'Sarah Sweeney': ['2:58', '2.58', '2:39', '2-25', '2-55', '2:54', '2.18', '2:55', '2:55'], 'James Lee': ['2-34', '3:21', '2.34', '2.45', '3.01', '2:01', '2:01', '3:10', '2-22'], 'Mikey McManus': ['2:22', '3.01', '3:01', '3.02', '3:02', '3.02', '3:22', '2.49', '2:38'], 'Julie Jones': ['2.59', '2.11', '2:11', '2:23', '3-10', '2-23', '3:10', '3.21', '3-21']}
>>> for each_athlete in data:
	print(data[each_athlete].name+' '+data[each_athlete].dob)

	
Sarah Sweeney 2002-6-17
James Lee 2002-3-14
Mikey McManus 2002-2-24
Julie Jones 2002-2-24
>>> data_copy=get_from_store()
>>> for each_athlete in data_copy:
	print(data_copy[each_athlete].name+' '+data_copy[each_athlete].dob)

	
Sarah Sweeney 2002-6-17
James Lee 2002-3-14
Mikey McManus 2002-2-24
Julie Jones 2002-2-24
>>> 
