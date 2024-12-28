def time(time_str):
    if 'AM' in time_str or 'PM' in time_str:
        return convert_to_24_hour(time_str)
    else:
        return convert_to_12_hour(time_str)
def convert_to_24_hour(time_str):
    time_part = time_str[:-2].strip()
    am_pm = time_str[-2:]
    hours, minutes = map(int, time_part.split(':'))

    if am_pm == 'PM' and hours != 12:
        hours += 12
    elif am_pm == 'AM' and hours == 12:
        hours = 0
    return f"{hours:02}:{minutes:02}"
def convert_to_12_hour(time_str):
    hours, minutes = map(int, time_str.split(':'))

    am_pm = 'AM'
    if hours >= 12:
        am_pm = 'PM'
        if hours > 12:
            hours -= 12
    elif hours == 0:
        hours = 12

    return f"{hours}:{minutes:02} {am_pm}"

print(time("6:20 PM"))