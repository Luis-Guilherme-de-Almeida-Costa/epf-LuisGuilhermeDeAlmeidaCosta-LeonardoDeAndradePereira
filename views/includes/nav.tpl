</head>
<header>
    <a class="logo" href="/">
        <img src="/assets/Images/logo.png" alt="">
    </a>

% if path:
    % if path == "logado":
        <nav>
            <ul class="nav-middle">
                % if pathStatus == "LI":
                    <li><a class="link navStatus" href="/">Home</a></li>
                    <li><a class="link navStatus" href="/">Catálogo</a></li>
                    <li><a class="link navStatus" href="/">Contatos</a></li>
                % elif pathStatus == "L":
                    <li><a class="link navStatus" href="/">Home</a></li>
                    <li><a class="link navStatus" href="#catalogo">Catálogo</a></li>
                    <li><a class="link navStatus" href="#contatos">Contatos</a></li>
                % end
            </ul>
        </nav>
    % end

    % if path == "naoLogado":
        <nav>
            <ul class="nav-middle">
                % if pathStatus == "A":
                    <li><a class="link navStatus" href="/">Home</a></li>
                    <li><a class="link navStatus" href="/">Sobre Nós</a></li>
                    <li><a class="link navStatus" href="/">Preços</a></li>
                    <li><a class="link navStatus" href="/">Contatos</a></li>
                % elif pathStatus == "I":
                    <li><a class="link navStatus" href="/">Home</a></li>
                    <li><a class="link navStatus" href="#sobre-nos">Sobre Nós</a></li>
                    <li><a class="link navStatus" href="#precos">Preços</a></li>
                    <li><a class="link navStatus" href="#contatos">Contatos</a></li>
                % end
            </ul>
        </nav>
    % end
% end


% if user:
    % if path == "logado" or path == "naoLogado":
        <ul class="user-nav">
            <li class="dropdown">
                <a href="#" class="dropdown-toggle main userf">
                    Olá, {{ user[0].upper() + user[1:] }} ▼
                </a>
                <a href="#" class="dropdown-toggle none nouserf">
                    <i class="fa-solid fa-bars" style="font-size: 28px;"></i>
                </a>
                <ul class="dropdown-menu">
                    % if pathStatus in ("LI", "L"):
                        % if pathStatus == "LI":
                            <li class="none"><a href="/">Home</a></li>
                            <li class="none"><a href="/">Catálogo</a></li>
                            <li class="none"><a href="/">Contatos</a></li>
                        % else:
                            <li class="none"><a href="/">Home</a></li>
                            <li class="none"><a href="#catalogo">Catálogo</a></li>
                            <li class="none"><a href="#contatos">Contatos</a></li>
                        % end
                    % elif pathStatus in ("A", "I"):
                        % if pathStatus == "A":
                            <li class="none"><a href="/">Home</a></li>
                            <li class="none"><a href="/">Sobre Nós</a></li>
                            <li class="none"><a href="/">Preços</a></li>
                            <li class="none"><a href="/">Contatos</a></li>
                        % else:
                            <li class="none"><a href="/">Home</a></li>
                            <li class="none"><a href="#sobre-nos">Sobre Nós</a></li>
                            <li class="none"><a href="#precos">Preços</a></li>
                            <li class="none"><a href="#contatos">Contatos</a></li>
                        % end
                    % end
                    <li class="divider none"></li>
                    <li><a href="/perfil/index"><i class="fa-solid fa-user" style="margin-right: 10px;"></i>Perfil</a></li>
                    <li class="divider"></li>
                    <li><a href="/login/logout"><i class="fa-solid fa-power-off" style="margin-right: 10px;"></i>Sair</a></li>
                </ul>
            </li>
        </ul>
    % end
% else:
    <ul class="user-nav-nao-logado">
        <li class="dropdown">
            <a href="#" class="dropdown-toggle none">
                <i class="fa-solid fa-bars" style="font-size: 28px;"></i>
            </a>
            <ul class="dropdown-menu-nao-logado">
                % if path:
                    % if path == "A":
                        <li class="none"><a href="/">Home</a></li>
                        <li class="none"><a href="/">Sobre Nós</a></li>
                        <li class="none"><a href="/">Preços</a></li>
                        <li class="none"><a href="/">Contatos</a></li>
                    % else:
                        <li class="none"><a href="/">Home</a></li>
                        <li class="none"><a href="#sobre-nos">Sobre Nós</a></li>
                        <li class="none"><a href="#precos">Preços</a></li>
                        <li class="none"><a href="#contatos">Contatos</a></li>
                    % end
                % end
                <li class="divider none"></li>
                <li><a href="/login/index"><i class="fa-solid fa-user" style="margin-right: 10px;"></i>Entrar</a></li>
                <li class="divider"></li>
                <li><a href="/register/index"><i class="fa-solid fa-power-off" style="margin-right: 10px;"></i>Cadastrar</a></li>
            </ul>
        </li>
    </ul>
    <a href="/login/index" id="sign-in" class="link">Entrar</a>
    <a href="/register/index" id="sign-up" class="link">Cadastrar</a>
% end
</header>
