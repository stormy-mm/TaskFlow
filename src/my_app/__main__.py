from my_app.repositories.task_repository import JsonTaskRepository
from my_app.application.task_application import TaskApplication
from my_app.cli.input_handlers import Handler


def main():
    """Главная функция: репозиторий и приложение создаются здесь, передаются в Handler."""
    repo = JsonTaskRepository("tasks.json")
    app = TaskApplication(repo)
    handler = Handler(app)

    Handler.show_greeting()
    while True:
        handler.handle(input(">>> "))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass