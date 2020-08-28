## To run the app in debug mode

### `python3 run.py` or `export FLASK_APP=run.py` and `export FLASK_DEBUG=1` (or on windows `set FLASK_app=run.py` and `set FLASK_DEBUG=1`) then `flask run`

## to set up db: 
### `in terminal run python3`
### `from flaskblog import db`
### `db.create_all()`

## to add data to db:
### `from flaskblog.models import User, Post`
### `user_1 (user_2, user_3 etc) = User(username='<username>', email='<email>', password='<password>')`
### `db.session.add(user_1)`
### `db.session.commit()`
### `post_1 = Post(title='Post 1', content='Post 1 content', user_id=user.id)'
### `db.session.add(post_1)`
### `db.session.commit()`
### to delete records from table
### db.session.query(Model).delete()
### db.session.query(Model).filter(Model.property==123).delete()

### To vaidate User: `User.query.all() or User.query.first() or User.query.filter_by(username='<username>').all()`
### To validate Posts: `### `user = User.query.filter_by(username='<username>').all()` then `user.posts` or `post = Post.query.first()` then `post.user_id` or `post.author`

### to drop db: `db.drop_all()`


