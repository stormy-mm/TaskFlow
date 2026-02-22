from datetime import datetime

from my_app.application.task_application import TaskApplication
from my_app.cli.date_parser import ParsingDate
from my_app.common.messages import EDIT_COMMANDS, Messages as Ms
from my_app.core.task_manager import Task
from my_app.common import  exceptions as e


class InputOutput:
    """Класс вывода и ввода"""

    @staticmethod
    def _default_parsing_date(datetime_user: datetime) -> str:
        """Парсинг даты по умолчанию"""
        return ParsingDate(view_date=datetime_user).date_format

    @staticmethod
    def run_add() -> tuple:
        """Добавление задачи"""
        while True:
            try:
                id_ = int(input(Ms.ADD_TASK[0]))
                break
            except ValueError:
                print("Ошибка: id должен быть целым числом")

        result_user = tuple(input(message) for message in Ms.ADD_TASK[1:])
        return id_, *result_user

    @staticmethod
    def run_show(task: Task) -> None:
        """Показ задачи"""
        id_, title, description, status, type_task, created_at, updated_at, deadline = task.__dict__.values()

        print(f"\nНайдена задача\n")
        print(f"ID: {id_}")
        print(f"Заголовок: {title}")
        print(f"Описание: {description if description else 'Отсутствует'}")
        print(f"Статус: {status}")
        print(f"Дата создания: {InputOutput._default_parsing_date(created_at)}")
        print(f"Дата обновления: {InputOutput._default_parsing_date(updated_at)}")
        print(f"Дедлайн: {InputOutput._default_parsing_date(deadline) if deadline else 'Отсутствует'}")

    @staticmethod
    def run_edit(id_: int, app: TaskApplication) -> None:
        """Редактирование задачи"""
        user_in = input("Сразу после ввода атрибута вводите новое значение\n"
                        "Редактировать..\n"
                        "- id <id>\n"
                        "- title <title>\n"
                        "- description <description>\n"
                        "- deadline <deadline>\n"
                        ">>>  ").lower().strip().split()

        if user_in[0] not in EDIT_COMMANDS:
            raise e.IncorrectInput

        try:
            if user_in[0] == "id":
                attribute, value = user_in[0], int(user_in[1])
            else:
                attribute, value = user_in[0], " ".join(user_in[1:])
        except IndexError:
            raise e.IncorrectInput

        match attribute:
            case "id":
                app.edit_id(id_, value)
            case "title":
                app.edit_title(id_, value)
            case "description":
                app.edit_description(id_, value)
            case "deadline":
                app.edit_deadline(id_, value)