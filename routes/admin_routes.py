import os
from flask import Blueprint, render_template, request, redirect, url_for, session
from models.db_models import Skill
from models.database import db
from werkzeug.utils import secure_filename


admin_bp = Blueprint("admin", __name__)

admin_username = 'admin'
admin_password = 'password'

@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'password':
            session['logged_in'] = True
            return redirect(url_for('admin.dashboard'))
        else:
            return "Wrong username and/or password"
    return render_template('admin/admin_login.html')

@admin_bp.route('/dashboard')
def dashboard():
    if not session.get('logged_in'):
        return redirect(url_for('admin.login'))
    return render_template('admin/admin_dashboard.html')

@admin_bp.route('/skills', methods=['GET', 'POST'])
def manage_skills():
    if request.method == 'POST':
        new_skill_name = request.form['skill_name']
    existing_skills = Skill.query.all()
    return render_template('admin/manage_skills.html', skills=existing_skills)

@admin_bp.route('/add_skill', methods=['POST'])
def add_skill():
    new_skill_name = request.form['skill_name']
    new_description = request.form['description_for_skill']
    new_skill = Skill(name=new_skill_name, level=1, description = new_description)
    db.session.add(new_skill)
    db.session.commit()
    return redirect(url_for('admin.manage_skills'))

@admin_bp.route('/delete_skill/<int:skill_id>', methods=['POST'])
def remove_skill(skill_id):
    skill_to_remove = Skill.query.get(skill_id)
    if skill_to_remove:
        db.session.delete(skill_to_remove)
        db.session.commit()
        return redirect(url_for('admin.manage_skills'))
    else:
        return "Skill not found", 404
    
@admin_bp.route('/edit_skill/<int:skill_id>', methods=['GET'])
def show_edit_skill_form(skill_id):
    skill_to_edit = Skill.query.get(skill_id)
    if skill_to_edit:
        return render_template('admin/edit_skill.html', skill=skill_to_edit)
    else:
        return "Skill not found", 404
    
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@admin_bp.route('edit_skill/<int:skill_id>', methods=['POST'])
def edit_skill(skill_id):
    skill_to_edit = Skill.query.get(skill_id)
    if skill_to_edit:
        new_name = request.form.get('new_name')
        new_description = request.form.get('new_description')
        if new_name:
            skill_to_edit.name = new_name
        if new_description:
            skill_to_edit.description = new_description
        image = request.files['image']
        if image:
            filename = secure_filename(image.filename)
            skill_image = os.path.join('./upload_folder_for_images', filename)
            image.save(skill_image)
            skill_to_edit.skill_image = skill_image
        db.session.commit()
        return redirect(url_for('admin.manage_skills'))
    else:
        return "Skill not found", 404
