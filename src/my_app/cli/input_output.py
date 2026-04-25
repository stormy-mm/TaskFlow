from ..common.messages import EDIT_COMMANDS, Messages as Ms
from ..common import exceptions as e


class InputOutput:
    """Класс вывода и ввода"""

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
    def run_show(id_, title, description, type_task, status, deadline, created_at, updated_at) -> None:
        """Показ задачи"""
        print(f"\nЗадача № {id_}")
        print(f"Заголовок: {title}")
        print(f"Описание: {description}")
        print(f"Статус: {status}")
        print(f"Дата создания: {created_at}")
        print(f"Дата обновления: {updated_at}")
        print(f"Дедлайн: {deadline if deadline else ""}")

    @staticmethod
    def run_edit() -> tuple:
        """Редактирование задачи"""
        print("Сразу после ввода атрибута вводите новое значение\n"
                "Редактировать..\n"
                "- id <id>\n"
                "- title <title>\n"
                "- description <description>\n"
                "- deadline <deadline>\n")
        user_in = input(">>>  ").strip().split()

        if not user_in:
            raise e.IncorrectInput

        cmd = user_in[0].lower()
        if cmd not in EDIT_COMMANDS:
            raise e.IncorrectInput

        try:
            if cmd == "id":
                return cmd, int(user_in[1])
            return cmd, " ".join(user_in[1:])
        except ValueError, IndexError:
            raise e.IncorrectInput