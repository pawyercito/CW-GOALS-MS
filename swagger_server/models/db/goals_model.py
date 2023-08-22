from swagger_server.resources.db import db

class Goals(db.Model):
    __tablename__ = 'goals'
    id_goal = db.Column(db.Integer, primary_key=True)
    internet_dolar = db.Column(db.Float(10,2))
    internet_volumen = db.Column(db.Integer)
    telefonia_dolar = db.Column(db.Float(10,2))
    telefonia_volumen = db.Column(db.Integer)
    television_dolar = db.Column(db.Float(10,2))
    television_volumen = db.Column(db.Integer)
    goal_date = db.Column(db.String(7))
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def __init__(self, payload):
        self.internet_dolar = payload.get('internet_dolar')
        self.internet_volumen = payload.get('internet_volumen')
        self.telefonia_dolar = payload.get('telefonia_dolar')
        self.telefonia_volumen = payload.get('telefonia_volumen')
        self.television_dolar = payload.get('television_dolar')
        self.goal_date = payload.get('goal_date')
        self.television_volumen = payload.get('television_volumen')

    def to_json(self):
        """
        It takes the object and returns a dictionary representation of it
        :return: A dictionary with the keys and values of the user object.
        """
        return {
            "id_goal": self.id_goal,
            "internet_dolar": self.internet_dolar,
            "internet_volumen": self.internet_volumen,
            "telefonia_dolar": self.telefonia_dolar,
            "telefonia_volumen": self.telefonia_volumen,
            "television_dolar": self.television_dolar,
            "television_volumen": self.television_volumen,
            "goal_date": self.goal_date,
            "created_at": self.created_at
        }

    @staticmethod
    def get_vendor_goals(id_goal):
        goals = Goals.query.filter_by(id_goal=id_goal).all()  # Filtrar los goals por el código del vendedor
        goals_list = [goal.to_json() for goal in goals]  # Convertir los goals a una lista de diccionarios JSON
        return goals_list

    def save(self):
        """
        The save function is a method that is called on an instance of the User class. 
        It adds the instance to the database and commits the changes
        """
        db.session.add(self)
        db.session.commit()

    def destroy(self):
        self.role = None
        self.route = None
        db.session.delete(self)
        db.session.commit()      