from handlers import Handler as Har
# from user_input import UserInput as UrI


def main():
    """Главная функция"""
    Har.show_greeting()
    us_in = input(">>> ").lower().strip()
    Har.handler(us_in)

if __name__ == '__main__':
    main()