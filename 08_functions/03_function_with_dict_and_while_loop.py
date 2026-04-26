'''8-6. Названия городов
Функция city_country() принимает город и страну, возвращает строку формата "Santiago, Chile".
Вызвать 3 раза и вывести результат.
'''
# def city_country(city, country):
#     location = f'{country.title()}, {city.title()}'
#     return location
# print(city_country('tokio', 'japan'))
# print(city_country('kiev', 'ukraine'))
# print(city_country('gonk kong', 'china'))

'''8-7. Альбом
Функция make_album() принимает имя музыканта и название альбома, возвращает словарь с этой информацией. 
Потом добавить необязательный параметр — количество песен (None по умолчанию). 
Если передано — добавить в словарь. Вызвать 3 раза.'''
# def make_album(artist, album, qtt=None):
#     music = {}
#     if qtt:
#         music = {'artist': artist.title(), 'album': album.title(), 'traks': qtt}
#     else:
#         music = {'artist': artist.title(), 'album': album.title()}
#     return music
# print(make_album('metalica', 'kill im all'))
# print(make_album('toll', '10_000 years'))
# print(make_album('marshakov', 'hate that', 99))

'''8-8. Альбомы пользователя
Берёшь функцию из 8-7. Добавляешь цикл while — спрашиваешь имя музыканта и альбом, передаёшь в make_album(),
выводишь результат. quit — выход.
'''
# def make_album(artist, album, qtt=None):
#     if qtt:
#         music = {'artist': artist, 'album': album, 'qtt': qtt}
#     else:
#         music = {'artist': artist, 'album': album}
#     return music
# while True:
#     quest_artist = input('\nEnter artist name (or "quit" to exit): ')
#     if quest_artist == 'quit':
#         break
#     quest_album = input('\nEnter album name: ')
#     if quest_artist == 'quit':
#         break
#     tracks = input('\nEnter quantity of tracks: ')
#     if tracks == 'quit':
#         break
#     print(make_album(quest_artist, quest_album, tracks))
