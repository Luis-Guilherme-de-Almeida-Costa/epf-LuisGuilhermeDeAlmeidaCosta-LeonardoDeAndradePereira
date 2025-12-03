% include('includes/headerNaoLogado') 
<link rel="stylesheet" href="/static/css/styleGeneral.css">
<link rel="stylesheet" href="/static/css/infoUsuario.css">
<link rel="stylesheet" href="/static/css/cadastroAdm.css">
<link rel="stylesheet" href="/static/css/sobraBackground.css">
% include('includes/nav') 
    <section class="containerIU container"> 
        <div class="titulo-IU" style="flex-direction: column;">
            <h1>Gerenciamento de <blue>Usuários</blue></h1>
            <p>Lista completa de usuários. Use o botão para tornar um usuário um administrador.</p>
        </div>

        % include('includes/messagesError') 
        % include('includes/messagesSuccess') 

        <div class="table-responsive" style="margin-top: 20px; margin-bottom: 50px;">
            <table class="user-table">
                <thead>
                    <tr>
                        <th style="width: 5%;">ID</th>
                        <th style="width: 30%;">Nome</th>
                        <th style="width: 35%;">Email</th>
                        <th style="width: 15%;">Status</th>
                        <th style="width: 15%;">Ação</th>
                    </tr>
                </thead>
                <tbody>
                    % for pessoa in pessoas:
                        % is_admin = False
                        % for i in adm_list:
                        %   if i['id_pessoa'] == pessoa['id_pessoa']:
                        %       is_admin = True
                        %   end
                        % end

                        <tr>
                            <td>{{pessoa['id_pessoa']}}</td>
                            <td>{{pessoa['nome']}}</td>
                            <td>{{pessoa['email']}}</td>
                            
                            % if is_admin:
                                <td class="status-admin">ADMINISTRADOR</td>
                                <td>
                                    <button class="botao-action remove-admin" disabled>
                                        É Admin
                                    </button>
                                </td>
                            % else:
                                <td class="status-user">Usuário Comum</td>
                                <td>
                                    <form action="/adm/store/{{pessoa['id_pessoa']}}" method="POST" style="margin: 0;">
                                        <button type="submit" class="botao-action promote-admin">
                                            Promover a Admin
                                        </button>
                                    </form>
                                </td>
                            % end
                        </tr>
                    % end
                </tbody>
            </table>
        </div>
    </section>
% include('includes/footerSemContato')