class Task:
	def __init__(self, name, dificulty, date):
		self.name = name
		self.dificulty = dificulty
		self.date = date
		self.posible_dedication_hours = 0
		self.needed_dedication_hours = 0
		self.priority = 0

	def calculate_priority(self,availableHours, firstDate, totalDificulty):
		self.posible_dedication_hours = (getTimeToDate(self.getDateInSeconds()) * (availableHours/24))
		self.needed_dedication_hours = (getTimeToDate(firstDate) * (int(availableHours)/24) * (int(self.dificulty)/int(totalDificulty)))
		self.priority = self.posible_dedication_hours - self.needed_dedication_hours

	def get_date_in_seconds(self):
		t = datetime(int(self.date[6:]), int(self.date[3:5]), int(self.date[0:2]))
		return int(round(t.timestamp()))
