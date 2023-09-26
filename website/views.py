from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import User, Note, db

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash("Note it's too short!", category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash("Note added!", category='success')

    return render_template("home.html", user=current_user)

@views.route('/note/<int:note_id>', methods=['DELETE'])
@login_required
def delete_note(note_id):
    note = Note.query.get(note_id)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            return jsonify({})
    
    return jsonify({'error': 'Error deleting note'}), 400

@views.route('/user/<int:user_id>', methods=['DELETE'])
@login_required
def delete_user(user_id):
    user_to_delete = User.query.get(user_id)
    if user_to_delete is not None and current_user.is_superuser:
        db.session.delete(user_to_delete)
        db.session.commit()
        return jsonify({'message': 'User deleted!'})
    
    return jsonify({'error': 'Error deleting user'}), 400
