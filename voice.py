#!/user/bin/python3

def call(number):
	## CALL
	# print("Calling...")
	# serialport.write("AT\r")
	# response = serialport.readlines(None)
	# serialport.write("ATD " + number + ';\r')
	# response = serialport.readlines(None)
	# print(response)
	## HANG-UP
	# print("Hanging up...")
	# serialport.write("AT\r")
	# response = serialport.readlines(None)
	# serialport.write("ATH\r")
	# response = serialport.readlines(None)
	# print(response)
	print(number)

def dial():
	# User input
	user_input = input("+1 ").replace("-", "")
	# Checks that the user input is a valid length
	if len(user_input) != 10:
		print("Invalid.")
		dial()
	else:
		# Formats number
		number = "1" + user_input
		# Call "call"
		call(number)

def main():
	dial()

if __name__ == "__main__":
	main()