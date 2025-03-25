from app.extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False) 

    def __repr__(self):
        return f"<User {self.username}>"   


class FinancialData(db.Model):
    __tablename__ = 'fin_data'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    currency = db.Column(db.String(10), nullable=False)
    exchange_rate = db.Column(db.Float, nullable=False)
    stock_symbol = db.Column(db.String(10), nullable=True)
    stock_price = db.Column(db.Float, nullable=True)

    def __repr__(self):
        return f"<FinancialData {self.date} - {self.value}>"
    




