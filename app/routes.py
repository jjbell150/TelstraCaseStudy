from app import app
from flask import render_template, redirect, url_for
from werkzeug.contrib.cache import SimpleCache
from .forms import StoreDocumentForm
documents = SimpleCache()

@app.route('/')
@app.route('/index')
def index():
	store_form = StoreDocumentForm()
	return render_template('store_document.html', store_form=store_form)
	
@app.route('/messages', methods=["POST"])
def store_document():
	success = False
	store_form = StoreDocumentForm()
	if store_form.validate_on_submit():
			value = documents.get(store_form.id.data)
			if value is None:
				success = documents.set(str(store_form.id.data), store_form.text.data, timeout=int(store_form.ttl.data))	
	return render_template('store_document.html', store_form=store_form,store_success=success)

@app.route('/messages/<id>', methods=["GET"])
def get_document(id):
	value = documents.get(id)
	if value is not None:
		return render_template('view_document.html',id=id,text=value)
	return render_template('view_document.html')
	
@app.route('/clear')
def clear_cache():
	success = documents.clear()
	return render_template('clear_cache.html',success=success)
