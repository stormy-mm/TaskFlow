import exceptions as e

from datetime import datetime

from abc import ABC, abstractmethod

from DOMAINS.checks import CheckChangeStatusTask as Check
from DOMAINS.time_clock import Clock


class TaskBehaviour(ABC):
    """Абстрактный класс для поведения задачи"""
    @abstractmethod
    def can_complete(self, task, status) -> bool:
        """Функция для проверки возможности завершения задачи"""
        pass


class SimpleBehavior(TaskBehaviour):
    """Класс для простой задачи"""
    def can_complete(self, task, status) -> bool:
        return Check(task.status, status).execute()


class TimedBehavior(TaskBehaviour):
    """Класс для задачи с временем"""
    def __init__(self, deadline: datetime):
        self.deadline = deadline

    def can_complete(self, task, status) -> bool:
        if Clock.now() <= task.deadline:
            return Check(task.status, status).execute()
        raise e.DeadlineHasExpired