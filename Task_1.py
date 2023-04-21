
x = 0 
while x < 5:
    name = str(input("გთხოვთ შეიყვანოთ მომხმარებილს სახელი: "))
    surname = str(input("გთხოვთ შეიყვანოთ მომხარებლის გვარი: "))
    try:
        if name == "ლუკა" and surname == "კარჟალოვი":
            print("თქვენ წარმატებით გაიარეთ რეგისტრაცია")
            x = 5
        else:
            print("თქვენს მიერ შეყვანილი სახელი ან გვარი არასწორია")
    except: 
        TypeError
    x+=1

# Solve with calsses
class registration():
    def __init__(self,name,surname) -> None:
        self.name = name
        self.surname = surname
    def __eq__(self,a1:object) -> None:
        try:
            isinstance(a1,registration)
            i = 0 
            while i < 5:
                if a1.name == self.name and a1.surname == self.surname:
                    print(self.__str__())
                    i = 5
                else:
                    print("თქვენს მიერ შეყვანილი სახელი ან გვარი არასწორია")
                    self.name = input("შეიყვანეთ თქვენი სახელი:  ")
                    self.surname = input("შეიყვანეთ თქვენი გვარი: ")
                    i+=1
        except:
            print("ERROR")
    def __str__(self) -> str:
        return "გილოცავთ თქვენ წარმატებით გაიარეთ რეგისტრაცია"
L = registration("ლუკა","კარჟალოვი")
User = registration(str(input("შეიყვანეთ თქვენი სახელი: ")),str(input("შეიყვანეთ თქვენი გვარი: ")))
print(User.__eq__(L))
