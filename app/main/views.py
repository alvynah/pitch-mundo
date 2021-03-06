from flask import render_template, request, redirect, url_for, abort
from flask_login import login_required, current_user
from . import main
from ..models import User,Pitch,Upvote,Downvote,Comment
from .forms import UpdateProfile, PitchForm,CommentForm
from .. import db,photos


# Views


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    pitchesview = Pitch.query.all()
    bus = Pitch.query.filter_by(category='Business').all()
    tech = Pitch.query.filter_by(category='Tech').all()
    event = Pitch.query.filter_by(category='Event').all()

    return render_template('index.html', pitchesview=pitchesview, bus=bus, tech=tech, event=event)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username=uname).first()
    user_id = current_user._get_current_object().id
    pitches = Pitch.query.filter_by(user_id=user_id).all()


    if user is None:
        abort(404)

    return render_template("profile/profile.html", user=user,pitches=pitches,user_id=user_id)


@main.route('/user/<uname>/update', methods=['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname=user.username))

    return render_template('profile/update.html', form=form)


@main.route('/user/<uname>/update/pic', methods=['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username=uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile', uname=uname))


@main.route('/create_new', methods=['POST', 'GET'])
@login_required
def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        title = form.title.data
        pitch = form.pitch.data
        category = form.category.data
        user_id = current_user
        new_pitch_object = Pitch(pitch=pitch, user_id=current_user._get_current_object().id, category=category, title=title)
        new_pitch_object.save_pitch()
        return redirect(url_for('main.index'))

    return render_template('new_pitch.html', form=form)


@main.route('/like/<int:id>', methods=['POST', 'GET'])
@login_required
def like(id):
    pitch = Pitch.query.get(id)
    new_vote_like = Upvote(pitch=pitch, upvote=1)
    new_vote_like.save()
    return redirect(url_for('main.index',id=id))


@main.route('/dislike/<int:id>', methods=['GET', 'POST'])
@login_required
def dislike(id):
    pitch = Pitch.query.get(id)
    new_vote_dislike = Downvote(pitch=pitch, downvote=1)
    new_vote_dislike.save()
    return redirect(url_for('main.index',id=id))


@main.route('/comment/<int:pitch_id>', methods=['POST', 'GET'])
@login_required
def comment(pitch_id):
    form = CommentForm()
    pitch = Pitch.query.get(pitch_id)
    all_comments = Comment.query.filter_by(pitch_id=pitch_id).all()
    if form.validate_on_submit():
        comment = form.comment.data
        pitch_id = pitch_id
        user_id = current_user._get_current_object().id
        new_comment = Comment(comment=comment, user_id=user_id, pitch_id=pitch_id)
        new_comment.save()
        return redirect(url_for('.comment', pitch_id=pitch_id))
    return render_template('comment.html', form=form, pitch=pitch, all_comments=all_comments)
