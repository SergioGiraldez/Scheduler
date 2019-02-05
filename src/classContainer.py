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


""" Returns the time between now and the date parameter in seconds.
	format of date: seconds """
def get_time_to_date_in_seconds(dateInSeconds):
	return (int(dateInSeconds) - int(round(datetime.now().timestamp())))
