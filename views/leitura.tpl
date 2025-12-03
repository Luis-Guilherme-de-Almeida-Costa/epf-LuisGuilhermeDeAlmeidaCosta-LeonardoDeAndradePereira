% include('includes/headerNaoLogado.tpl')
<link rel="stylesheet" href="/static/css/styleGeneral.css">
<link rel="stylesheet" href="/static/css/styleLeitura.css">
<link rel="stylesheet" href="/static/css/sobraBackground.css">
% include('includes/nav.tpl')

<div class="container">
  <div class="capa">
      <img src="/{{ filmes['capa_path'] }}" alt="">
  </div>

  <h1>{{ filmes['titulo'] }}</h1>

  <p>
    {{ filmes['sinopse'] }}
  </p>

  <div class="tags">
    % for i in filmes['categoria'].split(','):
        <span class="tag">{{ i.strip() }}</span>
    % end
  </div>

  <div class="buttons">
    <a href="/home/video/{{ filmes['id_filmes'] }}">
      <button type="submit">Visualizar</button>
    </a>
  </div>
</div>


<div class="container-none">
  <img src="/{{ filmes['capa_path'] }}" class="capa-img" alt="">

  <div class="container-content">
    <div class="capa-none">
      <h1 class="titulo-none">{{ filmes['titulo'] }}</h1>
    </div>

    <p>
      {{ filmes['sinopse'] }}
    </p>

    <div class="tags">
    % for i in filmes['categoria'].split(','):
        <span class="tag">{{ i.strip() }}</span>
    % end
    </div>

    <div class="buttons">
      <a href="/home/video/{{ filmes['id_filmes'] }}">
        <button type="submit">Visualizar</button>
      </a>
    </div>
  </div>
</div>
