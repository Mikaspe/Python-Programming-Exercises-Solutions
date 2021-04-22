import calendar

mm, dd, yyyy = map(int, input('MM DD YYYY: ').split())

dayId = calendar.weekday(yyyy, mm, dd)

print(calendar.day_name[dayId].upper())
