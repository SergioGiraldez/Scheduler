# SCHEDULER by Sergi Giraldez

#imports
import time
from datetime import datetime


""" Returns the time between now and the date parameter in seconds.
	format of date: seconds """
def get_time_to_date_in_seconds(dateInSeconds):
	return (int(dateInSeconds) - int(round(datetime.now().timestamp())))
