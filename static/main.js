document.addEventListener('DOMContentLoaded', function() {
    console.log('Página carregada no navegador!')
    
    // 1. Efeito de fade-in ao carregar a página
    document.body.style.opacity = '0';
    setTimeout(() => {
        document.body.style.transition = 'opacity 0.5s ease-in-out';
        document.body.style.opacity = '1';
    }, 100);

});

import './modules/nav.js';
/*
import 'core-js/stable';
import 'regenerator-runtime/runtime';

const path = window.location.pathname;

import './assets/css/styleGeneral.css';
import './modules/nav';

if (path === '/') {
  import('./assets/css/styleNaoLogado.css').then(() => console.log("O.O"))
  import('./assets/css/stylesFooter.css').then(() => console.log("O.O"))
}

if (path === '/home') {
  import('./assets/css/styleLogado.css').then(() => console.log("O.O"))
  import('./assets/css/stylesFooter.css').then(() => console.log("O.O"))
}

if (path.includes('/register') || path.includes('/login')) {
  import('./assets/css/styleAutenticacao.css')
    .then(() => console.log("o.o"));
  import('./assets/css/sobraBackground.css').then(() => console.log("O.O"));
}

if (path === '/perfil/index' || path === "/perfil/logado"){
  import ('./assets/css/infoUsuario.css').then(() => console.log("O.O"));
}

if (path === '/pagamento/index' || path === '/pagamento/autor') {
  import('./assets/css/pagamento.css').then(() => console.log("O.O"))
}

if(path === '/pagamento/cartao/leitor/index' || path === '/pagamento/boleto/leitor/index' || path === '/pagamento/pix/leitor/index') {
  import('./assets/css/infoUsuario.css').then(() => console.log("O.O"))
  import('./assets/css/sobraBackground.css').then(() => console.log("O.O"))
}


if(path === '/pagamento/cartao/autor/index' || path === '/pagamento/boleto/autor/index' || path === '/pagamento/pix/autor/index') {
  import('./assets/css/infoUsuario.css').then(() => console.log("O.O"))
  import('./assets/css/sobraBackground.css').then(() => console.log("O.O"))
}

if(path === '/pagamento/pix/leitor/index' || path === '/pagamento/pix/autor/index' || path === '/perfil/index' || path === '/login/esqueci/index' || path === "/perfil/logado") {
  import('./assets/css/sobraBackground.css').then(() => console.log("O.O"))
}

if(path.includes('/home/search')) {
  import('./assets/css/styleSearch.css').then(() => console.log("O.O"))
  import('./assets/css/sobraBackground.css').then(() => console.log("O.O"))
}

if(path.includes('/home/leitura/')) {
  import('./assets/css/styleLeitura.css').then(() => console.log("O.O"))
  import('./assets/css/sobraBackground.css').then(() => console.log("O.O"))
}

if(path.includes('/home/leitura/title/')) {
  import('./assets/css/sobraBackground.css').then(() => console.log("O.O"))
}
*/