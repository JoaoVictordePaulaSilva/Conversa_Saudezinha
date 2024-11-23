# ConverSaudezinha - Chatbot para Suporte a Saúde Mental

## Descrição
O **ConverSaudezinha** é um chatbot desenvolvido em **Flask** para fornecer suporte em saúde mental. O foco principal é a prevenção ao suicídio e o apoio psicológico. Além disso, o chatbot pode auxiliar na marcação de consultas presenciais e online, e oferece informações sobre sintomas e doenças, com uma abordagem acolhedora e empática.

## Arquitetura do Projeto
**Flask Application:** O código é estruturado em torno de um único aplicativo Flask. A aplicação gerencia as rotas para o login, registro de usuários, interações no chat, e exibição de informações sobre o chatbot.

**Sessions:** O sistema utiliza session para armazenar dados temporários dos usuários, como o nome do usuário, durante a interação no chat.

### Requisitos
- **Python 3.x**: Linguagem utilizada para o desenvolvimento.
- **Flask**: Framework web para Python, utilizado para criar o servidor e gerenciar as rotas.
- **Jinja2**: Motor de templates utilizado pelo Flask para gerar HTML dinâmico.
- **Flash**: Função do Flask para exibir mensagens de feedback temporárias.
- **Session**: Para manter o estado do usuário durante a navegação no sistema.


## Funcionalidades

### Página Inicial
- **Rota**: `/`
- A página inicial apresenta um formulário de login.

### Tela de Registro
- **Rota**: `/registrar`
- Permite o cadastro de novos usuários. O formulário exige o nome, CPF, idade, endereço, senha e confirmação de senha.
- Caso as senhas não coincidam ou o CPF já tenha sido registrado, o sistema exibe uma mensagem de erro.

### Tela de Login
- **Rota**: `/login`
- Realiza a validação do login com base no nome e senha fornecidos.
- Se as credenciais forem válidas, o usuário é redirecionado para a página de chat. Caso contrário, uma mensagem de erro é exibida.

### Interface de Chat
- **Rota**: `/chat`
- A página de chat permite que o usuário interaja com o chatbot. 
- O usuário envia mensagens e o chatbot responde de acordo com regras específicas, como apoio em crises de suicídio, informações sobre sintomas e doenças, e agendamento de consultas.

### Página Sobre
- **Rota**: `/sobre`
- A página apresenta informações sobre o projeto, sua finalidade e os objetivos.

## Lógica de Negócios

### Cadastro de Usuários
- **Armazenamento**: Dados do usuário (nome, CPF, idade, endereço, senha) são armazenados temporariamente em um dicionário `users`.
- **Validação**: Se o CPF já existir, o sistema não permite o cadastro de um novo usuário com o mesmo CPF. Também há validação das senhas para garantir que coincidam.

### Regras de Resposta do Chatbot
- **Suporte a Crise**: Respostas empáticas e de apoio para situações de risco de suicídio.
- **Consultas**: Informações sobre como agendar consultas presenciais e online.
- **Sintomas e Doenças**: O chatbot fornece informações sobre sintomas e doenças e auxilia o usuário a identificar condições de saúde. Dependendo do sintoma relatado, o chatbot sugere acompanhamento médico.
- **Tratamento**: O chatbot orienta o usuário a procurar ajuda especializada para tratamentos médicos, sem fornecer diagnósticos ou tratamentos diretamente.

### Gerenciamento de Estado
- **Session**: O estado do usuário, como o nome e o histórico de conversa, é mantido na sessão (`session`), o que permite que o usuário continue a conversa sem perder o contexto.

### Flash Messages
- O **Flash** é utilizado para mostrar mensagens de feedback temporárias ao usuário, como alertas de erro, confirmações de ações e dicas.

## Detalhamento das Funções e Métodos

### Função `home()`
- **Descrição**: Rota inicial que renderiza o template de login.
- **Método HTTP**: `GET`
  
### Função `register()`
- **Descrição**: Rota de registro de novos usuários. Valida o formulário de registro e, se válido, armazena os dados na variável `users`.
- **Método HTTP**: `GET` (exibe o formulário) e `POST` (processa os dados do formulário).

### Função `login()`
- **Descrição**: Rota de login. Verifica as credenciais fornecidas e, se válidas, redireciona para a página de chat.
- **Método HTTP**: `POST`

### Função `chat()`
- **Descrição**: Rota de chat, onde o usuário interage com o chatbot. O histórico de mensagens é mantido e exibido.
- **Método HTTP**: `GET` (exibe a página de chat) e `POST` (processa a entrada do usuário e gera a resposta do chatbot).

### Função `sobre()`
- **Descrição**: Rota que exibe a página "Sobre" do projeto.
- **Método HTTP**: `GET`

### Função `resposta_Chat(user_input)`
- **Descrição**: Função central que processa a entrada do usuário e gera uma resposta do chatbot com base nas regras predefinidas.
- **Lógica**: Respostas são baseadas em palavras-chave, como "suicídio", "consulta", "sintoma", entre outras. A função também gerencia o nível de gravidade da situação (ex: nível de tensão do usuário) e oferece respostas adequadas.

## Considerações Finais
Este projeto é um chatbot de apoio à saúde mental, com um foco em prevenção ao suicídio e auxílio psicológico. A estrutura básica está pronta, mas o sistema pode ser expandido e melhorado conforme novas necessidades surgem. A plataforma foi projetada para ser fácil de usar, com interações simples e uma abordagem acolhedora e empática.

