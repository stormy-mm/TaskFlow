from .repositories.task_sql import SqliteTaskRepository
from .application.task_application import TaskApplication
from .cli.input_handlers import Handler


def main():
    """Главная функция: репозиторий и приложение создаются здесь, передаются в Handler."""
    db = SqliteTaskRepository('tasks.db') # инициализация json репозитория
    app = TaskApplication(db) # инициализация приложения
    handler = Handler(app) # инициализация обработчика

    handler.show_greeting()
    while True:
        handler.user_handler(input(">>> "))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass