from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from .forms import SMSForm
from ..services.sms_service import SMSService

api_bp = Blueprint('api', __name__)

@api_bp.route('/send', methods=['POST'])
@login_required
def api_send_sms():
    data = request.get_json()
    form = SMSForm(data=data)
    if not form.validate():
        return jsonify({'error': 'invalid data', 'messages': form.errors}), 400
    service = SMSService()
    try:
        sid = service.send(form.to_number.data, form.message.data)
        return jsonify({'status': 'sent', 'sid': sid}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500