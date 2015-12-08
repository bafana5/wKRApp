from wKRApp.views import db
from wKRApp.models import Users

# create the database and the db tables
db.create_all()

# insert in Users
db.session.add(Users("123456", 
                     "Brian", 
                     "Nobody", 
                     "bnobody@nowhere.com", 
                     "0812345678", 
                     "Admin", 
                     "C4", 
                     "RAD", 
                     "Business", 
                     "bnobody", 
                     "123456", 
                     "No", 
                     "No")) 
db.session.add(Users("451263", 
                     "Person", 
                     "Someone", 
                     "psomeone@nowhere.com", 
                     "0823456789", 
                     "Supervisor", 
                     "D4", 
                     "RAD", 
                     "Business", 
                     "psomeone", 
                     "654321", 
                     "No", 
                     "No"))
db.session.add(Users("987456", 
                     "Test", 
                     "Sometest", 
                     "tsometest@nowhere.com", 
                     "0823456789", 
                     "User", 
                     "C1", 
                     "RAD", 
                     "Business", 
                     "tsometest", 
                     "456789", 
                     "No", 
                     "No"))

# commit the changes
db.session.commit()