import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox)
import sqlite3
con= 'none'
def connection():
	global con
	con=sqlite3.connect("demo.db")

def insert(Name, Ph_no, Email,t_table):
	global con
	Query= "insert into My_Contacts values('"+Name+"','"+Ph_no+"','"+Email+"')"
	try:
		con.execute(Query)
		con.commit()
	except:
		con.execute("create table My_Contacts(Name varchar(20),Ph_no INT, Email varchar(30))")
		con.execute(Query)
	check(t_table)

def check(t_table):
	global con
	cu = con.execute('select * from My_Contacts')
	k=0
	t_string="<table border=5><tr><th>Name</th><th>Ph_no</th><th>Email</th></tr>"
	for row in cu:
		if len(str(row[0]))!=0:
			t_string+="<tr><td>"+str(row[0])+"</td><td>"+str(row[1])+"</td><td>"+str(row[2])+"</td></tr>"
	t_string+="</table>"
	t_table.setText(t_string)


class LoginForm(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle('Contact Form And Contact List Page')
		self.resize(500, 100)

		layout = QGridLayout()
		#comment Dont have an account?
		label_ad = QLabel('<font size="6"> Add Contacts </font>')
		layout.addWidget(label_ad, 0, 1)

		#sign up button
		
		
		#Email___
		label_name = QLabel('<font size="4"> Name </font>')
		self.lineEdit_user_name = QLineEdit()
		layout.addWidget(label_name, 1, 0)
		layout.addWidget(self.lineEdit_user_name, 2, 0, 1, 3)
		#Password___
		label_ph_no= QLabel('<font size="4"> Ph_no </font>')
		self.lineEdit_ph_no = QLineEdit()
		layout.addWidget(label_ph_no, 3, 0)
		layout.addWidget(self.lineEdit_ph_no, 4, 0, 1, 3)

		label_Email= QLabel('<font size="4"> Email </font>')
		self.lineEdit_Email = QLineEdit()
		layout.addWidget(label_Email, 5, 0)
		layout.addWidget(self.lineEdit_Email, 6, 0, 1, 3)

		# Forgot password dialog
		

		#sign in button
		button_login = QPushButton('Save')
		button_login.clicked.connect(self.extract)
		button_login.setStyleSheet("QPushButton"
                             "{"
                             "background-color : skyblue;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : green;"
                             "}"
                             )
		layout.addWidget(button_login, 7, 2)
		self.t_title = QLabel('<font size="7"> My_Contacts </font>')
		layout.addWidget(self.t_title, 8, 1)

		self.t_table = QLabel()
		layout.addWidget(self.t_table, 9, 1)
		
		
		self.setLayout(layout)

	def extract(self):
		Name= self.lineEdit_user_name.text()
		Ph_no= self.lineEdit_ph_no.text()			
		Email= self. lineEdit_Email.text()
		insert(Name,Ph_no,Email,self.t_table)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	connection()
	form = LoginForm()
	form.show()

	sys.exit(app.exec_())