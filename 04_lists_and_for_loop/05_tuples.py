'''Создаем кортеж из 5ти значений и принтуем его циклом'''
gap = '\n'
f1_champ_list = ('Michael Schumacher ', 'Juan Manuel Fangio', 'Alain Prost ', 'Ayrton Senna',
                 'Niki Lauda')
champ_mess = 'Outstanding Formula 1 champions:'
print(champ_mess)
for champ in f1_champ_list:
    print(champ)
print(gap*3)

'''Изменим список и выведем его снова'''
f1_champ_list = ('Charles Leclerc', 'Max Verstappen', 'Alain Prost ', 'Ayrton Senna',
                 'Niki Lauda')
print(champ_mess)
for champ in f1_champ_list:
    print(champ)
print(gap)