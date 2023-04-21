number = int(input("შეიყვანეთ რიცხვი: "))
def Binary_convert(number) -> str:
    return f"{number}-ი ორობით ფორმატში ჩაიწერება როგორც {bin(number)[2:]}"
print(Binary_convert(number))