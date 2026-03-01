from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name:str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: list[Animal] = []
        self.workers: list[Worker] = []

    def add_animal(self, animal: Animal, price: int) -> str:
        if self.__budget < price:
            return "Not enough budget"
        if len(self.animals) == self.__animal_capacity :
            return "Not enough space for animal"

        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker) -> str:
        if len(self.workers) == self.__workers_capacity:
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name: str) -> str:
        worker = next((w for w in self.workers if w.name == worker_name), None)
        if worker :
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"
    def pay_workers(self) -> str:
        overall_to_pay = sum([w.salary for w in self.workers])
        if overall_to_pay <= self.__budget:
            self.__budget -= overall_to_pay
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self) -> str:
        overall_to_pay = sum([a.money_for_care for a in self.animals])
        if overall_to_pay <= self.__budget:
            self.__budget -= overall_to_pay
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int) -> int:
        self.__budget += amount
        return self.__budget

    def animals_status(self):
        result = [f"You have {len(self.animals)} animals"]
        # group animals by their class name in first-seen order
        groups: dict[str, list[Animal]] = {}
        for animal in self.animals:
            cls_name = animal.__class__.__name__
            if cls_name not in groups:
                groups[cls_name] = []
            groups[cls_name].append(animal)

        for cls_name, animals in groups.items():
            # pluralize by simply adding 's' (matches the exercise convention)
            result.append(f"----- {len(animals)} {cls_name}s:")
            for a in animals:
                result.append(f"{a}")
        return "\n".join(result)

    def workers_status(self):
        result = [f"You have {len(self.workers)} workers"]
        # group animals by their class name in first-seen order
        groups: dict[str, list[Worker]] = {}
        for worker in self.workers:
            cls_name = worker.__class__.__name__
            if cls_name not in groups:
                groups[cls_name] = []
            groups[cls_name].append(worker)

        for cls_name, animals in groups.items():
            # pluralize by simply adding 's' (matches the exercise convention)
            result.append(f"----- {len(animals)} {cls_name}s:")
            for a in animals:
                result.append(f"{a}")
        return "\n".join(result)
