from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

#from datacreate import BlogPost
from db_setup import init_db
init_db() # added other datacreate & db_setup for db creation

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)

# datacreate class is replaced

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/posts', methods=['GET', 'POST'])
def posts():
    from datacreate import BlogPost

    if request.method == 'POST':
        post_title = request.form['title']
        post_content = request.form['content']
        post_author = request.form['author']
        new_post = BlogPost(title=post_title, content=post_content, author=post_author)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/posts')
    else:
        all_posts = BlogPost.query.order_by(BlogPost.date_posted).all()
        return render_template('posts.html', posts=all_posts)

@app.route('/posts/delete/<int:id>')
def delete(id):
    from datacreate import BlogPost

    post = BlogPost.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect('/posts')

@app.route('/posts/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    from datacreate import BlogPost
    post = BlogPost.query.get_or_404(id)

    if request.method == 'POST':
        post.title = request.form['title']
        post.author = request.form['author']
        post.content = request.form['content']
        db.session.commit()
        return redirect('/posts')
    else:
        return render_template('edit.html', post=post)

@app.route('/posts/new', methods=['GET', 'POST'])
def new_post():
    from datacreate import BlogPost
    if request.method == 'POST':
        post.title = request.form['title']
        post.author = request.form['author']
        post.content = request.form['content']
        new_post = BlogPost(title=post.title, content=post.content, author=post.author)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/posts')
    else:
        return render_template('new_post.html')

if __name__ == "__main__":
    app.run(debug=True)
