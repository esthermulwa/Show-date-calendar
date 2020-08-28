"""
TASK: A program that prints The current time, 
date and calendar at your timezone
"""


from datetime import datetime, timedelta
import calendar
import re

timezone = "GMT+5"  
def main():

  patterns_dict = {str(digit): pattern for digit, pattern in enumerate(
    [
      convert([14, 17, 17, 17, 17, 14]),
      convert([4, 12, 20, 4, 4, 31]),
      convert([14, 17, 2, 4, 8, 31]),
      convert([30, 1, 31, 1, 1, 30]),
      convert([16, 16, 20, 31, 4, 4]),
      convert([31, 16, 16, 31, 1, 31]),
      convert([14, 16, 16, 30, 17, 14]),
      convert([30, 1, 1, 1, 1, 1]),
      convert([14, 17, 31, 17, 17, 14]),
      convert([14, 17, 15, 1, 1, 14])
    ]
  )}

  patterns_dict.update([
    ('p', convert([0, 0, 12, 18, 30, 18])),
    ('m', convert([0, 0, 0, 27, 21, 17, 17])),
    ('a', convert([0, 30, 18, 30, 16, 16])),
    (':', convert([0, 4, 4, 0, 4, 4], 2))]
  )

  now = get_current_datetime()

  print(f'Today is {now.strftime("%Y-%m-%d")} \n')

  display_time = f'{now.strftime("%I:%M%p").lower()}'

  display_char = [' ', '@', '*']

# Now lets print the calendar

  for row in range(6):
    for time_char in display_time:
      for col in patterns_dict[time_char][row]:
        print(display_char[col], end="")
      print(" ", end="")
    print()
  print()

  [print(calendar.month(now.year, now.month, 2))]
  
print("---------")

def get_utcOffset():
  utcOffset = int(re.search(r"([+-])(\d+)$", timezone).group()[1])

  if re.search(r"([+-])(\d+)$", timezone).group()[0] == "-":
    utcOffset = utcOffset * -1

  return utcOffset


def get_utcoffset_timedelta():
  return timedelta(hours=-6, minutes=30) \
    if timezone == "GMT" \
    else timedelta(hours=get_utcOffset())


def get_current_datetime():
  now = datetime.now()
  return now - get_utcoffset_timedelta()


def change_onbit(value):
  return 2 if value == 1 else value


def convert(rows, onbit=1):
  result = [[int(num) for num in
           '{0:05d}'.format(
             int(bin(row)[2:])
         )] for row in rows]

  if onbit != 1:
    result = [list(map(change_onbit, row))
               for row in result]
  return result


if __name__ == "__main__":
  main()
