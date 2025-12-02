% include('includes/headerNaoLogado.tpl')
<link rel="stylesheet" href="/static/css/styleGeneral.css">
<link rel="stylesheet" href="/static/css/infoUsuario.css">
% include('includes/nav.tpl')

<section class="containerIU">
    <div class="titulo-IU">
        <h1>OLÁ, <blue>{{ user['nome'] }}!</blue></h1>
    </div>

    <form class="container-IU" id="formCadastro" action="{{action}}" method="POST">

        <label for="nomeInput" class="titulo-inputs">Nome</label>
        <input type="text" class="inputs-IU" id="nomeInput" name="nome" value="{{ user['nome'] }}">

        <label for="cpfInput" class="titulo-inputs">CPF</label>
        <input type="text" class="inputs-IU" id="cpfInput" name="cpf" value="{{ user['cpf'] }}">

        <label for="emailInput" class="titulo-inputs">Email</label>
        <input type="email" class="inputs-IU" id="emailInput" name="email" value="{{ user['email'] }}">

        % include('includes/messagesError.tpl')
        % include('includes/messagesSuccess.tpl')

        <button type="submit" class="botao">SALVAR</button>
    </form>
</section>

% include('includes/footerSemContato.tpl')
