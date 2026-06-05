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
message = (
    "you are charged with crimes against humanity. "
    "You are required to appear in the Nuremberg courtroom on November 20, 1945, for sentencing."
)

print(len(usernames))

print(f"{usernames[0]}, {message}{gap}")
print(f"{usernames[1]}, {message}{gap}")
print(f"{usernames[2]}, {message}{gap}")
print(f"{usernames[3]}, {message}{gap}")
print(f"{usernames[4]}, {message}{gap}")
print(f"{usernames[5]}, {message}{gap}")
