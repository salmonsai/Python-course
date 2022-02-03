
#String
number = 100
rubles = 'рублей'
print(str(number), rubles)
number_1 = '200'
print(number_1 + ' ' + rubles)

#Integer
number = '100'
rubles = 'рублей'
print(int(number), rubles)
number_2 = 300
print(int(number) + number_2)


#Float
rubles_one = 1.5
rubles_two = 2.3
print(rubles_one + rubles_two)

#Bytes
bts = bytes(int(rubles_one))
print(bts)

#List
line = ['a', 'b', 'c']
line[1] = 'f' #working
print(list(line))

#Tuple
krt = ('a', 'b', 'c')
#krt[1] = 'f' #must dont't working
print(krt)

#Set
spk = ['a', 'b', 'c', 'a']
spk = set(spk)
spk.add('f')
print(spk)

#Frozen set
spk_1 = frozenset(['a', 'b', 'c', 'b'])
#spk_1.add('f') #must dont't working
print(spk_1)

#Dict
english = {
    'hand': 'рука',
    'new': 'новый',
    'down': 'вниз'
}
print(english)
print(english['new'])
print(english.keys())


