from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.models import FinancialData
from app.extensions import db
from datetime import datetime

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/data', methods=['POST'])
@jwt_required()
def add_financial_data():
    data = request.get_json()
    new_entry = FinancialData(
        date=datetime.strptime(data['date'], '%Y-%m-%d').date(),  # Parse date string
        currency=data['currency'],
        exchange_rate=data['exchange_rate'],
        stock_symbol=data.get('stock_symbol'),
        stock_price=data.get('stock_price')
    )
    db.session.add(new_entry)
    db.session.commit()
    return jsonify({'message': 'Financial data added successfully'}), 201

@api_blueprint.route('/data', methods=['GET'])
@jwt_required()
def get_all_data():
    records = FinancialData.query.all()
    output = [{'id': r.id, 'date': r.date, 'currency': r.currency, 'exchange_rate': r.exchange_rate,
               'stock_symbol': r.stock_symbol, 'stock_price': r.stock_price} for r in records]
    return jsonify(output)
