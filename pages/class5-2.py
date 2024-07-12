def hello():  # def可以定義一個指令 ，這個指令叫做hello，這個指令不需要傳入資料
    print("Hello!")


hello()


def hello2(name):  # def可以定義一個指令 ，這個指令叫做hello2，這個指令需要傳入一個資料
    print("Hello ,{name}!")


hello2("John")  # 這個指令會印出 Hello, John!
hello2("Ray")  # 這個指令會印出 Hello, Ray!


def hello3(
    name, age
):  # def可以定義一個指令 ，這個指令叫做hello3，這個指令需要傳入一個資料
    print("Hello ,{name} ! You are {age} years old!")


hello3("John", 18)  # 這個指令會印出 Hello, John! You are 18 years old!
hello3("Ray", 20)  # 這個指令會印出 Hello, Ray! You are 20 years old!
hello3(age=20, name="Ray")  # 這個指令會印出 Hello, Ray! You are 20 years old!


def age10(age):
    return age + 10
