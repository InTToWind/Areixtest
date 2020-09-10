import os
from flask import Flask, jsonify, abort, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource

records = []
count = [0]
categories = ['Financials','Leisure','Others','Home']

app = Flask(__name__)


def by_created_at(t):
    return t['created_at']

def by_amount(t):
    return t['amount']

def check_amount(amount):
    try:
        float(amount)
        pass
    except ValueError:
        return False
    if float(amount) > 0:
        return True
    return False

@app.route('/api/expense', methods = ['POST'])
def create_expense():
    if not request.form or not 'name' in request.form:
        return {'error': True, 'msg': '404 NOT FOUND'}

    name = request.form['name']
    amount = request.form['amount']
    category = request.form['category']
    created_at = request.form['created_at']

    if not (check_amount(amount) & (category in categories)):
        return {'error': True, 'msg': 'Invalid Input'}

    count[0] += 1
    record = {
        'record_id': count[0],
        'name': name,
        'amount': float(amount),
        'category': category,
        'created_at': created_at
    }
    records.append(record)
    return {'data': record, "error": False, "success": True, "msg": 'successfully created an expense'}


@app.route('/api/expenses/page=<int:page>&per_page=<int:per_page>', methods = ['GET'])
def get_list(page, per_page):
    total_records = len(records)
    first = (page - 1) * per_page
    last = min(page * per_page, total_records)
    if ((page < 1) | (per_page < 1) | (first > total_records - 1)):
        return {'error': True, 'msg': '404 NOT FOUND'}
    return {'data': records[first:last], 'error': False, 'success': 'True', 'msg': 'successfully got detailed expenses records'}


@app.route('/api/expense/<int:record_id>', methods = ['GET'])
def get_id(record_id):
    for record in records:
        if record['record_id'] == record_id:
            return {'data': record, 'error': False, 'success': True, 'msg': 'successfully got detailed record'}
    return {'error': True, 'msg': '404 NOT FOUND'}


@app.route('/api/expense/<int:record_id>', methods = ['POST'])
def edit_record(record_id):
    name = request.form['name']
    amount = request.form['amount']
    category = request.form['category']
    created_at = request.form['created_at']

    if not (check_amount(amount) & (category in categories)):
        return {'error': True, 'msg': 'Invalid Input'}

    for record in records:
        if record['record_id'] == record_id:
            record['name'] = name
            record['amount'] = float(amount)
            record['category'] = category
            record['created_at'] = created_at
            return {'data': None, 'error': False, 'success': True, 'msg': 'successfully updated record'}
    return {'error': True, 'msg': '404 NOT FOUND'}


@app.route('/api/expense/<int:record_id>', methods = ['DELETE'])
def delete_id(record_id):
    for record in records:
        if record['record_id'] == record_id:
            records.remove(record)
            return {'data': None, 'error': False, 'success': True, 'msg': 'successfully deleted record'}
    return {'error': True, 'msg': '404 NOT FOUND'}


@app.route('/api/expense/category=<category>', methods = ['GET'])
def filter_by_category(category):
    if not (category in categories):
        return {'error': True, 'msg': 'no such category'}
    current_records = []
    for record in records:
        if record['category'] == category:
            current_records.append(record)
    return {'data': current_records, 'category': category, 'error': False, 'success': True, 'msg': 'successfully filtered by ' + category}


@app.route('/api/expense/year=<int:year>&month=<int:month>', methods = ['GET'])
def filter_by_month(year, month):
    if month < 10:
        date = str(year) + '-0' + str(month)
    else:
        date = str(year) + '-' + str(month)
    current_records = []
    for record in records:
        if record['created_at'][0:7] == date:
            current_records.append(record)
    if len(current_records) == 0:
        return {'error': False, 'msg': 'no records found'}
    return {'data': current_records, 'month': date, 'error': False, 'success': True, 'msg': 'successfully filtered by ' + date}


@app.route('/api/expense/sort_by_created_at', methods = ['GET'])
def sort_by_created_at():
    if len(records) == 0:
        return {'error': False, 'msg': 'no records found'}
    current_records = list(records)
    current_records = sorted(current_records, key = by_created_at)
    return {'data': current_records, 'error': False, 'success': True, 'msg': 'successfully sorted by created_at'}


@app.route('/api/expense/sort_by_amount', methods = ['GET'])
def sort_by_amount():
    if len(records) == 0:
        return {'error': False, 'msg': 'no records found'}
    current_records = list(records)
    current_records = sorted(current_records, key = by_amount)
    return {'data': current_records, 'error': False, 'success': True, 'msg': 'successfully sorted by amount'}


@app.route('/api/expense/analysis', methods = ['GET'])
def analyze():
    if len(records) == 0:
        return {'error': False, 'msg': 'no records found'}
    sum_amount = 0
    max_amount = 0
    for record in records:
        sum_amount += record['amount']
        max_amount = max(max_amount, record['amount'])
    mean_amount = sum_amount / len(records)
    result = {
        'sum_amount': sum_amount,
        'max_amount': max_amount,
        'mean_amount': mean_amount
    }
    return {'data': result, 'error': False, 'success': True, 'msg': 'successfully analyze the records'}





@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
