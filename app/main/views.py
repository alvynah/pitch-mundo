from flask import render_template
from flask_login import login_required, current_user
from . import main

# Views


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')


@main.route('/create_new', methods=['POST', 'GET'])
@login_required
def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data
        category = form.category.data
        user_id = current_user
        new_pitch_object = Pitch(post=post, user_id=current_user._get_current_object(
        ).id, category=category, title=title)
        new_pitch_object.save_p()
        
        return redirect(url_for('main.index'))

    return render_template('new_pitch.html', form=form)
