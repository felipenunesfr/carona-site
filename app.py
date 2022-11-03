# Importando biblioteca Flask
from flask import Flask, render_template, request
from funcao import *
from datetime import datetime
import os




caronas_pesquisadas = []

caronas_pesquisadas2 = 0

datauser = 0

arq = open('registrado.txt', 'a')

fotos = os.path.join('static', 'fotos')

site = Flask(__name__)

site.config['UPLOAD_FOLDER'] = fotos

imagem = os.path.join(site.config['UPLOAD_FOLDER'], 'carona.png')
meu_perfil = os.path.join(site.config['UPLOAD_FOLDER'], 'meu_perfil.png')
receberfoto = os.path.join(site.config['UPLOAD_FOLDER'], 'receber.png')
darfoto = os.path.join(site.config['UPLOAD_FOLDER'], 'dar.png')
imagem_dados = os.path.join(site.config['UPLOAD_FOLDER'], 'imagem_dados.png')
imagem_oferecidas = os.path.join(site.config['UPLOAD_FOLDER'], 'imagem_oferecidas.png')
imagem_desejadas = os.path.join(site.config['UPLOAD_FOLDER'], 'imagem_desejadas.png')

@site.route("/login")
@site.route("/")
def loginpage():
    
    return render_template("pagina_login.html", user_image = imagem)

@site.route("/login", methods =["POST"])
def acesso():
    
    if request.method == "POST":
        usuario = request.form["usuario"]
        senha = request.form["senha"]

    usuario = usuario.strip()
    senha = senha.strip()
    
    usuario = "?" + usuario + "?"
    senha = "?" + senha + "?"
    
    if senha == "" or usuario == "":
        return render_template("pagina_login_erro.html", user_image = imagem)
    
    login = codigo(usuario) + "-" + codigo(senha)
    arq = open('registrado.txt') 
    registrados = arq.read()
    
    if login in registrados:
        linha = abrir(login)
        dados = tradutor(linha)
        global datauser
        datauser = dados
        arq.close()
        return menu_inicial()
            
    else:
        return render_template("pagina_login_erro.html", user_image = imagem)
    
@site.route("/cadastro")   
def cadastrar():
    
    return render_template("pagina_cadastro.html", user_image = imagem) 
    
@site.route("/cadastro", methods =["POST"]) 
def registre():
    
    if request.method == "POST":
        usuario = request.form["usuario"]
        senha = request.form["senha"]
        email = request.form["email"]
        dre = request.form["dre"]
        telefone = request.form["telefone"]
      
    erro = 0  
      
    usuario = usuario.strip()
    erro = validar(usuario)
    
    if erro == 1:
        return erros("Reposta inválida: Não é permitido acento ou espaços no usuário.")

    if erro == 2:
        return erros("Usuário Inválido; em branco ou já existente.")
    
    senha = senha.strip()
    erro = validarsenha(senha)
    
    if erro == 1:
        return erros("Reposta inválida: Não é permitido acento ou espaços na Senha.")
    
    if erro == 2:
        return erros("Senha inválida: em branco. ") 
        
    email = email.strip()
    erro = validar(email)
    
    if erro == 1:
        return erros("Reposta inválida: Não é permitido acento ou espaços no email")

    if erro == 2:
        return erros("Email Inválido; em branco ou já existente.")
    
    dre = dre.strip()
    erro = validar(dre)
    
    if erro == 1:
        return erros("Reposta inválida: Não é permitido acento ou espaços no DRE")

    if erro == 2:
        return erros("DRE Inválido; em branco ou já existente.")
    
    telefone = telefone.strip()
    erro = validartele(telefone)
    
    if erro == 1:
        return erros("Reposta inválida: Não é permitido acento ou espaços no telefone.")

    if erro == 2:
        return erros("Telefone Inválido; em branco ou já existente.")
    
    if erro == 3:
        return erros("Telefone Inválido.")
    
    else:
        telefone = erro
    
    v = diferente(usuario, senha, email, dre, telefone)
    
    if v == 0:
        return erros("Um campo não pode ser igual a outro.")
    
    usuario = "?" + usuario + "?"
    senha = "?" + senha + "?"
    email = "?" + email + "?"
    dre = "?" + dre + "?"
    telefone = "?" + telefone + "?"

    
    login = ("\n" + codigo(usuario) + "-" + codigo(senha) + "-" + codigo(email) + "-" + codigo(dre) + "-" + codigo(telefone) + "-" + codigo("usuario") + "+")
    arq = open('registrado.txt', 'a')
    arq.write(login)
    arq.close()
    return render_template("pagina_login.html", user_image = imagem)    

def erros(erro):
    
    return render_template("pagina_cadastro.html", user_image = imagem, erro7 = erro)

@site.route("/menuinicial")
def menu_inicial():
    return render_template("menu_inicial.html", user_image = imagem, botao1 = meu_perfil, botao2 = darfoto, botao3 = receberfoto)
    
@site.route("/darcarona")
def darcarona():
    return render_template("dar_carona.html", user_image = imagem)

@site.route("/darcarona", methods = ['POST'])  
def dar1():
    
    try:
        user = str(datauser[0])
    except:
        return render_template("pagina_login.html", user_image = imagem)
    
    if request.method == "POST":
        via = request.form["via"]
    
    if request.method == "POST":
        dia1 = request.form["dia1"]
        mes1 = request.form["mes1"]
    
    dia1 = acertar(dia1)
    mes1 = acertar(mes1)
        
    if dia1 != "" and mes1 == "" or dia1 == "" and mes1 != "": 
         return "Data inválida"
    
    if dia1 != "" and mes1 != "":
        g = data_valida(int(dia1), int(mes1))
    
        if g == 0:
            errosdar("Data inválida!")
    
        data1 = dia1 + "/" + mes1
        datare = data1   
    else:
        errosdar("É obrigatório ter uma data!")
    
    try:
        conferirdia(data1)
    except:
        return errosdar("A data precisa ser pelo menos atual")
    
    if request.method == "POST":
        hora1 = request.form["hora1"]
        min1 = request.form["min1"]
    
    hora1 = acertar(hora1)
    min1 = acertar(min1)
    
    if hora1 != "" and min1 == "" or hora1 == "" and min1 != "": 
        return errosdar("Hora inválida")
    
    if hora1 != "" and min1 != "":
    
        horario1 = hora1 + ":" + min1
        
    else:
        horario1 = ""
    
    if request.method == "POST":
        hora2 = request.form["hora2"]
        min2 = request.form["min2"]
    
    hora2 = acertar(hora2)
    min2 = acertar(min2)
    
    if hora2 != "" and min2 == "" or hora2 == "" and min2 != "": 
        return errosdar("Hora inválida")
    
    if hora2 != "" and min2 != "":
    
        horario2 = hora2 + ":" + min2
        
    else:
        horario2 = ""
    
    if horario1 == "" and horario2 != "":
        return errosdar("Hora inválida!")
    
    if horario1 != "":
        b = conferirhora(horario1, datare)
            
        if b:
            errosdar("A hora pode ser no mínimo 2 horas atrás")
    
    if horario2 == "":    
        horario2 = "Qualquer Hora 2"
    
    if horario1 == "":    
        horario1 = "Qualquer Hora 1"
        
    if horario1 == "Qualquer Hora 1" and horario2 != "Qualquer Hora 2":
        return errosdar("Horário incorreto")
    
    if horario1 != "Qualquer Hora 1" and horario2 != "Qualquer Hora 2":
        try:
            entre = formatohora(horario1, horario2)
        except:
            return errosdar("Horário incorreto")
    else:
        entre = "NT"    
        
    if request.method == "POST":
        origem = request.form["origem"]
        bairro = request.form["destino"]
        passagem1 = request.form["passagem1"]
        passagem2 = request.form["passagem2"]
        
    origem = origem.strip()
    bairro = bairro.strip()
    passagem1 = passagem1.strip()
    passagem2 = passagem2.strip()
    
    if passagem1 == "" and passagem2 != "":
        passagem1 = passagem2
        passagem2 = ""
    
    if via == "volta" and bairro == "":
        return errosdar("Na volta é preciso adicionar pelo menos o destino!")
    
    if via == "ida" and origem == "":
        return errosdar("Na ida é preciso adicionar pelo menos a origem!")
        
    if via == "volta" and passagem1 != "":
        bairro = bairro + "_" + passagem1
        
        if passagem2 != "" :
            bairro = bairro + "_" + passagem2
            
    if via == "ida" and passagem1 != "":
        origem = origem + "_" + passagem1
        
        if passagem2 != "" :
            origem = origem + "_" + passagem2
    
    if bairro == "":
        bairro = "Qualquer Destino"
        
    if origem == "":
        origem = "Qualquer Origem"    
            
    caminho = ("\n" + user + "-" + via + "-" + origem + "-" + horario1 + " / " + entre + " / " + horario2 + "-" + bairro + "-" + data1)        
    
    tela = (user + "-" + via + "-" + origem + "-" + horario1 + " / " + entre + " / " + horario2 + "-" + bairro + "-" + data1)
    
    arq2 = open('registrado.txt', 'r')
    
    l = achar_minhas_caronas(user)
    l = len(l)
    
    if l == 10:
        return errosdar("Já foi atingido o limite máximo de caronas oferecidas!")
    
    elif tela not in arq2:
        arq2.close()
        arq2 = open('registrado.txt', 'a')
        arq2.write(caminho)
    else:
        return errosdar("Carona já existente!")
    
    arq2.close()
    
    return mostrar_oferecidas_page()
    
def errosdar(erro):
    
    return render_template("dar_carona.html", user_image = imagem, erro7 = erro)

@site.route("/meuperfil")
def meuperfil(): 
    return render_template("meu_perfil.html", user_image = imagem, botao1 = imagem_dados, botao2 = imagem_oferecidas, botao3 = imagem_desejadas)   

@site.route("/caronasofereciadas")
def mostrar_oferecidas_page():
    
    try:
        usuario = str(datauser[0])
    except:
        return render_template("pagina_login.html", user_image = imagem)
    
    l = achar_minhas_caronas(usuario)
    del l[-1]
    carona = l 
    x = len(carona)
    if l == []:
        mensagem1 = "Nenhuma carona oferecida!"
    else:
        for a in range(len(carona)):
            carona[a] = (carona[a]).strip("?")
            
        mensagem1 = ""
        
    return render_template("mostrar_caronas_oferecidas.html", user_image = imagem, caronas = carona, maximo = x, mensagem = mensagem1)

@site.route("/caronasofereciadas", methods =['POST'])
def mostrar_oferecidas():
    
    try:
        usuario = str(datauser[0])
    except:
        return render_template("pagina_login.html", user_image = imagem)
    
    z = find(usuario)
    m = find("+")
    
    for g in range(len(m)):
        if m[g] in z:
            z.remove(m[g])

    n = []
    for l in range(len(z)):
        d = z[l]
        with open("registrado.txt") as f:
            texto = f.readlines()[d]
            n.append(texto)
    
    if request.method == "POST":
        numero = request.form["escolha"]
    
    if numero != "":
    
        h = numero
        h = int(h)
        h = h - 1
        j = str(n[h])
        j = j.strip()
    
        with open('registrado.txt', 'r') as fr:
            lines = fr.readlines()
    
            with open('registrado.txt', 'w') as fw:
                for line in lines:
                    
                    if line.strip('\n') != j:
                        fw.write(line)
                        
        k = find(j)
        p = pesquisa(codigo("usuario"), 0)
        z = set(k) & set(p)
        z = list(z)
        if z != []:
            c = []
            s = ""
            q = 1
            for y in range(len(z)):
                with open("registrado.txt") as f:
                    texto = f.readlines()[z[y]] 
                    r = texto.split("+")
                    for v in r:
                        if j == v:
                            v = ""
                            q = 0
                        if q:
                            s = s + "+" + v
                        q = 1
                    s = s[1:]
                    c.append(s)
                    
            for o in range(len(z)):
                
                alterar_linha(z[o], c[o])
                             
        men = "Carona excluída com sucesso!"
    else:
        men = ""           
             
    l = achar_minhas_caronas(usuario)
    del l[-1]
    carona = l 
    x = len(carona)
    
    if l == []:
        mensagem1 = "Nenhuma carona oferecida!"
    else:
        mensagem1 = ""        

        
    return render_template("mostrar_caronas_oferecidas.html", user_image = imagem, caronas = carona, maximo = x, mensagem = mensagem1, mensagem2 = men)

def achar_minhas_caronas(usuario):
    
    z = find(usuario)
    m = find("+")
    
    for g in range(len(m)):
        if m[g] in z:
            z.remove(m[g])

    n = []
    for l in range(len(z)):
        d = z[l]
        with open("registrado.txt") as f:
            texto = f.readlines()[d]
            n.append(texto)
    
    l = show3(n)
    l = abrirl(l)
    l = l.split("[")
    
    return l

@site.route("/recebercarona")
def receberpage(): 
    tempo = datetime.now()
    mesAtual = tempo.month
    return render_template("receber_carona.html", user_image = imagem, minimomes = str(mesAtual))  

@site.route("/recebercarona", methods =['POST'])
def receber_carona():
    
    try:
        user = str(datauser[0])
    except:
        return render_template("pagina_login.html", user_image = imagem)
    
    via = ""
    
    if request.method == "POST":
        via = request.form["via"]
        
    if request.method == "POST":
        dia1 = request.form["dia1"]
        mes1 = request.form["mes1"]
    
    dia1 = acertar(dia1)
    mes1 = acertar(mes1)
    
    if dia1 != "" and mes1 == "" or dia1 == "" and mes1 != "": 
         return "Hora inválida"
    
    if dia1 != "" and mes1 != "":
        g = data_valida(int(dia1), int(mes1))
    
        if g == 0:
            erros_receber("Data inválida!")
    
        data1 = dia1 + "/" + mes1
        datare = data1 
   
        try:
            conferirdia(data1)
        except:
            return erros_receber("A data precisa ser pelo menos atual")
        
    else:
        data1 = ""
        datare = 0 
                  
    if request.method == "POST":
        dia2 = request.form["dia2"]
        mes2 = request.form["mes2"]
    
    dia2 = acertar(dia2)
    mes2 = acertar(mes2)
    
    if dia2 != "" and mes2 == "" or dia2 == "" and mes2 != "": 
         return "Data inválida"
    
    if dia2 != "" and mes2 != "":
        g = data_valida(int(dia2), int(mes2))
    
        if g == 0:
            erros_receber("Data inválida!")
    
        data2 = dia2 + "/" + mes2
    
        try:
            conferirdia(data2)
        except:
            return erros_receber("A data precisa ser pelo menos atual!")
    else:
        data2 = ""  
    
    if data1 == "" and data2 != "":
        return erros_receber("Data inválida!")
    
    if data1 != "" and data2 != "":
              
        dia = periododia1(data1, data2)
            
        if dia == 1:
            return erros_receber("Data inválida1!") 
    else:
        dia = data1
        
    if request.method == "POST":
        hora1 = request.form["hora1"]
        min1 = request.form["min1"]
    
    hora1 = acertar(hora1)
    min1 = acertar(min1)
    
    if hora1 != "" and min1 == "" or hora1 == "" and min1 != "": 
        return erros_receber("Hora inválida")
    
    if hora1 != "" and min1 != "":
    
        horario1 = hora1 + ":" + min1
        
    else:
        horario1 = ""
        
    if request.method == "POST":
        hora2 = request.form["hora2"]
        min2 = request.form["min2"]
    
    hora2 = acertar(hora2)
    min2 = acertar(min2)
    
    if hora2 != "" and min2 == "" or hora2 == "" and min2 != "": 
        return erros_receber("Hora inválida")
    
    if hora2 != "" and min2 != "":
    
        horario2 = hora2 + ":" + min2
        
    else:
        horario2 = ""
    
    if horario1 == "" and horario2 != "":
        return erros_receber("Hora inválida!")
    
    if horario1 != "":
        b = conferirhora(horario1, datare)
            
        if b:
            erros_receber("A hora pode ser no mínimo 2 horas atrás")
    
    if horario1 != "" and horario2 != "":
        entre = formatohora(horario1, horario2)
        entre = entre.split()
        entre.append(horario1)
        entre.append(horario2)
    
    elif horario1 != "" and horario2 == "":
        entre = horario1       
         
    else:
        entre = ""
        
    origem = []
    bairro = []  
        
    if request.method == "POST":
        origem.append((request.form["origem"]).strip())
        bairro.append((request.form["destino"]).strip())
        passagem1 = request.form["passagem1"]
        passagem2 = request.form["passagem2"]
        
    passagem1 = passagem1.strip()
    passagem2 = passagem2.strip()
    
    if passagem1 == "" and passagem2 != "":
        passagem1 = passagem2
        passagem2 = ""
        
    if via == "volta" and passagem1 != "":
        bairro.append(passagem1)
        
        if passagem2 != "" :
            bairro.append(passagem2)
            
    if via == "ida" and passagem1 != "":
        origem.append(passagem1)
        
        if passagem2 != "" :
            origem.append(passagem2)
            
    if via == "" and passagem1 != "":
        origem.append(passagem1)
        
        if passagem2 != "" :
            origem.append(passagem2)
    
    if via == "":
        u = pesquisa("volta", 0)
        i = pesquisa("ida", 0)
        h = u + i
    else:
        h = pesquisa(via, 0)
    
    q = pesquisa(dia, 0)
    g = pesquisa(origem, "Qualquer Origem")
    b = pesquisa(bairro, "Qualquer Destino")
    k = pesquisa(user, 0)
    c = pesquisa(codigo(user), 0)
    e = find("+")
    if entre != "":
        en = pesquisa(entre, 0)
        z = (set(h) & set(b) & set(g) & set(q) & set(en))
    else:
        j = pesquisa(hora1, "Qualquer Hora 1")
        v = pesquisa(hora2, "Qualquer Hora 2")  
        z = (set(h) & set(b) & set(v) & set(q) & set(j) & set(g))
    z = list(z)
    
    m = k + c + e
    for a in range(len(m)):
        if m[a] in z:
            z.remove(m[a])
               
    t = 0
    l = []
    o = []
    
    while t < len(z):
        n = int(z[t])
        arquivo = open("registrado.txt")     
        f = arquivo.readlines()
        d = (f[n])
        l.append(abrir2(d))       
        o.append(d)
        arquivo.close()
        t = t + 1 
    
    global caronas_pesquisadas
        
    caronas_pesquisadas = o
        
    y = []
    for a in range(len(l)):
        y.append(str(a + 1) + "# " + l[a])
    
    global caronas_pesquisadas2
        
    caronas_pesquisadas2 = y
    
    return pesquisa_carona_page(y)

@site.route("/pesquisacarona")
def pesquisa_carona_page(carona):
    
    if carona != []:
        carona1 = carona
        for a in range(len(carona1)):
            carona1[a] = (carona1[a]).strip("?")
            
        x = len(carona)
        resposta = ""
    if carona == []:
        resposta = "Nenhuma carona disponível"
        carona1 = ""
        x = 0
        
    return render_template("mostrar_caronas_pesquisa.html", user_image = imagem, caronas = carona1, maximo = x, mensagem = resposta)

@site.route("/pesquisacarona", methods =['POST'])
def pesquisa_carona():
    
    try:
        user = str(datauser[0])
    except:
        return render_template("pagina_login.html", user_image = imagem)
    
    if request.method == "POST":
        escolha = request.form["escolha"] 
           
    j = caronas_pesquisadas    
    y = []    
    m = escolha
    m = int(m)
    y.append(j[m - 1])
    t = addc(y, user)
    if t == 1:
        r = "Carona adicionada!"
        
    if t == 2:
        r = "Essa carona já foi adicionada!"
    carona = caronas_pesquisadas2 
    x = len(caronas_pesquisadas2)
    
    return render_template("mostrar_caronas_pesquisa.html", user_image = imagem, caronas = carona, maximo = x, erro7 = r)
    
@site.route("/caronasadicionadas")
def caronas_adicionadas_page():
    
    try:
        usuario = str(datauser[0])
    except:
        return render_template("pagina_login.html", user_image = imagem)
    
    k = pesquisa(codigo(usuario), 0)
    j = pesquisa(codigo("usuario"), 0)
    z = set(k) & set(j)
    z = list(z)

    z = int(z[0])
            
    with open("registrado.txt") as f:
        texto = f.readlines()[z]
    
    h = show(texto)
    x = len(h)
    
    if h == []:
        mensagem1 = "Nenhuma carona adicionada!"
    else:
        mensagem1 = ""
        
    
    a = show4(texto)
    del a[-1]
    l = a
    g = []
    
    for b in l:
        if "+" in b:
            b = b.split("-")
            b = b[0]
            b = b[1:]
            g.append(b)
    
    g = list(g)
    
    telefones = []
    
    for i in range(len(g)):
        
        k = pesquisa(codigo(g[i]), 0)
        j = pesquisa(codigo("usuario"), 0)
        z = set(k) & set(j)
        z = list(z)
        z = int(z[0])
    
        with open("registrado.txt") as f:
                texto = f.readlines()[z]
            
        texto = show4(texto)
        texto = texto[0]
        texto = texto.strip()
        texto = texto + "+"
        texto = tradutor(texto)  
        telefones.append(texto[4])
    
    for y in range(len(h)):
        h[y] = (h[y]).strip("?")
    
    u = []
    for b in range(len(h)):
        u.append(str(b + 1) + "# " + h[b] + " / " + (telefones[b]).strip("?")) 
        
    return render_template("mostrar_caronas_adicionadas.html", user_image = imagem, caronas = u, mensagem = mensagem1, maximo = x)

@site.route("/caronasadicionadas", methods =['POST'])
def caronas_adicionadas():
    
    try:
        usuario = str(datauser[0])
    except:
        return render_template("pagina_login.html", user_image = imagem)
    
    
    if request.method == "POST":
        escolha = request.form["escolha"]
    
    escolha = int(escolha)
    k = pesquisa(codigo(usuario), 0)
    j = pesquisa(codigo("usuario"), 0)
    z = set(k) & set(j)
    z = list(z)
    z = int(z[0])
    
    with open("registrado.txt") as f:
        texto = f.readlines()[z]    
    
    a = show4(texto)
    
    del a[escolha]
    a = LtoS(a)
    
    alterar_linha(z, a)
    
    return caronas_adicionadas_page()

@site.route("/meusdados", methods =['POST'])
def meus_dados():    
    
    try:
        usuario = str(datauser[0])
    except:
        return render_template("pagina_login.html", user_image = imagem)
    
    k = pesquisa(codigo(usuario), 0)
    j = pesquisa(codigo("usuario"), 0)
    z = set(k) & set(j)
    z = list(z)
    z = int(z[0])
    
    with open("registrado.txt") as f:
        texto = f.readlines()[z]    
    
    todo = show4(texto)
    
    
    linha = abrir(texto)
    dados = tradutor(linha)
    
    user = (dados[0]).strip("?")
    senha = (dados[1]).strip("?")
    email = (dados[2]).strip("?")
    dre = (dados[3]).strip("?")
    telefone = (dados[4]).strip("?")
    
    return render_template("meus_dados.html", user_image = imagem, usuario1 = user, senha1 = senha,  email1 = email, dre1 = dre, telefone1 = telefone )

@site.route("/meusdadoseditar")
def meus_dados_editar_page():    

    return render_template("meus_dados_editar.html", user_image = imagem)
    
@site.route("/meusdadoseditar", methods =['POST'])
def meus_dados_editar(): 
    
    global datauser
    
    try:
        user = str(datauser[0])
    except:
        return render_template("pagina_login.html", user_image = imagem)
   
    k = pesquisa(codigo(user), 0)
    j = pesquisa(codigo("usuario"), 0)
    z = set(k) & set(j)
    z = list(z)
    z = int(z[0])
    
    with open("registrado.txt") as f:
        texto = f.readlines()[z]    
    
    todo = show4(texto)
    
    
    linha = abrir(texto)
    dados = tradutor(linha)
    
    if request.method == "POST":
        senha = request.form["senha1"]
        email = request.form["email1"]
        dre = request.form["dre1"]
        telefone = request.form["telefone1"]

    senha = senha.strip()
    email = email.strip()
    dre = dre.strip()
    telefone = telefone.strip()
    
    if senha != "":
        
        erro = validarsenha(senha)
    
        if erro == 1:
            return render_template("meus_dados_editar.html", user_image = imagem, teste = "Reposta inválida: Não é permitido acento ou espaços na Senha.")
        
        if erro == 2:
            return render_template("meus_dados_editar.html", user_image = imagem, teste = "Senha inválida: em branco. ") 
        
        senha = "?" + senha + "?"
        dados[1] = senha
    
    if email != "":
        
        erro = validar(email)
        
        if erro == 1:
            return render_template("meus_dados_editar.html", user_image = imagem, teste = "Reposta inválida: Não é permitido acento ou espaços no email")

        if erro == 2:
            return render_template("meus_dados_editar.html", user_image = imagem, teste = "Email Inválido; em branco ou já existente.")

        email = "?" + email + "?"
        dados[2] = email
    
    if dre != "":
        
        erro = validar(dre)
    
        if erro == 1:
            return render_template("meus_dados_editar.html", user_image = imagem, teste = "Reposta inválida: Não é permitido acento ou espaços no DRE")

        if erro == 2:
            return render_template("meus_dados_editar.html", user_image = imagem, teste = "DRE Inválido; em branco ou já existente.")
        
        dre = "?" + dre + "?"
        dados[3] = dre
        
    if telefone != "":

        erro = validartele(telefone)
    
        if erro == 1:
            return render_template("meus_dados_editar.html", user_image = imagem, teste = "Reposta inválida: Não é permitido acento ou espaços no telefone.")

        if erro == 2:
            return render_template("meus_dados_editar.html", user_image = imagem, teste = "Telefone Inválido; em branco ou já existente.")
        
        if erro == 3:
            return render_template("meus_dados_editar.html", user_image = imagem, teste = "Telefone Inválido.")
        
        else:
            
            telefone = erro
            telefone = "?" + telefone + "?"
            dados[4] = telefone
    
    dados1 = dados
    
    usuario = dados1[0]
    senha = dados1[1]
    email = dados1[2]
    dre = dados1[3]
    telefone = dados1[4]
    
    v = diferente(usuario, senha, email, dre, telefone)
    
    if v == 0:
        return render_template("meus_dados_editar.html", user_image = imagem, teste = "Um campo não pode ser igual a outro.")
    
    datauser = "-".join(dados)
    
    for a in range(len(dados)):
        dados[a] = codigo(dados[a])
    
    dados = ('-'.join(dados))
    dados = dados + "-" + str(codigo("usuario"))
    todo[0] = dados
    
    total = ""
    for b in todo:
        total = total + b
    

    alterar_linha(z, total)
    
    return meus_dados()

@site.route("/excluir", methods =['POST'])
def exluir_page():
    
    if request.method == 'POST':
        if request.form['botao'] == 'Enviar':
            
            try:
                usuario = str(datauser[0])
            except:
                return render_template("pagina_login.html", user_image = imagem)
            
            z = find(usuario)
            m = find("+")
            
            for g in range(len(m)):
                if m[g] in z:
                    z.remove(m[g])

            n = []
            for l in range(len(z)):
                d = z[l]
                with open("registrado.txt") as f:
                    texto = f.readlines()[d]
                    n.append(texto)
            
            for h in range(len(n)):
                j = str(n[h])
                j = j.strip()
            
                with open('registrado.txt', 'r') as fr:
                    lines = fr.readlines()
            
                    with open('registrado.txt', 'w') as fw:
                        for line in lines:
                            
                            if line.strip('\n') != j:
                                fw.write(line)
                                
                k = find(j)
                p = pesquisa(codigo("usuario"), 0)
                z = set(k) & set(p)
                z = list(z)
                if z != []:
                    c = []
                    s = ""
                    q = 1
                    for y in range(len(z)):
                        with open("registrado.txt") as f:
                            texto = f.readlines()[z[y]] 
                            r = texto.split("+")
                            for v in r:
                                if j == v:
                                    v = ""
                                    q = 0
                                if q:
                                    s = s + "+" + v
                                q = 1
                            s = s[1:]
                            c.append(s)
                            
                    for o in range(len(z)):
                        
                        alterar_linha(z[o], c[o])   
        
        k = pesquisa(codigo(usuario), 0)
        j = pesquisa(codigo("usuario"), 0)
        z = set(k) & set(j)
        z = list(z)
        z = int(z[0])
        alterar_linha(z, "")
        return render_template("excluir.html", user_image = imagem, mensagem = "exluida com sucesso")    
    else:
        return render_template("excluir.html", user_image = imagem)    
   
def erros_receber(erro):
    tempo = datetime.now()
    mesAtual = tempo.month
    return render_template("receber_carona.html", user_image = imagem, erro7 = erro, minimomes = str(mesAtual))

atual()
linhabranca()   
if __name__ == "__main__":
    site.run()