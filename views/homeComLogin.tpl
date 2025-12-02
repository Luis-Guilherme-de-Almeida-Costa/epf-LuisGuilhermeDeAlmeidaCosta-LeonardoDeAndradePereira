% include('includes/headerNaoLogado.tpl')
<link rel="stylesheet" href="/static/css/styleGeneral.css">
<link rel="stylesheet" href="/static/css/styleLogado.css">
<link rel="stylesheet" href="/static/css/stylesFooter.css">
% include('includes/nav.tpl')

<section class="container">
    <div id="container-home"> 
        <div id="home">
            <h1><blue>Aproveite</blue> seu lugar <br/><blue>Ideal</blue></h1>

            <form action="/home/search" id="form-search" method="GET">
                <div class="barra-pesquisa">
                    <input type="text" name="searchData" placeholder="Pesquise aqui..." />
                    <button type="submit">
                        <i class="fa fa-search"></i>
                    </button>
                </div>
            </form>
        </div>
    </div>    
</section>

<section class="catalogo-container" id="catalogo">
    <div class="barra-pesquisa-container">
        <form action="/home/search" id="form-search" method="GET">
            <div class="barra-pesquisa">
                <input type="text" name="searchData" placeholder="Pesquise aqui..." />
                <button type="submit">
                    <i class="fa fa-search"></i>
                </button>
            </div>
        </form>
    </div>

    <!-- PRINCIPAIS -->
    <div class="secao-catalogo">
        <h1>Principais</h1>
        <div class="scroll-horizontal">

            % if filmes and len(filmes) > 0:
                % for filme in filmes:
                    <a href="/home/leitura/{{ filme['id_filmes'] }}" class="link">
                        <div class="item-catalogo">
                            <div class="imagem">
                                <img src="{{filme['capa_path']}}" alt="Capa do filme" />
                            </div>
                            <h2>{{filme['titulo']}}</h2>
                        </div>
                    </a>
                % end
            % else:
                <p>Nenhum filme encontrado.</p>
            % end

        </div>
    </div>

    <!-- AÇÃO -->
    <div class="secao-catalogo">
        <h1>Ação</h1>
        <div class="scroll-horizontal">

            % if acao and len(acao) > 0:
                % for filme in acao:
                    <a href="/home/leitura/{{ filme['id_filmes'] }}" class="link">
                        <div class="item-catalogo">
                            <div class="imagem">
                                <img src="{{filme['capa_path']}}" alt="Capa do filme" />
                            </div>
                            <h2>{{filme['titulo']}}</h2>
                        </div>
                    </a>
                % end
            % else:
                <p>Nenhum filme encontrado.</p>
            % end

        </div>
    </div>
</section>

% include('includes/footerComContato.tpl')