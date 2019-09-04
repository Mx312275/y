
import os

print ('\n[1] Termux\n[2] kali')

x = input('\nEnter number > ')

if x == '1':

	with open('/data/data/com.termux/files/usr/etc/bash.bashrc','r')as y:
		y = y.read()
		X = y.find('alias style=\'python3 ~/.style.py\'')

	if X != -1:
		pass
	else:
		with open('/data/data/com.termux/files/usr/etc/bash.bashrc','a')as file:
			file.write('alias style=\'python3 ~/.style.py\'')



	if os.path.isfile('~/.style.py') == True:
		print ('Restart the application please')
		...
	else:
		os.system('git clone https://github.com/Mx312275/.style')
		os.system('apt install figlet -y')
		os.system('apt install toilet -y')
		os.system('apt install jp2a -y')
		os.system('mv .style/.style.py ~/.style.py')
		os.system('rm -rif .style')
		os.system('clear')
		print ('Restart the application please')

else:
	print('The tool will be downloaded to Kali soon')
