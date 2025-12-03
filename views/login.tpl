% include('includes/headerNaoLogado.tpl')
<link rel="stylesheet" href="/static/css/styleGeneral.css">
<link rel="stylesheet" href="/static/css/styleAutenticacao.css">
<link rel="stylesheet" href="/static/css/sobraBackground.css">
<link rel="stylesheet" href="/static/css/styleNaoLogado.css">
<link rel="stylesheet" href="/static/css/stylesFooter.css">
% include('includes/nav.tpl')

<section class="container">
    <div class="titulo-autenticacao">
        <h1><blue>LOGIN</blue></h1>
    </div>

    <form class="container-login" id="formLogin" action="{{action}}" method="POST">
        
        <label for="emailInput" class="titulo-inputs">Email</label>
        <input type="email" class="inputs" id="emailInput" name="email" value="{{ data.get('email', '') if data else '' }}" required>

        <label for="senhaInput" class="titulo-inputs">Senha</label>
        <input type="password" class="inputs" id="senhaInput" name="senha" required>

        % include('includes/messagesError.tpl')

        <button type="submit" class="botao" id="loginBtn">Entrar</button>

        <p style="margin-top: 10px; margin-bottom: 0px;">Ainda não possui uma conta?</p>
        <a href="/pessoas/add" class="link"
           style="text-align: center; text-decoration: underline; font-size: 14px;">
           Cadastre-se
        </a>

        <p>© 2025 - C&M</p>
    </form>
</section>

% include('includes/footerSemContato.tpl')
