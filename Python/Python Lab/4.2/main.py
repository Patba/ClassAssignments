# dziedziczenie z typow immutable

class PositiveNumberTuple(tuple):

    def __new__(cls, *numbers):

        skipped_value_count = 0
        positive_numbers = []

        for number in numbers:
            if number >= 0:
                positive_numbers.append(number)
            else:
                skipped_value_count += 1

        instance = super().__new__(cls, tuple(positive_numbers))
        instance.skipped_value_count = skipped_value_count
        return instance


positive_ints_tuple = PositiveNumberTuple(-3, -5, 0, 5, 9, 627, -1, 26, 24, 2, 8)

print(positive_ints_tuple)

print(type(positive_ints_tuple))
