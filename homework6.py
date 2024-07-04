my_dict = {'sunur': 1997, 'ruslan': 1983,'maxim': 1991}
print(my_dict)
print(my_dict['sunur'])
print(my_dict.get('ara'))
my_dict['ara'] = 1996
my_dict['kamila']= 1995
print(my_dict['ara'])
del my_dict['ruslan']
print(my_dict.get('ruslan'))
print(my_dict)

my_set = {'sunur',1,2,3,'sunur',1,2,3}
print(my_set)
my_set.update(['kamila','ara'])
my_set.discard(1)
print(my_set)