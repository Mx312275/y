import sys, time, threading




print('< style script >\n')


def Upper_string():
	x = ' [1]  python for ever '
	print (x,end='\r')
	for i in range(3):
		for i in range (0,len(x)):
			print (x[:i].lower()+x[i].upper(),end='\r')
			time.sleep(0.1)
	print('\n')

def Animation():
	y = '\|/-'
	for i in range(10):
		for i in range(0,len(y)):
			print(' [2]   '+y[i],end='\r')
			time.sleep(0.1)
	print('\n')
		




Upper_string()
Animation()
