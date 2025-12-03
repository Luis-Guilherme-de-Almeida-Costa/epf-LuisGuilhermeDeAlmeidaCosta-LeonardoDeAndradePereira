C&M

Este é um projeto de template educacional voltado para o ensino de **Programação Orientada a Objetos (POO)** do Prof. Lucas Boaventura, Universidade de Brasília (UnB).

Utiliza o microframework **Bottle**. Ideal para uso em disciplinas introdutórias de Engenharia de Software ou Ciência da Computação.

## 💡 Objetivo

  O sistema C&M é uma plataforma para visualizar títulos de conteúdos digitais, neste caso, filmes enviados pelos administradores do website. Será possível utilizar funcionalidades como a busca inteligente por títulos e a visualização dos conteúdos desejados no horário em que forem lançados.

---

## 🗂 Estrutura de Pastas

```bash
poo-python-bottle-template/
├── app.py # Ponto de entrada do sistema
├── config.py # Configurações e caminhos do projeto
├── main.py # Inicialização da aplicação
├── mysql_plugin.py # Realiza a conexao com o banco de dados
├── requirements.txt # Dependências do projeto
├── README.md # Este arquivo
├── controllers/ # Controladores e rotas
├── plugins/ # Arquivo para interceptar controllers antes de sua execução
├── services/ # Services
├── sessions/ # Pasta que guarda as sessions dos usuarios do beaker
├── models/ # Definição das entidades (ex: User)
├── services/ # Lógica de persistência (JSON)
├── views/ # Arquivos HTML (Bottle Templating)
├── ├── includes # arquivos que aparecem em diversas paginas
├── static/ # CSS, Images, modules, main.js uploads
├── utils/ # Arquivos para auxiliar no desenvolvimento. (ex: validar, verificarAdm, flash)
└── .vscode/ # Configurações opcionais do VS Code
```


---

## 📁 Descrição das Pastas

### `controllers/`
Contém as classes responsáveis por lidar com as rotas da aplicação. Exemplos:
- `user_controller.py`: rotas para listagem, adição, edição e remoção de usuários.
- `base_controller.py`: classe base com utilitários comuns.
- `filme_controller.py`: classe responsável pela inserção e listagem de filmes.
- `home_controller.py`: classe responsável pela listagem das páginas principais.
- `administrador_controller`: classe responsável pela listagem e adição de administradores.
### `models/`
Define as classes que representam os dados da aplicação. Exemplo:
- `user.py`: classe `User`, com atributos como `id`, `name`, `email`, etc.
- `filmes.py`: classe `Filmes`, com atributos como `id`, `titulo`, `categoria`, `data_exibicao`, `status`, `capa_path`, `video_path`, `id_administrador`, `created_at` e 
`updated_at`.
- `administrador.py`: classe `AdministradorModel`, com funções como `get_all`, `get_by_id_pessoa`, `add_administrador`.
- `pessoas.py`: classe `Pessoas`, com atributos como `name`, `email`, `cpf`, `situacao`, `senha`.

### `services/`
Responsável por salvar, carregar e manipular dados usando arquivos JSON. Exemplo:
- `administrador_service.py`: contém métodos como `get_all`, `get_by_id_pessoa`, `save`.
- `filmes_service.py`: contém métodos como `get_all`, `get_by_id`, `get_by_category`, `get_by_name`, `add_filme`, `dalete_filme`, `_remove_file`.
- `pessoas_service.py`: contém métodos como `get_all`, `get_by_id`, `get_administrador_by_id`, `login`, `save`, `edit`, `logout`.
- `user_service.py`: contém métodos como `get_all`, `add_user`, `delete_user`.

### `views/`
Contém os arquivos `.tpl` utilizados pelo Bottle como páginas HTML:
  
- `cadastro.tpl`: Formulário para criar usuário.
- `cadastroAdm.tpl`: formulário para adicionar administrador.
- `criaFIlmes.tpl`: formulário para criar filmes.
- `editarPefil.tpl`: formulário para editar usuário.
- `filmeRemover.tpl`: formulário para remover filmes.
- `homeComLogin.tpl`: listagem dos livros e página principal.
- `homeSemLogin.tpl`: página principal para pessoas que não estão logadas.
- `leitura.tpl`: visualização do catalogo do filme.
- `login.tpl`: formulário para adentrar no sistema.
- `search.tpl`: formulário para buscar filmes.
- `videoPlayer.tpl`: visualização do filme.

### `views/includes`
Contém os arquivos `.tpl` utilizados pelo Bottle como páginas HTML:
  
- `footerComContato.tpl`: Footer com o contato.
- `footerSemContato.tpl`: Footer sem o contato.
- `headerNaoLogado.tpl`: Header principal.
- `messagesError.tpl`: Mensagem de erro.
- `messagesSuccess.tpl`: Mensagem de sucesso.
- `nav.tpl`: Navbar do site.

### `static/`
Arquivos estáticos como:
- `css/cadastroAdm.css`: estilos básicos.
- `css/infoUsuario.css`: estilos básicos.
- `css/pagamento.css`: estilos básicos.
- `css/sobraBackground.css`: estilos básicos.
- `css/style.css`: estilos básicos.
- `css/styleAutenticacao.css`: estilos básicos.
- `css/styleGeneral.css`: estilos básicos.
- `css/styleLeitura.css`: estilos básicos.
- `css/styleLogado.css`: estilos básicos.
- `css/styleNaoLogado.css`: estilos básicos.
- `css/styleSearch.css`: estilos básicos.
- `css/styleFooter.css`: estilos básicos.
- `css/videoPlayer.css`: estilos básicos.
- `modules/atualizarNomePasta.js`: scripts JS para a inserção de filmes.
- `modules/nav.js`: scripts JS para navbar responsiva.
- `modules/playerVideo.js`: scripts JS essencial para a interação com o video.
- `Images/*` Imagens utilizadas no website.
- `uploads/capas` Pasta que guarda as capas dos sites.
- `uploads/videos` Pasta que guarda os videos dos sites.

### `utils/`
Pasta utilizada no sistema inteiro para auxiliar no projeto:
- `flash.py`: Guarda os sucessos e erros temporários.
- `validate.py`: Valida os campos.
- `verificarAdm.py`: Verifica se é adm e retorna true, false.

### `plugins/`
Pasta utilizada no sistema inteiro para auxiliar no controller:
- `auth_redirect_plugin.py`: Gerencia permissão de entrada nas urls.

---

## ▶️ Como Executar

1. Crie o ambiente virtual na pasta fora do seu projeto:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\\Scripts\\activate     # Windows
```

2. Entre dentro do seu projeto criado a partir do template e instale as dependências:
```bash
pip install -r requirements.txt
```

3. Rode a aplicação:
```bash
python main.py
```

4. Accese sua aplicação no navegador em: [http://localhost:8080](http://localhost:8080)

---

## ✍️ Personalização
Para adicionar novos modelos (ex: Atividades):

1. Crie a classe no diretório **models/**.

2. Crie o service correspondente para manipulação do JSON.

3. Crie o controller com as rotas.

4. Crie as views .tpl associadas.

---

## 🧠 Autor e Licença
Projeto desenvolvido como template didático para disciplinas de Programação Orientada a Objetos, baseado no [BMVC](https://github.com/hgmachine/bmvc_start_from_this).
Você pode reutilizar, modificar e compartilhar livremente.
