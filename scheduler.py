# SCHEDULER by Sergi Giraldez

#imports
import time
from datetime import datetime

class Info:
	def __init__(self, availableHours, tasks, firstDate, totalDificulty):
		self.availableHours = availableHours
		self.tasks = tasks
		self.firstDate = firstDate
		self.totalDificulty = totalDificulty

""" Class that contais every task info and the priority calculus method."""
class Task:
	def __init__(self, name, dificulty, date):
		self.name = name
		self.dificulty = dificulty
		#date = dd-mm-yyyy TODO: ADD HOUR
		self.date = date
		self.posibleHours = 0
		self.neededHours = 0
		#less priority bigger value
		self.priority = 0

	""" Calculus of the priority, posibleHours and neededHours """
	def calcPriority(self,availableHours, firstDate, totalDificulty):
		self.posibleHours = (getTimeToDate(self.getDateInSeconds()) * (availableHours/24))
		self.neededHours = (getTimeToDate(firstDate) * (int(availableHours)/24) * (int(self.dificulty)/int(totalDificulty)))
		self.priority = self.posibleHours - self.neededHours

	def getDateInSeconds(self):
		t = datetime(int(self.date[6:]), int(self.date[3:5]), int(self.date[0:2]))
		return int(round(t.timestamp()))

""" Returns the time between now and the date parameter in seconds.
	format of date: seconds """
def getTimeToDate(dateInSeconds):
	return (int(dateInSeconds) - int(round(datetime.now().timestamp())))
