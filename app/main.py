#app/cinema/bar.py
class CinemaBar:
    @staticmethod
    def sell_product(product: str, customer_name: str) -> None:
        print(f"Cinema bar sold {product} to {customer_name}.")

#app/people/customer.py
class Customer:
    def __init__(self, name: str, food: str) -> None:
        self.name = name
        self.food = food

    def watch_movie(self, movie: str) -> None:
        print(f'{self.name} is watching "{movie}".')

#app/people/cinema_staff.py
class Cleaner:
    def __init__(self, name: str) -> None:
        self.name = name

    def clean_hall(self, hall_number: int) -> None:
        print(
            f"Cleaner {self.name} is cleaning hall number {hall_number}."
        )

#app/cinema/hall.py
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(
        self,
        movie: str,
        customers: list[Customer],
        cleaner: Cleaner
    ) -> None:
        print(f'"{movie}" started in hall number {self.number}.')

        for customer in customers:
            customer.watch_movie(movie)

        print(f'"{movie}" ended.')

        cleaner.clean_hall(self.number)

#app/main.py
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: list[dict],
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    customer_objects: list[Customer] = []

    for customer in customers:
        CinemaBar.sell_product(
            customer["food"],
            customer["name"]
        )

        customer_objects.append(
            Customer(
                customer["name"],
                customer["food"]
            )
        )

    hall = CinemaHall(hall_number)
    cleaner_obj = Cleaner(cleaner)

    hall.movie_session(
        movie,
        customer_objects,
        cleaner_obj
    )


