# write your imports here


    def cinema_visit(
    customers: list[dict],
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    for customer in customers:
        print(f"Cinema bar sold {customer['food']} to {customer['name']}.")

    print(f'"{movie}" started in hall number {hall_number}.')

    for customer in customers:
        print(f"{customer['name']} is watching \"{movie}\".")

    print(f'"{movie}" ended.')
    print(f"Cleaner {cleaner} is cleaning hall number {hall_number}.")
