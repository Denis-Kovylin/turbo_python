"""Суть залачи: создать переменную с цветом пришелца. Конструкцией if-elif-else проверять цвет пришелца
и выводить соответствующее цвета пришельца сообщение"""

gap = "\n"
score_5_mess = "Congratulations on taking out that monster! You get 5 points for that."
score_10_mess = (
    "Congratulations on taking out that monster! You get 10 points for that."
)
score_15_mess = (
    "Congratulations on taking out that monster! You get 15 points for that."
)
error_mess = "Something went wrong(( Please try again later!"
alien_colors_tuple = ("green", "yellow", "red", "blue")
alien_color = alien_colors_tuple[2]

if alien_color == "green":
    print(score_5_mess, gap * 3)
elif alien_color == "yellow":
    print(score_10_mess, gap * 3)
elif alien_color == "red":
    print(score_15_mess, gap * 3)
else:
    print(error_mess, gap * 3)

"""пишем проверку на возрастную категорию"""
age = 10

if age < 2:
    print("This is a baby")
elif age >= 2 and age < 4:
    print("This is a child")
elif age >= 4 and age < 13:
    print("Thi sis a teenager")
elif age >= 13 and age < 20:
    print("This is a young man")
elif age >= 20 and age < 65:
    print("This si adult")
elif age >= 65 and age <= 150:
    print("This is lod mam")
else:
    print(error_mess)
print(gap * 3)

"""Проверка на наличие фрукта в списке"""
fruits: list = ["apples", "bananas", "mango", "plums", "watermelons"]

if "apples" in fruits:
    print(f"I really like {fruits[0]}")
if "bananas" in fruits:
    print(f"I really like {fruits[1]}")
if "mango" in fruits:
    print(f"I really like {fruits[2]}")
if "plums" in fruits:
    print(f"I really like {fruits[3]}")
if "watermelons" in fruits:
    print(f"I really like {fruits[4]}")
