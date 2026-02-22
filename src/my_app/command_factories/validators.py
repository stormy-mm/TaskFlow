from datetime import datetime

from my_app.common import exceptions as e
from my_app.common.messages import Status as St


class ICheck:
    """Миксин для проверки разрешения изменения статуса задачи"""
    @staticmethod
    def can_change_status(status, exception, *statuses) -> bool:
        if status in statuses:
            raise exception
        return True


class CheckChangeStatusTask:
    """Класс для проверки разрешения изменения статуса задачи"""
    def __init__(self, task_status, status):
        """Инициализация статуса задачи"""
        self.task_status = task_status
        self.status = status

    def execute(self) -> bool:
        """Проверка разрешения изменения статуса задачи"""
        match self.status:
            case St.DONE:
                return self.can_change_to_done()
            case St.IN_PROGRESS:
                return self.can_change_to_start()
            case St.CANCELLED:
                return self.can_change_to_cancel()
        return False

    def can_change_to_done(self) -> bool:
        """Проверка разрешения изменения статуса задачи на DONE"""
        return ICheck.can_change_status(self.task_status, e.TaskCannotCompleted, St.NEW, St.CANCELLED)

    def can_change_to_start(self) -> bool:
        """Проверка разрешения изменения статуса задачи на IN_PROGRESS"""
        return ICheck.can_change_status(self.task_status, e.TaskCannotStart, St.DONE, St.CANCELLED)

    def can_change_to_cancel(self) -> bool:
        """Проверка разрешения изменения статуса задачи на CANCELLED"""
        return ICheck.can_change_status(self.task_status, e.TaskCannotCancel, St.DONE, St.CANCELLED)


class CheckOverdueStatus:
    """Класс для проверки статуса задачи на OVERDUE"""
    def __init__(self, deadline: datetime, created_at: datetime):
        """Инициализация дедлайна и времени создания задачи"""
        self.deadline = deadline
        self.created_at = created_at

    def run(self) -> str:
        """Запуск проверки"""
        if self.deadline is not None:
            if self.deadline < self.created_at:
                return St.OVERDUE
        return St.NEW