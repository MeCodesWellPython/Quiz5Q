import pgzrun


def drawTopLeft(value):
	screen.draw.text(value,topleft=(50,60))


def drawMiddle(value):
	screen.draw.text(value,topleft=(600,100))


def draw():
	global check
	if check == 3:
		drawTopLeft("Hello!")
	else:
		drawMiddle("Hello World!")
		
		
number = input("Pick a number between 1 and 5: ")
check=int(number)
if number not in ["1","2","3","4","5"]:
	uiop = input("Please enter a number between 1 and 5: ")



#pgzrun.go()