% include('includes/headerNaoLogado') 
<link rel="stylesheet" href="/static/css/styleGeneral.css">
<link rel="stylesheet" href="/static/css/infoUsuario.css">
<link rel="stylesheet" href="/static/css/cadastroAdm.css">
<link rel="stylesheet" href="/static/css/sobraBackground.css">
% include('includes/nav') 

<section class="containerIU container"> 
 <div class="titulo-IU" style="flex-direction: column;">
    <h1>Gerenciamento de <blue>Filmes</blue></h1>
    <p>Lista completa de filmes. Use o botão para remover um filme da plataforma.</p>
 </div>
% include('includes/messagesError') 
% include('includes/messagesSuccess') 

 <div class="table-responsive" style="margin-top: 20px; margin-bottom: 50px;">
    <table class="user-table">
        <thead>
            <tr>
                <th style="width: 5%;">ID</th>
                <th style="width: 65%;">Título</th>
                <th style="width: 30%;">Ação</th>
            </tr>
        </thead>
        <tbody>
            % for filme in filmes:
                <tr>
                    <td>{{filme['id_filmes']}}</td>
                    <td>{{filme['titulo']}}</td>
                    <td>
                        <form action="/filmes/remove/{{filme['id_filmes']}}" method="POST" style="margin: 0;">
                            <button type="submit" class="botao-action promote-admin" style="background-color: #dc3545;">
                                Remover Filme
                            </button>
                        </form>
                    </td>
                </tr>
            % end
        </tbody>
    </table>
 </div>
</section>
% include('includes/footerSemContato')