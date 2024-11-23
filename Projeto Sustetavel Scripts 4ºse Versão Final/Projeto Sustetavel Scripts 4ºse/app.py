from flask import Flask, render_template, redirect, request, url_for, flash, session
##precisa dessa bct abaixo para rodar bonitinho
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Senhazinha'
users = {}  # Armazena temporariamente os dados dos usuários
historico_conversa = [] #armazena as mensagens, tanto do chat qnt do usuario 
nivel_tensao = 0
sintoma_nivel = 0
ajuda = True
St_sintoma = False

@app.route('/')
def home():
    return render_template('login.html')
##metodos para as modificações da tela de registro
@app.route('/registrar', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nome = request.form['nome']
        cpf = request.form['cpf']
        idade = request.form['idade']
        endereco = request.form['endereco']
        senha = request.form['senha']
        confirma_senha = request.form['confirma_senha']
        session['nome_usuario'] = nome # Armazena o nome do usuário para usar no chat
       
        if senha != confirma_senha:
            flash("As senhas não coincidem. Tente novamente.")
            return redirect(url_for('register'))
       
        if cpf in users:
            flash("Usuário já cadastrado.")
            return redirect(url_for('register'))

        # Salva os dados temporariamente
        users[cpf] = {
            'nome': nome,
            'idade': idade,
            'endereco': endereco,
            'senha': senha
        }
        flash("Cadastro realizado com sucesso!")
        return redirect(url_for('home'))

    return render_template('registrar.html')
##metodo para as modificações da pagina de login
@app.route('/login', methods=['POST'])
def login():
    nome = request.form.get('nome')
    senha = request.form.get('senha')
   
    # Validação simples para login
    for user_data in users.values():
        if user_data['nome'] == nome and user_data['senha'] == senha:
            return redirect(url_for('chat'))
   
    flash("Credenciais incorretas! Tente novamente.")
    return redirect(url_for('home'))

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        user_input = request.form['user_input'].lower()
        response = resposta_Chat(user_input)
        historico_conversa.append({'user': user_input, 'bot': response})
##esse else é para ouros metodos, como o get, faz com que execute do mesmo jeito
    else:
        user_input = ''
        response = ''
    
    nome_usuario = session['nome_usuario']
    return render_template('chat.html', historico_conversa=historico_conversa, nome_usuario=nome_usuario)

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')


def resposta_Chat(user_input):
    global nivel_tensao, ajuda, St_sintoma, sintoma_nivel

    ##Ifs Suicídio ou depressão
    if "suicídio" in user_input or "deprimido" in user_input or "me matar" in user_input:
        nivel_tensao += 1

    if nivel_tensao == 1 and ajuda:
        return "Sinto muito por você estar passando por isso. Para apoio imediato, entre em contato com um profissional de saúde mental ou ligue 188."
    elif nivel_tensao == 2 and ajuda:
        return "Considere entrar em contato com um profissional, existem pessoas que se importam com você e não gostariam que você tomasse uma decisão errada, por favor, ligue 188."
    elif nivel_tensao >= 3 and ajuda:
        return "Por favor, ligue para 188 para receber assistência, sua vida é mais importante que um momento complicado, continue firme e não desista, ainda há muito para viver."
    elif not ajuda:
        return "Fale mais, estou aqui para te apoiar e te mostrar o qual forte você é!"
    
    ## Ifs Consulta
    elif "consulta presencial" in user_input:
        return "Para uma consulta presencial o seu endereço é o mesmo cadastrado anteriormente?. Podemos usá-lo para encontrar clínicas próximas?"
    elif "sim" in user_input and not St_sintoma:
        return "Encontrei algumas opções de clínicas próximas ao seu endereço: \n 1. Clinica A+ - Rua A, 123, Telefone: (11) 1234-5678 \n 2. Grupo Fleury - Av. Saúde, 456, Telefone: (11) 9876-5432 \n Deseja mais alguma ajuda?" 
    elif "consulta online" in user_input:
        return "Para consultas online, aqui está uma lista de números e e-mails de clínicas e médicos que atendem remotamente. Qual especialidade você precisa?"
    
    ## Ifs para sintomas e doenças
    elif "sintoma" in user_input or "doença" in user_input:
        return "Por favor, me diga mais sobre os sintomas ou a doença que você quer saber."
    elif "dor de cabeça" in user_input:
        if sintoma_nivel == 0:
            sintoma_nivel += 1
            return "Normalmente dor de cabeça está associada a altos niveis de estresse ou falta de hidratação, tente tomar mais água e fazer descansos com o que quer que estiver fazendo, tem mais algum sintoma que queira falar ?"
        elif sintoma_nivel == 1:
            return "Tente fazer um descanso do que estiver fazendo, caso persista, consulte um médico, eu posso te ajudar a marcar uma consulta :)"
    elif "coceira na pele" in user_input:
        if sintoma_nivel == 0:
            St_sintoma = True
            return "Coceiras na pele podem ser indicativo de alergias ou de alguma picada de inseto, você está com dor ou o local da coceira está sangrando ?"
        elif sintoma_nivel == 1:
            St_sintoma = True
            return "Procure ajuda, coceiras e dor de cabeça podem ser o início de alguma infecção ou alguma alergia mais forte, você está com dor ou o local da coceira está sangrando ?"
    elif "sim" in user_input and St_sintoma:
        St_sintoma = False
        return "Um Dermatologista conseguiria fazer um diagnóstico melhor, quando há sangramento ou dor esses sintomas se tornam mais preocupantes, procure ajuda o mais rápido possível."
    elif "não" in user_input and St_sintoma:
        St_sintoma = False
        return "Isso é bom, caso houvesse algum desses sintomas a situação seria mais preocupante, compre alguma pomada para passar na área afetada ou tente descansar um pouco."
    
    ##Ifs para Tratamento e encerramento de assunto
    elif "tratamento" in user_input:
        return "Não posso te fornecer dados sobre tratamentos, pois esse é um assunto que precisa ser conversado com um médico especialista na área."
    elif "entendi" in user_input:
        return "Espero que tenha recebido a ajuda que precisava, qualquer coisa estarei aqui a sua disposição."

    ## If recusando ajuda e caso padrão
    elif "não quero ajuda" in user_input or "pare de oferecer ajuda" in user_input:
        ajuda = False
        return "Entendo, não irei mais falar sobre o número de prevenção ao suicidio, mas saiba que eu confio na sua força para superar esse momento e estarei aqui para o que precisar!!"
    else:
        return "Desculpe, ainda estou aprendendo. Tente perguntar de outra forma!"


##esse trem aqui é o que faz rodar para os leigos
## deixa ele quietinho ai
if __name__ == "__main__":
    app.run(debug=True)
