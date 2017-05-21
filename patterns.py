import turtle
import alphabet as al
from data import offset, mag
import data

def start(speed):
	turtle.speed(speed)
	turtle.pencolor('white')
	turtle.setpos(-300, 200)

def reset(additional_spacing=False):
	newline()
	if additional_spacing:
		turtle.color('white')
		turtle.setheading(0)
		turtle.fd(20)
	turtle.color(data.color)

def end(letter_spacing):
	global offset
	turtle.pencolor('white')
	turtle.setheading(0)
	turtle.fd(letter_spacing)
	offset += al.mag


def draw_space():

	reset()
	end(20)

def newline():
	y_pos = turtle.position()[1]
	if turtle.position()[0] >= 350:
		turtle.pencolor('white')
		turtle.setpos(-300, y_pos - 60)

def fd_bk(distance):
	''' draw line forward by distance, then
		retrace that distance.'''
	turtle.fd(distance)
	turtle.bk(distance)

def draw_up(distance):
	turtle.setheading(90)
	turtle.fd(distance)

def draw_text(input_string):
	'''
	Call any func from alphabet (al) module. Converts
	param input_string to function calls
	'''
	input_string = input_string[0:]
	print(input_string)
	for i in input_string:
		if i == ' ':
			draw_space()
		else:
			method = getattr(al, 'draw_{}'.format(i))
			method()
			# PROBLEM: adding different char sets in different modules
			# Problem: DRAWING space