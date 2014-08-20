# -*- coding: utf-8 -*-
# all the imports

from flask import request, redirect, url_for,\
	render_template
from apps import app
from database import Database

dataStorage = Database()

@app.route('/', methods=['GET', 'POST'])
def show_entries():
	entries = dataStorage.out()
	return render_template('show_entries.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
	storage={}
	storage['num'] = dataStorage.num
	storage['count'] = 0
	storage['title'] = request.form['title']
	storage['contents'] = request.form['contents']
	
	dataStorage.put(storage)
	dataStorage.num += 1
	return redirect(url_for('show_entries'))

@app.route('/del/<idx>',methods=['GET'])
def del_entry(idx):
	for data in dataStorage.database:
		if int(idx) == data['num']:
			dataStorage.database.remove(data)
			break
	return redirect(url_for('show_entries'))

@app.route('/plus/<idx>',methods=['GET'])
def plus_entry(idx):
	for data in dataStorage.database:
		if int(idx) == data['num']:
			data['count'] += 1
			break
	dataStorage.database = sorted(dataStorage.database, \
		key = lambda list: list['count'], reverse = True)

	return redirect(url_for('show_entries'))

@app.route('/minus/<idx>',methods=['GET'])
def minus_entry(idx):
	for data in dataStorage.database:
		if int(idx) == data['num']:
			if data['count'] == 0:
				data['count'] = 0
			else:
				data['count'] -= 1
			break

	dataStorage.database = sorted(dataStorage.database, \
		key = lambda list: list['count'], reverse = True)

	return redirect(url_for('show_entries'))

@app.route('/reverse',methods=['GET'])
def reverse_entry():
	dataStorage.database = sorted(dataStorage.database, \
		key = lambda list: list['count'], reverse = True)

	return redirect(url_for('show_entries'))

@app.route('/verse',methods=['GET'])
def verse_entry():
	dataStorage.database = sorted(dataStorage.database, key = lambda list: list['count'])
	return redirect(url_for('show_entries'))

@app.route('/comment/like/<int:id>', methods=['GET', 'POST'])
def comment_count(id):
	comment = Comment.query.get(id)
	comment.count += 1

	db.session.commit()

	id = comment.article_id

	return redirect(url_for('article_detail', id=id))
