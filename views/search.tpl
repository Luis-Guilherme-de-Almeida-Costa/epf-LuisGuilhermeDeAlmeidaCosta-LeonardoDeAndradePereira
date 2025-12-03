% include('includes/headerNaoLogado.tpl')
<link rel="stylesheet" href="/static/css/styleGeneral.css">
<link rel="stylesheet" href="/static/css/sobraBackground.css">
<link rel="stylesheet" href="/static/css/styleSearch.css">
% include('includes/nav.tpl')

<div class="search-bar">
    <form action="/home/search" id="form-search" method="GET">
        <div class="barra-pesquisa">
            <input type="text" name="searchData" placeholder="Pesquise aqui..." />
            <button type="submit">
                <i class="fa fa-search"></i>
            </button>
        </div>
    </form>
</div>

<section class="container">
    <div class="resultado-titulo">Resultados de acordo com sua pesquisa:</div>
    
    <div class="container-livros">

        % if len(filmes) > 0:
            % for filme in filmes:
                <div class="container-scroll">
                    <a href="/home/leitura/{{ filme['id_filmes'] }}" class="link livro-link">
                        <div class="livro">
                            <img src="/{{filme['capa_path']}}" alt="Capa do filme" />
                            <div class="livro-info">
                                <h3>{{ filme['titulo'] }}</h3>
                                <p>{{ filme['sinopse'] }}</p>
                            </div>
                        </div>
                    </a>
                </div>
            % end
        % else:
            <p>Nenhum filme encontrado.</p>
        % end

    </div>
</section>

% include('includes/footerSemContato.tpl')
