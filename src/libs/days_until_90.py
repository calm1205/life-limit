from datetime import date

def days_until_90(birthdate: date) -> int:
    today = date.today()
    
    ninetieth_birthday = date(birthdate.year + 90, birthdate.month, birthdate.day)
    
    if today < ninetieth_birthday:
        delta = ninetieth_birthday - today
        return delta.days
    else:
        return 0