from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from .forms import SMSForm
from ..services.sms_service import SMSService
from ..models import SMSLog

sms_bp = Blueprint('sms', __name__, template_folder='templates')

@sms_bp.route('/')
@login_required
def dashboard():
    logs = current_user.sms_logs.order_by(SMSLog.timestamp.desc()).limit(20).all()
    return render_template('dashboard.html', logs=logs)

@sms_bp.route('/send', methods=['GET', 'POST'])
@login_required
def send_sms():
    form = SMSForm()
    if form.validate_on_submit():
        service = SMSService()
        try:
            sid = service.send(form.to_number.data, form.message.data)
            flash(f'SMS envoyé! SID: {sid}')
            return redirect(url_for('sms.dashboard'))
        except Exception as e:
            flash(f'Erreur lors de l’envoi: {str(e)}')
    return render_template('send_sms.html', form=form)