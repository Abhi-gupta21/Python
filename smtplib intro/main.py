#5r%XnOMiu)40GJ
import smtplib

my_email = "abhtecho@gmail.com"
password = "zdfe wjll blym bbeb"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user = my_email, password = password)
message = "you are the prettiest!!       " * 100000
connection.sendmail(from_addr = my_email, to_addrs = "hesaree123@gmail.com", msg = message)
connection.close()

# come back to this day, its quite interesting. You could not do it cause of gmail problem.