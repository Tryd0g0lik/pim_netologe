import datetime
from application.salary import calculate_salary
from application.db.people import get_employees



if __name__ == '__main__':
  c = calculate_salary()
  g = get_employees()

  print(datetime.date.today())