from bottle import route, request, redirect, HTTPResponse, install

class AuthRedirectPlugin:
    def __init__(self):
        self.forbidden_routes = ['/pessoas/add', '/pessoas/login']

    def apply(self, callback, route):
        if route.rule in self.forbidden_routes:
            def wrapper(*args, **kwargs):
                session = request.environ.get('beaker.session')
                
                if session and session.get('logged_in'):
                    print(session.get('user_name'))
                    return redirect('/')
                
                return callback(*args, **kwargs)
            return wrapper
        return callback
    
class LoginRequiredPlugin:
    def __init__(self):
        self.protected_routes = ['/home', '/pessoas/edit', '/filmes/store']

    def apply(self, callback, route):
        if route.rule in self.protected_routes:
            def wrapper(*args, **kwargs):
                session = request.environ.get('beaker.session')
                
                if not session or not session.get('logged_in'):
                    return redirect('/')
                
                return callback(*args, **kwargs)
            return wrapper
        return callback
    
def setup_auth_redirect(app):
    app.install(AuthRedirectPlugin())
    app.install(LoginRequiredPlugin())