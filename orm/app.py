from flask import Flask, request, jsonify
from models import db, User, Post

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    print(data)
    new_user = User(username=data['username'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'id': new_user.id, 'username': new_user.username}), 201

@app.route('/posts', methods=['POST'])
def create_post():
    data = request.json
    new_post = Post(title=data['title'], content=data['content'], user_id=data['user_id'])
    db.session.add(new_post)
    db.session.commit()
    return jsonify({'id': new_post.id, 'title': new_post.title}), 201

@app.route('/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    return jsonify([{'id': post.id,
                     'title': post.title,
                     'content': post.content,
                     'user_id': post.user_id} for post in posts])

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)