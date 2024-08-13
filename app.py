from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)  # Permite requisições CORS de qualquer origem

def init_db():
    with sqlite3.connect('sales.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sales (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                seller TEXT,
                product TEXT,
                quantity INTEGER,
                price REAL
            )
        ''')
        conn.commit()

@app.route('/register_sale', methods=['POST'])
def register_sale():
    data = request.json
    with sqlite3.connect('sales.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO sales (seller, product, quantity, price) 
            VALUES (?, ?, ?, ?)
        ''', (data['seller'], data['product'], data['quantity'], data['price']))
        conn.commit()
    return jsonify({'message': 'Venda registrada com sucesso!'})

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', debug=True, port=5000)
