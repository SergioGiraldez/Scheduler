from datetime import datetime

class Task:
	def __init__(self, name, dificulty, date):
		self.name = name
		self.dificulty = dificulty
		self.date = date
		self.posible_dedication_hours = 0
		self.needed_dedication_hours = 0
		self.priority = 0

	def calculate_priority(self, category):
		self.posible_dedication_hours = (get_time_to_date(self.get_date_in_seconds()) * (category.available_hours/24))
		self.needed_dedication_hours = (get_time_to_date(category.first_date) * (int(category.available_hours)/24) * (int(self.dificulty)/int(category.total_dificulty)))
		self.priority = self.posible_dedication_hours - self.needed_dedication_hours

	def get_date_in_seconds(self):
		date = datetime(int(self.date[6:]), int(self.date[3:5]), int(self.date[0:2]))
		return int(round(date.timestamp()))

	def get_time_to_date(date_in_seconds):
		return (int(date_in_seconds) - int(round(datetime.now().timestamp())))
