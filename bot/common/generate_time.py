from datetime import date, timedelta


def create_five_days() -> list[str]:
    today = date.today()

    result = [
        (today+timedelta(days=i)).strftime("%d.%m.%Y")
        for i in range(1, 5)
    ]
    
    return result