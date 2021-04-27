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
        exists = False
        # check if user exits in database
        # if not create user and add to database
        # create row in Message table with user (created/found) add to tausers =  User.query.all()
        users =User.query.all()
        the_user = None
        for u in users:
            if u.author == form.author:
                exists=true
                the_user=u
                break
        if not exists:
            the_user=User(author=form.author.data)
            db.session.add(the_user)
            db.session.commit()
        print(the_user)
        m=Messages(message=form.message.data,user_id=the_user.id)
        db.session.add(m)
        db.session.commit()
        

    # output all messages
    # create a list of dictionaries with the following structure
    # [{'author':'carlos', 'message':'Yo! Where you at?!'},
    #  {'author':'Jerry', 'message':'Home. You?'}]
    posts = [
    {'author':'carlos','message':'Yo! Where you at?!'},
    {'author':'Jerry','message':'Home. You?'}
    ]
    messages=Messages.query.all()
    messageList = []
    for m in messages:
        print(m)
        user=User.query.filter_by(id=m.user_id).first()
        if (user is None):
            continue
        name=user.author
        messageList.append({'author':name, 'message':m.message})
    return render_template('home.html', posts=messageList, form=form)

