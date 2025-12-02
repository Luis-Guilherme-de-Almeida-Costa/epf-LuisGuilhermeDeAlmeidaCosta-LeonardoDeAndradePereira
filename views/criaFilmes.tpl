% include('includes/headerNaoLogado') 
<link rel="stylesheet" href="/static/css/styleGeneral.css">
<link rel="stylesheet" href="/static/css/infoUsuario.css">
<link rel="stylesheet" href="/static/css/sobraBackground.css">
% include('includes/nav') 
    <section class="containerIU container" style="margin-top: 40px";>   
        <div class="titulo-IU">
            <h1>Criação dos <blue>Filmes</blue></h1>
        </div>
        <form class="container-IU" action="{{action}}" method="POST">
            <label for="titulo"><h2>Título do Filme:</h2></label>
            <input type="text" class="inputs-IU" name="titulo" placeholder="Digite o título do filme" required>

            <label for="categoria"><h2>Categoria:</h2></label>
            <select class="inputs-IU" name="categoria" required style="height: 50px; margin-bottom: 20px;">
                <option value="" disabled selected>Selecione uma categoria</option>
                <option value="Acao">Ação</option>
                <option value="Aventura">Aventura</option>
                <option value="Comedia">Comédia</option>
                <option value="Drama">Drama</option>
                <option value="Terror">Terror</option>
                <option value="FiccaoCientifica">Ficção Científica</option>
                <option value="Documentario">Documentário</option>
                <option value="Animacao">Animação</option>
            </select>

            <label for="categoria"><h2>Diretor:</h2></label>
            <input type="text" class="inputs-IU" name="categoria" placeholder="Digite o nome do diretor" required>

            <label for="data_exibicao"><h2>Data e Horário de Exibição:</h2></label>
            <input type="datetime-local" class="inputs-IU" name="data_exibicao">
            <p style="margin: 0px">Caso nenhum horário seja selecionado o filme será anunciado imediatamente!</p>

            <label for="capa"><h2 style="margin-bottom: 0px">Capa do Filme (JPG/PNG):</h2></label>
            <p style="margin-bottom: 10px; margin-top: 3px">O tamanho deve ser !</p>
            <div class="file-upload-wrapper">
                <input type="file" class="inputs-IU file-input" name="capa" id="input-capa" accept="image/jpeg, image/png" required">
                
                <span class="file-upload-filename">Nenhum arquivo selecionado</span>
                
                <span class="file-upload-button">Escolher Arquivo</span>
            </div>

            <label for="arquivo_video"><h2>Arquivo do Filme (MP4):</h2></label>
            <div class="file-upload-wrapper">
                <input type="file" class="inputs-IU file-input" name="arquivo_video" id="input-video" accept="video/mp4" required">
                
                <span class="file-upload-filename">Nenhum arquivo selecionado</span>
                <span class="file-upload-button">Escolher Arquivo</span>
            </div>

            % include('includes/messagesError') 
            % include('includes/messagesSuccess') 

            <button type="submit" class="botao" style="margin-bottom: 50px;">Criar</button>
        </form>
    </section>
% include('includes/footerSemContato')