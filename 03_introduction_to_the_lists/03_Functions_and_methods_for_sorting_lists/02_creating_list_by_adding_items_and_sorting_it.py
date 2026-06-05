"""Создадим пустой список и заполним его командами Ф1. Потом выведим."""

gap = "\n"
f1_teams_list = []
f1_teams_list.append("Scuderia Ferrari")
f1_teams_list.append("Alpine F1 Team")
f1_teams_list.append("Cadillac F1 Team")
f1_teams_list.append("Audi F1 Team")
f1_teams_list.append("Aston Martin Aramco Formula 1")
f1_teams_list.insert(3, "Haas F1 Team")
f1_teams_list.insert(0, "McLaren Formula 1")
f1_teams_list.insert(-1, "Mercedes-AMG Petronas F1 Team")
f1_teams_list.insert(4, "Racing Bulls")
f1_teams_list.insert(-3, "Oracle Red Bull Racing")
f1_teams_list.insert(1, "Williams F1 Team")
print(f1_teams_list, len(f1_teams_list), gap * 3)

"""Повыводим список в разных сотировках без изминения оригинала"""
print(sorted(f1_teams_list), gap)
print(sorted(f1_teams_list, reverse=True), gap)
print(list(reversed(f1_teams_list)), gap)
print(f1_teams_list, gap * 3)

"""Посортируем оригенальный список в алфавитном и обратноалфавитном порядке"""
f1_teams_list.sort(reverse=True)
print(f1_teams_list, gap)
f1_teams_list.sort()
print(f1_teams_list, gap * 3)

"""Вытесним две команды и напишем что они отстой"""
message = "your team really sucks!"
poped_team = f1_teams_list.pop(1)
print(f"{poped_team}, {message}{gap}")
poped_team = f1_teams_list.pop(2)
print(f"{poped_team}, {message}{gap}")
print(f1_teams_list, gap * 3)

"""Удалим разными способами все команда кроме 3х чемпионских"""
f1_teams_list.remove("Alpine F1 Team")
f1_teams_list.remove("Audi F1 Team")
f1_teams_list.remove("Haas F1 Team")
f1_teams_list.remove("Oracle Red Bull Racing")
del f1_teams_list[-1]
del f1_teams_list[-2]
message = "The teams in contention for the championship title are: "
print(f"{message}{f1_teams_list[0]}, {f1_teams_list[1]}, {f1_teams_list[2]}")
