from flask import render_template, redirect

from app import db
from app import app
from app.forms import MessageForm
from app.models import User, Messages

# add route '/' and also add the two methods to handle request: 'GET' and 'POST'
@app.route('/', methods=['GET', 'POST'])
def home():
    form=MessageForm()
    if form.validate_on_submit():
        # check if user exits in database
        # if not create user and add to database
        # create row in Message table with user (created/found) add to ta database

	users= User.query.all()
	exists=False
	for u in users:
		if u.author == form.author:
			exists=true
			break
	if exists == False:
		u=User(author=u.author)
		db.session.add(u)
		db.session.commit()


    # output all messages
    # create a list of dictionaries with the following structure
    # [{'author':'carlos', 'message':'Yo! Where you at?!'},
    #  {'author':'Jerry', 'message':'Home. You?'}]
    posts = [
    {'author':'carlos','message':'Yo! Where you at?!'},
    {'author':'Jerry','message':'Home. You?'}
    ]

    return render_template('home.html', posts=posts, form=form)

