# SCHEDULER by Sergi Giraldez

#imports
import time
from datetime import datetime

class Info:
	def __init__(self, available_hours, tasks, first_date, total_dificulty):
		self.available_hours = availableHours
		self.tasks = tasks
		self.first_date = firstDate
		self.total_dificulty = totalDificulty

""" Class that contais every task info and the priority calculus method."""
class Task:
	def __init__(self, name, dificulty, date):
		self.name = name
		self.dificulty = dificulty
		#date = dd-mm-yyyy TODO: ADD HOUR
		self.date = date
		self.posible_dedication_hours = 0
		self.needed_dedication_hours = 0
		#less priority bigger value
		self.priority = 0

	def calculate_priority(self,availableHours, firstDate, totalDificulty):
		self.posible_dedication_hours = (getTimeToDate(self.getDateInSeconds()) * (availableHours/24))
		self.needed_dedication_hours = (getTimeToDate(firstDate) * (int(availableHours)/24) * (int(self.dificulty)/int(totalDificulty)))
		self.priority = self.posible_dedication_hours - self.needed_dedication_hours

	def get_date_in_seconds(self):
		t = datetime(int(self.date[6:]), int(self.date[3:5]), int(self.date[0:2]))
		return int(round(t.timestamp()))

""" Returns the time between now and the date parameter in seconds.
	format of date: seconds """
def get_time_to_date_in_seconds(dateInSeconds):
	return (int(dateInSeconds) - int(round(datetime.now().timestamp())))
