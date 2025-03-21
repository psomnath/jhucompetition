a = 'abc.def.csv'
ex=a.split('.')[-1]
print(a.replace(ex,'')[:-1])