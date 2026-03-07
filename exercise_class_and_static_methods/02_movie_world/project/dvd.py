from calendar import month_name


class DVD:
    def __init__(self, name: str, _id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = _id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented : bool = False

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int) -> "DVD":
        day, month, year = date.split(".")
        month_n = month_name[int(month)]
        return cls(name, id, int(year), month_n, age_restriction)

    def __repr__(self):
        rented = "rented" if self.is_rented else "not rented"
        return (f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) "
                f"has age restriction {self.age_restriction}. Status: {rented}")