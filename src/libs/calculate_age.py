from datetime import date

def calculate_age(birthdate: date) -> int:
    today = date.today()
    age = today.year - birthdate.year

    is_birthday_passed = (today.month, today.day) >= (birthdate.month, birthdate.day)
    if not is_birthday_passed:
        age -= 1

    return age
