# Создан список людей подлежаших Нюрбернгскому трибуналу;
# Создана повестка на явку в зал суда;
# Поочередно каждому из них бутед "вручена повестка" методом переменных и обращения к списку по индексу;

usernames = [
    "Adolf Hitler",
    "Hermann Göring",
    "Joseph Goebbels",
    "Rudolf Hess",
    "Heinrich Himmler",
    "Wilhelm Keitel",
]
gap = "\n"
message_to_all = (
    "you are charged with crimes against humanity. "
    "You are required to appear in the Nuremberg courtroom on November 20, 1945, for sentencing."
)
message_to_removed_user = (
    "we were wrong. You're a great guy, and all charges against you have been dropped."
)

print(len(usernames))

print(f"{usernames[0]}, {message_to_all}{gap}")
print(f"{usernames[1]}, {message_to_all}{gap}")
print(f"{usernames[2]}, {message_to_all}{gap}")
print(f"{usernames[3]}, {message_to_all}{gap}")
print(f"{usernames[4]}, {message_to_all}{gap}")
print(f"{usernames[5]}, {message_to_all}{gap*2}")

# Далее исключает Гителра из списка в связи с самоубийством и добавляем вместо него в список Зеленского.
# Выводим отмену вызова для Гитлера и повторно выводим сообщение повестки для обновленного списка осужденных

removed_user = usernames.pop(0)
print(f"{removed_user}, {message_to_removed_user}{gap*2}")

usernames.insert(0, "Volodimir Zeleskiy")

print(f"{usernames[0]}, {message_to_all}{gap}")
print(f"{usernames[1]}, {message_to_all}{gap}")
print(f"{usernames[2]}, {message_to_all}{gap}")
print(f"{usernames[3]}, {message_to_all}{gap}")
print(f"{usernames[4]}, {message_to_all}{gap}")
print(f"{usernames[5]}, {message_to_all}{gap*2}")

# Делее список участников розширяется и выводиться обновленная повестка обновленному списку юзеров

usernames.insert(2, "Voladimir Putin")
usernames.insert(1, "Valerii Zaluzhnyi")
usernames.append("Donald Trump")

print(f"{usernames[0]}, {message_to_all}{gap}")
print(f"{usernames[1]}, {message_to_all}{gap}")
print(f"{usernames[2]}, {message_to_all}{gap}")
print(f"{usernames[3]}, {message_to_all}{gap}")
print(f"{usernames[4]}, {message_to_all}{gap}")
print(f"{usernames[5]}, {message_to_all}{gap}")
print(f"{usernames[6]}, {message_to_all}{gap}")
print(f"{usernames[7]}, {message_to_all}{gap}")
print(f"{usernames[8]}, {message_to_all}{gap}")
