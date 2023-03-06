from . import bp as api_bp
from app.blueprints.user.models import Post,User


@api_bp.get('/posts')
def api_posts():
    result= []
    posts = Post.query.all()
    for post in posts:
        result.append({
            'id':post.id,
            'body':post.body,
            'timestamp':post.timestamp,
            'user_id':post.user_id
        })
    return result

@api_bp.route('/post/<id>', methods=['GET'])
def api_post(id):
    post = Post.query.get(int(id))
    return {
            'id':post.id,
            'body':post.body,
            'timestamp':post.timestamp,
            'user_id':post.user_id
        }

@api_bp.get('/user_posts/<username>')
def api_user_posts(username):
    result= []
    user = User.query.filter_by(username=username).first()
    for post in user.posts:
        result.append({
            'id':post.id,
            'body':post.body,
            'timestamp':post.timestamp,
            'user_id':post.user_id
        })
    return result