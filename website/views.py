from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import User, Note, db
import json

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

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            return jsonify({})

@views.route('/delete-user', methods=['POST'])
@login_required
def delete_user():
    data = request.get_json()
    userId = data.get('userId') 
    if userId is not None:
        user_to_delete = User.query.filter_by(id=userId).first()
        if current_user.is_superuser:
            db.session.delete(user_to_delete)
            db.session.commit()
            return jsonify({'message': 'Usuário excluído com sucesso'})
    
    return jsonify({'error': 'Erro ao excluir o usuário'}), 400
