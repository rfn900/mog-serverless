def one_month_ago_date(today):
    if today.month == 1:
        one_month_ago = today.replace(year=today.year - 1, month=12)
    else:
        extra_days = 0
        while True:
            try:
                one_month_ago = today.replace(
                    month=today.month - 1, day=today.day - extra_days)
                break
            except ValueError:
                extra_days += 1

    return one_month_ago.strftime("%Y-%m-%d")
