from . import bp as user_bp
from .models import User, Post
from app.forms import PostForm
from flask import redirect, render_template
from flask_login import login_required, current_user

@user_bp.route('/post', methods=['GET', 'POST'])
@login_required
def post():
    post = PostForm()
    if post.validate_on_submit():
        title = post.title.data
        body = post.body.data
        user_id = current_user.id
        p = Post(title= title,body=body,user_id=user_id)
        p.commit()
        return redirect('/user/post')
    return render_template('post.jinja', form=post)

@user_bp.route('/user/<username>')
def user(username):
    user_match = User.query.filter_by(username=username).first()
    if not user_match:
        redirect('/')
    posts = user_match.posts
    return render_template('trainer.jinja', user=user_match, posts=posts)