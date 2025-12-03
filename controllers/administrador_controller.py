from bottle import Bottle, request, redirect # Importar 'redirect'
from .base_controller import BaseController
from services.pessoas_service import PessoasService
from services.administrador_service import AdministradorService
from utils.flash import FlashManager
from utils.verificarAdm import VerificarAdm

class AdministradorController(BaseController):
    def __init__(self, app):
        super().__init__(app)

        self.setup_routes()
        self.administrador_service = AdministradorService()
        self.pessoas_service = PessoasService()
        self.verificar_adm = VerificarAdm()

    def setup_routes(self):
        self.app.route('/adm/index', method=['GET'], callback=self.show_administrador)
        self.app.route('/adm/store/<id_pessoa>', method=['POST'], callback=self.add_administrador)


    def show_administrador(self, db):
        flash = FlashManager()

        session = request.environ.get('beaker.session')

        id_pessoa_adm = session.get('user_id')

        user = self.pessoas_service.get_by_id(db, id_pessoa_adm)

        pessoa = self.pessoas_service.get_all(db)

        adm = self.verificar_adm.verificarAdm(db, id_pessoa_adm)

        usuariosAdm = self.administrador_service.get_all(db)

        if not adm:
            return redirect("/home")
    
        errors, success_message, form_data = flash.get_flash_messages()

        return self.render(
            'cadastroAdm', 
            action="/adm/index", 
            path="logado", 
            pathStatus='L', 
            user=user, 
            pessoas=pessoa,
            adm=adm,
            adm_list=usuariosAdm,
            errors=errors,
            success=success_message
        )

    def add_administrador(self, db, id_pessoa):
        flash = FlashManager()

        result = self.administrador_service.save(db, id_pessoa)
        
        if result['success']:
            flash.set_flash_success(["Usuário promovido com sucesso!"])
            return redirect('/adm/index')
        else:
            errors = result.get("errors", {"geral": "Erro ao atualizar usuário."})
            flash.set_flash_errors_and_data(errors, {})
            return redirect('/home')