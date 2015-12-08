from wKRApp.views import db

class Users(db.Model):
    __tablename__ = "users"
    id          = db.Column(db.Integer, primary_key=True)
    employeeID  = db.Column(db.String, nullable=False)
    name        = db.Column(db.String, nullable=False)
    surname     = db.Column(db.String, nullable=False)
    email       = db.Column(db.String, nullable=False)
    telephone   = db.Column(db.String, nullable=False)
    userRole    = db.Column(db.String, nullable=False)
    careerLevel = db.Column(db.String, nullable=False)
    careerLadder= db.Column(db.String, nullable=False)
    unit        = db.Column(db.String, nullable=False)
    username    = db.Column(db.String, nullable=False)
    password    = db.Column(db.String, nullable=False)
    blocked     = db.Column(db.String, nullable=False)
    destroyed   = db.Column(db.String, nullable=False)

    def __init__(self, employeeID, 
                       name, 
                       surname, 
                       email, 
                       telephone, 
                       userRole, 
                       careerLevel,
                       careerLadder,
                       unit,
                       username,
                       password,
                       blocked,
                       destroyed):
        self.employeeID  = employeeID
        self.name        = name
        self.surname     = surname
        self.email       = email
        self.telephone   = telephone
        self.userRole    = userRole
        self.careerLevel = careerLevel
        self.careerLadder= careerLadder
        self.unit        = unit
        self.username    = username
        self.password    = password
        self.blocked     = blocked
        self.destroyed   = destroyed

    def __repr__(self):
        return '<{}>, <{}>, <{}>, <{}>, <{}>, <{}>, <{}>, <{}>, <{}>, <{}>, <{}>, <{}>, <{}>'.format(self.employeeID, 
                                 self.name, 
                                 self.surname,
                                 self.email,
                                 self.telephone,
                                 self.userRole,
                                 self.careerLevel,
                                 self.careerLadder,
                                 self.unit,
                                 self.username,
                                 self.password,
                                 self.blocked,
                                 self.destroyed)