from bottle import request

class FlashManager:   
    def __init__(self):
        self._session = request.environ.get('beaker.session')

    def get_flash_messages(self):
        session = request.environ.get('beaker.session')

        errors = session.pop('flash_errors', [])
        success_message = session.pop('flash_success', None)

        form_data = session.pop('form_data', {})

        session.save()
        
        return errors, success_message, form_data
        
    def set_flash_errors_and_data(self, errors, data):
        session = request.environ.get('beaker.session')
        session['flash_errors'] = errors
        session['form_data'] = data
        session.save()

    def set_flash_success(self, message):
        session = request.environ.get('beaker.session')
        session['flash_success'] = message
        session.save()