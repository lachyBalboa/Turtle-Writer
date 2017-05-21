import turtle
import patterns
from data import mag

# find ways to make more reusable patterns for letters.
# create classes for letters of similar shapes, especially
# d b p q g AND i j t

# create numbers.py and draw numbers
# create characters.py and draw misc characters like + - $ etc.
def draw_a():

	# Initialise
	patterns.reset()
	angle = 60

	# draw letter
	turtle.setheading(angle)
	turtle.fd(mag)
	turtle.setheading(angle - (angle * 2))
	turtle.fd(mag / 2)
	turtle.setheading(angle * 3)
	turtle.fd(mag / 2)
	turtle.backward(mag / 2)
	turtle.setheading(angle - (angle * 2))
	turtle.fd(mag / 2)

	patterns.end(20)


def draw_b():
	patterns.reset()
	angle = 90
	turtle.setheading(angle)
	turtle.fd(mag * 1.415)
	for i in range(2):
		turtle.setheading(-angle / 2)
		turtle.fd(mag / 2)
		turtle.setheading(-angle * 1.5)
		turtle.fd(mag / 2)

	patterns.end(30)

def draw_c():
	patterns.reset()
	angle = 90
	turtle.setheading(angle)
	turtle.fd(mag)
	turtle.setheading(angle - angle)
	patterns.fd_bk(mag / 2)
	turtle.setheading(270)
	turtle.fd(mag)
	turtle.setheading(angle - angle)
	turtle.fd(mag / 2)

	patterns.end(10)

def draw_d():
	patterns.reset()

	angle = 90
	turtle.fd(mag)
	turtle.bk(mag)
	turtle.setheading(angle)
	turtle.fd(mag / 1.5)
	turtle.setheading(angle - angle)
	turtle.fd(mag)
	turtle.setheading(angle)
	turtle.fd(mag * 1.5)
	turtle.bk(mag * 2.17)

	patterns.end(20)

def draw_e():
	patterns.reset()
	angle = 90
	turtle.setheading(angle)
	turtle.fd(mag)
	turtle.setheading(angle - angle)
	turtle.fd(mag / 2)
	turtle.setheading(angle * 3)
	turtle.fd(mag / 2)
	turtle.setheading(angle * 2)
	turtle.fd(mag / 2)
	turtle.setheading(angle * 3)
	turtle.fd(mag * 0.5)
	turtle.setheading(0)
	turtle.fd(mag / 2)

	patterns.end(20)

def draw_f():
	patterns.reset()

	angle = 90
	turtle.setheading(angle)
	turtle.fd(mag)
	for i in range(2):
		turtle.setheading(angle - angle)
		turtle.fd(mag / 2)
		turtle.bk(mag / 2)
		turtle.setheading(angle * 3)
		turtle.fd(mag / 3)
	turtle.fd(mag / 3)

	patterns.end(40)

def draw_g():
	patterns.reset(additional_spacing=True)

	angle = 90

	turtle.setheading(angle)
	turtle.fd(mag)

	for i in range(3):
		turtle.lt(90)
		turtle.fd(mag / 2)

	turtle.setheading(angle * 3)
	turtle.fd(mag - 10)
	turtle.setheading(angle - angle)
	turtle.bk(mag / 2)
	turtle.setheading(angle)
	turtle.fd(mag / 3)
	turtle.bk(mag / 3)
	turtle.setheading(angle - angle)
	turtle.fd(mag / 2)

	patterns.end(20)

def draw_h():
	patterns.reset()

	turtle.setheading(90)
	turtle.fd(mag)
	turtle.bk(mag / 2)
	turtle.setheading(0)
	turtle.fd(mag / 2)
	turtle.setheading(270)
	turtle.fd(mag / 2)

	patterns.end(20)

def draw_i():
	patterns.reset(additional_spacing=True)

	turtle.setheading(90)
	turtle.fd(5)

	def draw_line():
		turtle.setheading(0)
		turtle.fd(mag / 2)
		turtle.bk(mag)
		turtle.fd(mag / 2)
	draw_line()
	turtle.setheading(90)
	turtle.fd(mag)
	draw_line()

	turtle.setheading(270)
	turtle.fd(mag + 5)

	patterns.end(40)

def draw_j():
	patterns.reset(additional_spacing=True)
	turtle.setheading(180)
	turtle.fd(mag / 2)
	turtle.setheading(90)
	turtle.fd(10)
	turtle.bk(10)
	turtle.setheading(0)
	turtle.fd(mag / 2)
	turtle.setheading(90)
	turtle.fd(mag)
	turtle.setheading(180)
	turtle.fd(mag / 2)
	turtle.bk(mag)
	turtle.fd(mag / 2)

	turtle.setheading(270)
	turtle.fd(mag)

	patterns.end(40)

def draw_k():
	patterns.reset()

	turtle.setheading(90)
	turtle.fd(mag)
	turtle.bk(mag / 2)

	def draw_arms(reverse=False):
		angle = 60
		if reverse:
			angle = -60
		turtle.setheading(angle)
		turtle.fd(mag / 2 + 10)
		turtle.bk(mag / 2 + 10)

	draw_arms()
	draw_arms(reverse=True)

	turtle.setheading(270)
	turtle.fd(mag / 2)

	patterns.end(30)

def draw_l():
	patterns.reset()

	turtle.setheading(90)
	patterns.fd_bk(mag)
	turtle.setheading(0)
	turtle.fd(mag / 2)

	patterns.end(20)


def draw_m():
	patterns.reset()

	for i in range(2):
		turtle.setheading(60)
		turtle.fd(mag / 2)
		turtle.setheading(-60)
		turtle.fd(mag / 2)
	patterns.end(30)

def draw_n():
	patterns.reset()

	turtle.setheading(60)
	turtle.fd(mag / 2)
	turtle.setheading(-60)
	turtle.fd(mag / 2)
	turtle.setheading(60)
	patterns.fd_bk(mag / 2)

	patterns.end(20)

def draw_o():
	patterns.reset()

	patterns.fd_bk(mag / 2)
	turtle.setheading(90)
	turtle.fd(mag / 2)
	turtle.setheading(0)
	turtle.fd(mag / 2)
	turtle.setheading(270)
	turtle.fd(mag / 2)
	patterns.end(20)


def draw_p():
	patterns.reset()

	turtle.setheading(90)
	turtle.fd(mag)
	turtle.setheading(0)
	turtle.fd(mag / 2)
	turtle.setheading(270)
	turtle.fd(mag / 2)
	turtle.setheading(180)
	turtle.fd(mag / 2)
	turtle.setheading(270)
	turtle.fd(mag / 2)

	patterns.end(30)

def draw_q():
	patterns.reset()

	turtle.setheading(90)
	turtle.fd(mag / 2)
	turtle.setheading(0)
	turtle.fd(mag / 2)
	turtle.setheading(270)
	turtle.fd(mag / 2)
	turtle.setheading(180)
	turtle.fd(mag / 2)
	turtle.bk(mag / 2)
	turtle.setheading(270)
	turtle.fd(mag / 2)
	turtle.bk(mag / 2)

	patterns.end(20)

def draw_r():
	patterns.reset()

	turtle.setheading(90)
	turtle.fd(mag)
	turtle.setheading(0)
	turtle.fd(mag / 2)
	turtle.setheading(270)
	turtle.fd(mag / 2)
	turtle.setheading(180)
	turtle.fd(mag / 2)
	turtle.setheading(-60)
	turtle.fd(mag / 2 + 3)

	patterns.end(20)

def draw_s():
	patterns.reset()

	turtle.fd(mag / 2)
	turtle.setheading(90)
	turtle.fd(mag / 2)
	turtle.setheading(180)
	turtle.fd(mag / 2)
	turtle.setheading(90)
	turtle.fd(mag / 2)
	turtle.setheading(0)
	turtle.fd(mag / 2)

	turtle.bk(mag / 2)
	turtle.setheading(270)
	turtle.fd(mag / 2)
	turtle.setheading(0)
	turtle.fd(mag / 2)
	turtle.setheading(270)
	turtle.fd(mag / 2)

	patterns.end(20)

def draw_t():
	patterns.reset()
	patterns.draw_up(40)
	turtle.setheading(0)
	turtle.fd(mag / 2)
	turtle.bk(mag)
	turtle.fd(mag / 2)
	turtle.setheading(270)
	turtle.fd(mag)
	patterns.end(20)

def draw_u():

	patterns.reset()
	patterns.draw_up(30)

	turtle.bk(mag - 10)
	turtle.setheading(0)
	turtle.fd(mag / 2)
	patterns.draw_up(30)
	turtle.bk(mag - 10)

	patterns.end(20)

def draw_v():
	patterns.reset()
	turtle.setheading(-60 * 4)
	patterns.fd_bk(30)
	turtle.setheading(60)
	patterns.fd_bk(30)

	patterns.end(20)



def draw_w():
	patterns.reset()
	turtle.setheading(-60 * 4)
	patterns.fd_bk(30)
	turtle.setheading(60)
	turtle.fd(30)
	turtle.setheading(-60)
	turtle.fd(30)
	turtle.setheading(60)
	patterns.fd_bk(30)
	patterns.end(40)

def draw_x():
	patterns.reset()

	turtle.setheading(60)
	turtle.fd(mag)
	turtle.bk(mag / 2)
	turtle.setheading(- 60 * 4)
	turtle.fd(mag / 2)
	turtle.bk(mag)

	patterns.end(20)

def draw_y():
	patterns.reset()

	turtle.setheading(60)
	turtle.fd(mag)
	turtle.bk(15)
	turtle.setheading(-60 * 4)
	patterns.fd_bk(mag / 2)
	turtle.setheading(60)
	turtle.bk(mag - 15)

	patterns.end(30)

def draw_z():
	patterns.reset()

	turtle.setheading(180)
	turtle.fd(mag / 2)
	turtle.setheading(60)
	turtle.fd(mag)
	turtle.setheading(180)
	patterns.fd_bk(mag / 2)

	turtle.setheading(60)
	turtle.bk(mag)
	turtle.setheading(0)
	turtle.fd(mag / 2)

	patterns.end(30)
