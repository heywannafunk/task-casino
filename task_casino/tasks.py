from dataclasses import dataclass
from enum import Enum
import random


class TaskType(Enum):
    COURSE = 0
    READING = 1


@dataclass
class Task():
    name: str
    type: TaskType
    url: str
    progress: float
    done: bool


class TaskDeck():
    def __init__(self, name='defaultDeck'):
        self.name = name
        self.tasks = []

    def add_task(self): # TODO: add addition of a Task object
        name = input('Type the name of your task: ')
        type = 0
        url = input('Type the url of your task: ')
        progress = 0.0
        done = False
        task = Task(name, type, url, progress, done)
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)


def create_deck():
    pass


class TaskDealer():
    def __init__(self, name='defaultDealer', decks=[]):
        self.name = name
        self.decks = decks

    def add_deck(self, deck):
        self.decks.append(deck)

    def remove_deck(self, deck):
        self.decks.remove(deck)

    def deal(self, scheme=[1]):
        tasks = []
        for i, number_of_tasks in enumerate(scheme):
            tasks.append(random.sample(self.decks[i].tasks, number_of_tasks))
        print(tasks)
        return tasks


@dataclass
class Hand():
    tasks: list[Task]