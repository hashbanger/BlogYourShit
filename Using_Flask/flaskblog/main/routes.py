from flask import render_template, request, Blueprint
from flask.models import Post
main = Blueprint('users', __name__)

@main.route('/')
def home():
    page = request.args.get('page', default = 1, type = int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(per_page = 5)
    return render_template('home.html', posts = posts)

@main.route('/about')
def about():
    return render_template('about.html', title = 'About')