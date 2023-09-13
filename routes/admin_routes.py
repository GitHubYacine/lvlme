from flask import Blueprint, render_template, request, redirect, url_for, session


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
    return render_template('admin_dashboard.html')
