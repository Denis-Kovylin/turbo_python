"""Вывести 3 первых, 3 из середины, 3 последних элемента списка"""

gap = "\n"
drivers_list = [
    "Max Verstappen",
    "Lando Norris",
    "George Russell",
    "Charles Leclerc",
    "Oscar Piastri",
    "Fernando Alonso",
    "Carlos Sainz",
]
print(drivers_list[:3])
print(drivers_list[2:5])
print(drivers_list[-3:], gap * 3)

"""Копирование списка слайсом. Добавление элементов в один и другой список"""
my_f1_teams_list = ["Ferrari", "McLaren", "Mercedes"]
friend_f1_teams_list = my_f1_teams_list[:]
my_f1_teams_list.append("Audi")
my_f1_teams_list.append("Haas")
friend_f1_teams_list.append("Red Bull Racing")
friend_f1_teams_list.append("Cadillac")
message_favorit_teams = "My favorite Formula 1 teams: "

print(message_favorit_teams)
for team in my_f1_teams_list:
    print(team)
print(gap * 3)

print(message_favorit_teams)
for team in friend_f1_teams_list:
    print(team)
print(gap * 3)
