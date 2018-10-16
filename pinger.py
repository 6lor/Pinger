# Automated pinger with logs
import requests
import datetime
import winsound
import time

if __name__ == "__main__":
	try:
		while True:
			# Try pinging the link
			try:
				responce = str(requests.get("http://www.google.com").status_code)
				if responce == "200":
					winsound.PlaySound('sound_success.wav', winsound.SND_FILENAME)
			# If timed out or no connection
			except:
				responce = "No connection"
				winsound.PlaySound('sound_bad.wav', winsound.SND_FILENAME)

			# Get the status and time, add them together and print the result
			print(str(datetime.datetime.now()) + " - " + responce)

			# Sleep
			time.sleep(30)
	except KeyboardInterrupt:
		print("Bye!")