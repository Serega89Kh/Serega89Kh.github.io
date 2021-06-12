from flask import abort, render_template, request, redirect, url_for
from app import app
from models import Blog

@app.route('/', methods=['GET', 'POST'])
def homepage():
    blogs = Blog.select()
    if request.method == 'POST':
        if request.form.get('content'):
            blog = Blog.create(content=request.form['content'])
            return render_template('homepage.html', blogs=blogs)
    return render_template('homepage.html', blogs=blogs)

@app.route('/delete/<int:pk>/', methods=['POST', 'GET'])
def delete_note(pk):
    blog = Blog.get(blog.id == pk)
    blog.delete_instance()
    blog.save()
    return redirect(url_for('homepage'))


@app.route('/update/<int:pk>/', methods=['POST', 'GET'])
def update_note(pk):
    if request.method == 'POST':
        if request.form.get('updated_parts'):
            blog = Blog.get(Blog.id == pk)
            query = Blog.update(content=request.form['updated_parts']).where(Blog.id==pk)
            query.execute()
            return redirect(url_for('homepage'))
    return render_template('update.html', blog=blog)

