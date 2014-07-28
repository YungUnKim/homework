from flask import render_template, Flask, request, url_for
from apps import app

from google.appengine.ext import db

class Photo(db.Model):
	text = db.StringProperty()


@app.route('/')
@app.route('/index')
def index():
	return render_template("upload.html", all_list=Photo.all())



@app.route('/upload', methods=['POST'])
def upload_db():
	post_data = request.files['text']
	
	upload_data = Photo()
	upload_data.text = request.form['text']
	upload_data.put()

	comment = "uploaded!"

	return render_template("upload.html", comment=comment, all_list=Photo.all())
