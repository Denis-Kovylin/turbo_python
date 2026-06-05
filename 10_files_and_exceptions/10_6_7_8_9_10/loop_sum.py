"""10-7. Калькулятор
То же что 10-6 но в цикле while True. quit — выход. При ошибке — continue."""

while True:
    num_1 = input("enter first number (quit to exit): ")
    if num_1 == "quit":
        print("Bie bie")
        break
    num_2 = input("enter second number (quit to exit): ")
    if num_2 == "quit":
        print("Bie bie")
        break
    try:
        num_1 = int(num_1)
        num_2 = int(num_2)
    except ValueError:
        continue
    else:
        print(f"Result: {num_1 + num_2}")
