% include('includes/headerNaoLogado.tpl')
    <link rel="stylesheet" href="/static/css/styleGeneral.css">
    <link rel="stylesheet" href="/static/css/styleAutenticacao.css">
    <link rel="stylesheet" href="/static/css/sobraBackground.css">
    <link rel="stylesheet" href="/static/css/styleNaoLogado.css">
    <link rel="stylesheet" href="/static/css/stylesFooter.css">
% include('includes/nav.tpl')

<section class="container">
    <div class="titulo-autenticacao">
        <h1><blue>CADASTRO</blue></h1>
    </div>
    <form class="container-cadastro" id="formCadastro" action="{{action}}" method="POST">
        
        <label for="nomeInput" class="titulo-inputs">Nome</label>
        <input type="text" class="inputs" id="nomeInput" name="nome" value="{{ data.get('nome', '') if data else '' }}" required>

        <label for="cpfInput" class="titulo-inputs">CPF</label>
        <input type="text" class="inputs" id="cpfInput" name="cpf" value="{{ data.get('cpf', '') if data else '' }}" required>

        <label for="emailInput" class="titulo-inputs">Email</label>
        <input type="email" class="inputs" id="emailInput" name="email" value="{{ data.get('email', '') if data else '' }}" required>

        <label for="senhaInput" class="titulo-inputs">Senha</label>
        <input type="password" class="inputs" id="senhaInput" name="senha" required>

        <label for="confirmarSenhaInput" class="titulo-inputs">Confirmar Senha</label>
        <input type="password" class="inputs" id="confirmarSenhaInput" name="confirmarSenha" required>

        % include('includes/messagesError.tpl')

        <button type="submit" class="botao" id="cadastroBtn">CADASTRAR</button>
        <a class="underline link" style="margin-bottom: 10px;" href="/pessoas/login">Já possuo conta!</a>
    </form>
</section>

% include('includes/footerSemContato.tpl')
