import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox)
import sqlite3
import contact
con = 'none'
def connection():
	global con
	con=sqlite3.connect("demo.db")

def insert(Query):
	global con
	try:

		con.execute(Query)
		con.commit()
	except:
		con.execute("create table cred(Email varchar(20),password varchar(20),Secret varchar(20))")
	return 1
def check(Email, password, Query):
	global con
	cu = con.execute(Query)
	k=0
	for row in cu:
		if row[0]==Email and row[1]==password:
			return 1
		else:
			k=1
	if k==1:
		return 0

class LoginForm(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle('Sign In')
		self.resize(500, 120)

		layout = QGridLayout()
		#comment Dont have an account?
		label_ad = QLabel('<font size="3"> Dont have an account? </font>')
		layout.addWidget(label_ad, 0, 0)

		#sign up button
		label1=QLabel()
		label1.setText('SignUp')
		label1.mouseReleaseEvent = main2
		layout.addWidget(label1, 0, 1)
		
		#Email___
		label_name = QLabel('<font size="4"> Email </font>')
		self.lineEdit_username = QLineEdit()
		layout.addWidget(label_name, 1, 0)
		layout.addWidget(self.lineEdit_username, 2, 0, 1, 3)
		#Password___
		label_password = QLabel('<font size="4"> Password </font>')
		self.lineEdit_password = QLineEdit()
		layout.addWidget(label_password, 3, 0)
		layout.addWidget(self.lineEdit_password, 4, 0, 1, 3)

		# Forgot password dialog
		label_ad = QLabel('<font size="3"> Forgot Password? </font>')
		layout.addWidget(label_ad, 5, 2)

		#sign in button
		button_login = QPushButton('Sign In')
		button_login.clicked.connect(self.check_password)
		button_login.setStyleSheet("QPushButton"
                             "{"
                             "background-color : skyblue;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : green;"
                             "}"
                             )
		layout.addWidget(button_login, 6, 0, 1, 3)
		
		self.setLayout(layout)

	def check_password(self):
		msg = QMessageBox()
		Email= self.lineEdit_username.text()
		password= self.lineEdit_password.text()
		Query= "select * from cred"
		flag= check(Email, password, Query)
		if flag == 1  :
			#msg.setText('Success')
			#msg.exec_()
			#app.quit()
			contact.connection()
			self.show_c = contact.LoginForm()
			self.show_c.show()
		else:
			msg.setText('Incorrect Password')
			msg.exec_()



class SignUp(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle('Sign Up')
		self.resize(500, 120)

		layout = QGridLayout()
		#Already have an account?
		label_ad = QLabel('<font size="3"> Already have an account?  </font>')
		layout.addWidget(label_ad, 0, 0)
		#SignIn
		label1=QLabel()
		label1.setText('SignIn')
		label1.mouseReleaseEvent = main1
		layout.addWidget(label1, 0, 1)
		#Email
		label_name = QLabel('<font size="4"> Email </font>')
		self.lineEdit_username = QLineEdit()
		layout.addWidget(label_name, 1, 0)
		layout.addWidget(self.lineEdit_username, 2, 0)

		label_password = QLabel('<font size="4"> Password </font>')
		self.lineEdit_password = QLineEdit()
		layout.addWidget(label_password, 3, 0)
		layout.addWidget(self.lineEdit_password, 4, 0)

		label_Secret = QLabel('<font size="4"> Secret </font>')
		self.lineEdit_Secret = QLineEdit()
		layout.addWidget(label_Secret, 5, 0)
		layout.addWidget(self.lineEdit_Secret, 6, 0)	


		button_login = QPushButton('Sign Up')
		button_login.clicked.connect(self.check_password)
		button_login.setStyleSheet("QPushButton"
                             "{"
                             "background-color : skyblue;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : green;"
                             "}"
                             )
		layout.addWidget(button_login, 7, 0, 1, 2)
		#layout.setRowMinimumHeight(2, 75)

		label_ad = QLabel('<font size="3"> By clicking the "SignUp" button, you are creating an account, and you agree to the Terms of Use. </font>')
		layout.addWidget(label_ad, 8, 0, 1, 2)
		

		self.setLayout(layout)

	

	def check_password(self):
		msg = QMessageBox()
		Email= self.lineEdit_username.text()
		password= self.lineEdit_password.text()
		Secret= self. lineEdit_Secret.text()
		Query= "insert into cred values('"+Email+"','"+password+"','"+Secret+"')"
		flag= insert(Query)
		if flag == 1  :
			msg.setText('User Created')
			msg.exec_()
			app.quit()
		else:
			msg.setText('Failed to create')
			msg.exec_()


def main2(a1):
	global form
	form = SignUp()
	form.show()
def main1(a2):
	global form
	form = LoginForm()
	form.show()
if __name__ == '__main__':
	app = QApplication(sys.argv)
	connection()
	form = LoginForm()
	form.show()

	sys.exit(app.exec_())