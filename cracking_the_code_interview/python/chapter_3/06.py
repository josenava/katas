"""
python's builtin linked list implementation is deque
"""
from abc import ABC
from collections import deque


class AnimalOrder(ABC):
    def __init__(self, order_n: int, name: str):
        self.order_n = order_n
        self.name = name

    def is_older_than(self, a: "AnimalOrder") -> bool:
        return self.order_n < a.order_n

    def __repr__(self) -> str:
        return f"AO({self.order_n}, {self.name})"


class DogOrder(AnimalOrder):
    pass


class CatOrder(AnimalOrder):
    pass


class AnimalShelter:
    def __init__(self):
        self.dogs_queue: deque = deque()
        self.cats_queue: deque = deque()

    def enqueue(self, animal_order: AnimalOrder):
        if isinstance(animal_order, DogOrder):
            self.dogs_queue.appendleft(animal_order)
        if isinstance(animal_order, CatOrder):
            self.cats_queue.appendleft(animal_order)

    def dequeue_any(self) -> AnimalOrder:
        if len(self.dogs_queue) == 0:
            return self.cats_queue.pop()
        elif len(self.dogs_queue) == 0:
            return self.dogs_queue.pop()

        first_dog = self.dogs_queue[-1]
        first_cat = self.cats_queue[-1]
        if first_dog.order_n < first_cat.order_n:
            return self.dogs_queue.pop()

        return self.cats_queue.pop()

    def dequeue_dog(self) -> DogOrder:
        return self.dogs_queue.pop()

    def dequeue_cat(self) -> CatOrder:
        return self.cats_queue.pop()

    def __repr__(self) -> str:
        return f"AnimalShelter(dogs: {str(self.dogs_queue)}, cats: {str(self.cats_queue)})"


if __name__ == "__main__":
    animal_shelter = AnimalShelter()
    orders = [
        DogOrder(1, "aaaa"),
        DogOrder(2, "bbbbb"),
        CatOrder(3, "hehey"),
        DogOrder(4, "buat"),
        CatOrder(5, "another"),
    ]
    for o in orders:
        animal_shelter.enqueue(o)

    animal1 = animal_shelter.dequeue_any()
    cat1 = animal_shelter.dequeue_cat()
    animal2 = animal_shelter.dequeue_any()
    dog1 = animal_shelter.dequeue_dog()

    assert animal1.order_n == 1
    assert animal1.name == "aaaa"

    assert cat1.name == "hehey"
    assert animal2.name == "bbbbb"
    assert dog1.name == "buat"
