from datetime import datetime

arq = open('registrado.txt', 'a')

#adiciona uma carona a mesma linha do usuario no arquivo texto, recebe o nome do usuario e o numero da carona desejada
def addc(m, t):
    
    m = str(m[0])
    m = m.strip()
    k = pesquisa(codigo(t), 0)
    j = pesquisa(codigo("usuario"), 0)
    z = set(k) & set(j)
    z = list(z)
    z = int(z[0])
    p = desejadas(t)
    
    if m not in p:
        
        with open("registrado.txt") as f:
            texto = f.readlines()[z]
            
        nova = texto.strip() + m + "+"
        arq2 = open('registrado.txt', 'r')
        
        arq2.close()
        alterar_linha(z, nova)
        return 1
        
    else:
        return 2

#altera uma linha especifica no arquivo       
def alterar_linha(index_linha,nova_linha):
    
    with open('registrado.txt','r') as f:
        texto = f.readlines()
    with open('registrado.txt','w') as f:
        for i in texto:
            if texto.index(i)==index_linha:
                f.write(nova_linha + '\n')
            else:
                f.write(i)

#mostra as caronas que estao atreladas ao perfil
def desejadas(usuario):
    
    k = pesquisa(codigo(usuario), 0)
    j = pesquisa(codigo("usuario"), 0)
    z = set(k) & set(j)
    z = list(z)
    z = int(z[0])
    with open("registrado.txt") as f:
        texto = f.readlines()[z]
    h = show2(texto)    

    return h

#apaga as linhas em branco no arquivo
def linhabranca():
    
    with open("registrado.txt", 'r') as fr:
        lines = fr.readlines()
  
        with open("registrado.txt", 'w') as fw:
            for line in lines:

                if line.strip('\n') != "":
                    fw.write(line)

#abre uma lista de forma específica              
def show(z):
    
    z = str(z)
    y = ""
    i = []
    g = []
    
    for a in z:
        
        if a == "+":
            a = ""
            g.append(y)
            y = ""
            
        y = y + a
        
    g.append(y)
    del g[0]
    del g[-1]
    
    for a in range(len(g)):
    
        i.append(abrir2(str(g[a]))) 
                      
    return i

#abre uma lista de forma específica  
def show3(z):
    
    a = 0
    
    while a < len(z):
        if "+" in z[a]:
            del z[a]
            a = a + 1
        a =  a + 1
        
    i = []
    
    for b in range(len(z)):
        
        i.append(str(abrir2(z[b])))
    
    for a in range(len(i)):
        w = i[a].split("/")
        del w[0]
        o = w[1] + "/" + w[2]
        del w[2]
        w[1] = o
        w = LtoS(w)
        i[a] = w  
                           
    return i    
          
#abre uma lista de forma específica              
def show4(z):
    
    z = str(z)
    y = ""
    i = []
    g = []
    
    for a in z:
        
        if a == "+":
            g.append(y)
            y = ""
            
        y = y + a
        
    g.append(y)
    
    for a in range(len(g)):
    
        i.append(str(g[a]))
                      
    return i

#abre uma lista de forma específica  
def show2(z):
    
    z = str(z)
    y = ""
    i = []
    g = []
    
    for a in z:
        
        if a == "+":
            a = ""
            g.append(y)
            y = ""
            
        y = y + a
        
    g.append(y)
    del g[0]
    del g[-1]
    
    for a in range(len(g)):
    
        i.append(str(g[a]))
                      
    return i

#abre uma lista de forma específica                  
def abrirl(d):
    x = ""
    for a in range(len(d)):
        y = str(a + 1) + "# " + str(d[a]) + "["
        x = x + y
    return x

#transforma uma lista em uma string de formaa específica
def LtoS(a):
    y = ""
    for b in range(len(a)):
        y = y + a[b]
        
    return y

#abre uma lista de forma específica 
def abrir3(f):
    
    f = str(f)
    x = []
    y = ""
    
    for a in f:
        if a == "-":
            a = ""
            x.append(y)
            y = ""
        y = y + a
    x.append(y)
    
    user = str(x[0])

    return user

#pega a data de todas as caronas
def relogio():

    caronas = find("volta") + find("ida")

    linhas = []
    for l in range(len(caronas)):
        d = caronas[l]
        with open("registrado.txt") as f:
            texto = f.readlines()[d]
            linhas.append(texto)

    datas = []
    for a in linhas:
        a = a.split("-")
        if "+" not in a[5]:
            datas.append(a[5].strip())

    return datas

#apaga as caronas que tiveram seus dias passados
def atual():

    datas = relogio()
    tempo = datetime.now()
    diaAtual = tempo.day
    mesAtual = tempo.month

    z = len(datas)
    a = 0
    while a < z:
        x = datas[a].split("/")
        mes = int(x[1])

        if mes > mesAtual:
            del datas[a]
            z = z - 1
            a = a - 1

        a = a + 1
     
    a = 0    
    while a < z:
        x = datas[a].split("/")
        dia = int(x[0])
        mes = int(x[1])

        if mes == mesAtual and dia >= diaAtual:
            del datas[a]
            z = z - 1
            a = a - 1
        a = a + 1
    
    caronas = pesquisa(datas, "sdfdfs")
    
    linhas = []
    for l in range(len(caronas)):
        d = caronas[l]
        with open("registrado.txt") as f:
            texto = f.readlines()[d]
            linhas.append(texto)    
    
    novaslinhas = []
    
    for b in linhas:
        if "+" in b:
            b = b.strip()
            k = b.split("+")
            h = k
            for g in k:
                for t in datas:
                    if t in g:
                        h.remove(g)
            m = ""
            for j in h:
                m = m + j + "+"
                
            m = m[:-1]
            h = m
                
        else:
            h = ""
        
        novaslinhas.append(h)
    
    for c in range(len(novaslinhas)):
        
        alterar_linha(caronas[c], novaslinhas[c])        

#valida uma informação do perfil      
def validar(e):
    erro = espaco(e)
    if erro > 0:
        return erro
    
    e = e.strip()
    acentos = ["á", "é", "í", "ó", 'ú', "â", "ê", "î", "ô", "û", "ã", "õ", 'à', "è", "ì", "ò", "ù"]
    
    for a in acentos:
        if a in e.lower():
            return 1 
        
    e = codigo(e)
    arq = open('registrado.txt') 
    registrados = arq.read()
    
    if e == "" or e in registrados:
        arq.close()
        return 2
    
    else:
        return 0

#valida uma informação do perfil 
def validarsenha(e):
    erro = espaco(e)
    if erro > 0:
        return erro
    
    e = e.strip()
    acentos = ["á", "é", "í", "ó", 'ú', "â", "ê", "î", "ô", "û", "ã", "õ", 'à', "è", "ì", "ò", "ù"]
    
    for a in acentos:
        if a in e.lower():
            return 1 
        
    e = codigo(e)
    arq = open('registrado.txt') 
    registrados = arq.read()
    
    if e == "":
        arq.close()
        return 2
    
    else:
        return 0
    
#verifica se uma string tem espaço  
def espaco(x):
    
    a =  " " in  x
    
    if a:
        return 1
    else:
        return 0

#valida uma informação do perfil 
def validartele(e):
    
    telefone = e
    erro = espaco(e)
    if erro > 0:
        return erro
    
    e = e.strip()
    acentos = ["á", "é", "í", "ó", 'ú', "â", "ê", "î", "ô", "û", "ã", "õ", 'à', "è", "ì", "ò", "ù"]
    
    for a in acentos:
        if a in e.lower():
            return 1 
        
    e = codigo(e)
    arq = open('registrado.txt') 
    registrados = arq.read()
    
    if e == "" or e in registrados:
        arq.close()
        return 2
    
    try:
        int(telefone)
        
    except:
        
        return 3
    
    if len(telefone) != 11:
        return 3            
    
    x = list(telefone)
    x.insert(0, "(")
    x.insert(3, ")")
    y = ""
    for b in range(len(x)):
        y = y + x[b]
        
    return y

#transforma uma informação em numero a partir da função ord
def codigo(u):
    u = u.strip()
    id = []  
    for letra in u:
        x = ord(letra) - 28
        id.append(str(x))
    
    id = "".join(id)
    return id

#verifica se os elementos são diferentes entre si
def diferente(a, b, c, d, e):
    if a == b or a == c or a == d or a == e or b == c or b == d or b == e or c == d or c == e or d == e:
        return 0
    else:
        return 1

#traduz a informação dada pela função codigo
def tradutor(codigo):
    y = 1
    palavra = ""
    x = 0
    letra = [] 
    tudo = []
    for a in codigo:
        if a == "+":
            break
        if a == "-" or a == codigo[-1]:
            tudo.append(palavra)
            palavra = ""
            y = 0
            x = 0
        if y > 0:    
            letra.append(a)
            x = x + 1
        if (x % 2) == 0 and x != 0:
            letra = int((''.join(letra))) + 28
            letra = chr(letra)
            palavra = palavra + letra
            letra = []
            x = 0
        y = 1

    return tudo

#abre uma lista de forma específica 
def abrir(t):
    with open("registrado.txt", 'r') as fp:
        lines = fp.readlines()
        for line in lines:
            if line.find(t) != -1:
                return line

#procura dois elementos em uma lista
def pesquisa(a, b):

    if type(a) != list:
        x = []
        x = find(a)
        
        if b == 0:
            pass
        
        else:
            x = x + find(b)
        
        return x
    
    if type(a) == list:
        y = []
        if b != 0:
            y = find(b)
        
        for t in range(len(a)):
            l = find(a[t])
            
            y = y + l
       
        return y

#procura um elemento em uma lista
def find(a):
    x = []
    with open("registrado.txt", 'r') as fp:

        lines = fp.readlines()
        
        for line in lines:

            if line.find(a) != -1:
                x.append(lines.index(line))           
    return x

#abre uma lista de forma específica       
def abrir2(f):
    
    f = str(f)
    x = []
    
    x = f.split("-")
    
    horas = str(x[3])
    
    horas = horas.split("/")
    h1 = horas[0]
    h2 = horas[-1]
            
    h2 = h2.strip()
    h1 = h1.strip()
    user = str(x[0])
    via = str(x[1])
    via = via.title()
    origens = str(x[2])
    bairros = str(x[4])
    dia = str(x[5])
    
    bairro1 = ""
    bairro2 = ""
    bairro3 = ""

    t = len(bairros.split("_"))

    if t == 3:
        bairro1, bairro2, bairro3 = bairros.split("_")
        
    if t == 2:
        bairro1, bairro2 = bairros.split("_")
        
    if t == 1:
        bairro1 = bairros
        
    bairros = bairro1 + " " + bairro2 + " " + bairro3
    
    origem1 = ""
    origem2 = ""
    origem3 = ""

    t = len(origens.split("_"))

    if t == 3:
        origem1, origem2, origem3 = origens.split("_")
        
    if t == 2:
        origem1, origem2 = origens.split("_")
        
    if t == 1:
        origem1 = origens
        
    origens = origem1 + " " + origem2 + " " + origem3
    
    origens = origens.strip()
    bairros = bairros.strip()
    origens = origens.title()
    bairros = bairros.title()
    dia = dia.strip()
    
    if via == "Volta" and origens == "Qualquer Origem":
        origens = "Qualquer Campus"    
    
    if via == "Ida" and bairros == "Qualquer Destino":
        bairros = "Qualquer Campus"
        
    u = user + " / " + via + " / " + dia + " / " + origens +  " / " + h1 + " até " + h2 +  " / " + bairros
    
    if h1 == "Qualquer Hora 1" and h2 == "Qualquer Hora 2":
        u = user + " / " + via + " / " + dia + " / " + origens +  " / " + "Qualquer Hora" + " / " + bairros
    
    if h1 == h2:
        u = user + " / " + via + " / " + dia + " / " + origens +  " / " + h1 +  " / " + bairros
    
    return u

#valida a hora inserida
def validarhora(f):
    
    if len(f) > 5:
        return int("a")
    
    h = ""
    m = ""
    h, m = f.split(":")
    k = ["00", "05", "10", "15", "20", '25', '30', '35', "40", '45', '50', '55']
 
    if str(m) not in k:
        return int("a")
            
    h = int(h)
    m = int(m)
    
    if h > 24:
        return int("a")
    
    else:
        
        return h, m

#valida a data inserida
def data_valida(d, m):
    
    if d > 31:
        return 0
    
    if m > 12:
        return 0
    
    t = [4, 6, 9, 11]
    
    for b in range(len(t)):
        
        if d > 30 and m == t[b]:
            return 0
        
    h = [1, 3, 5, 7, 8, 10, 12]
    
    for n in range(len(h)):
        
        if d > 31 and m == h[n]:
            return 0
        
    if d > 29 and m == 2:
        return 0
    
    else:
        return 1
    
#formata a data
def formatodata(f):
    
    if len(f) != 5:
        int("a")
        
    d = ""
    m = ""
    
    d, m = f.split("/")
        
    d = int(d)
    m = int(m)
    
    if m > 12:
        int("a")
    
    h = data_valida(d, m)
    
    if h:
        m = str(m)
        d = str(d)
        g = d + "/" + m
        return g
    
    else:
        int("a")
        
#define um periodo entre uma hora e outro   
def formatohora(t1, t2):
    h1, m1 = validarhora(t1)
    h2, m2 = validarhora(t2)
    x = []
    y = ""
    
    if h1 == h2 and m1 == m2:
        return "NT"
    
    elif h1 >= h2 and m1 >= m2:
        print("Resposta inválida de tempo!  ")
        int("a")
    
    if h1 != h2:
        
        while h1 < h2:
            m1 = m1 + 5
            if m1 == 60:
                h1 = h1 + 1
                m1 = "00"
            if m1 == 5:
                m1 = "05"
            x.append(str(h1) + ":" + str(m1))
            m1 = int(m1)
 
    if h1 == h2:
    
        while m1 < int(m2):
            m1 = m1 + 5
            if m1 == 5:
                m1 = "05"
            x.append(str(h1) + ":" + str(m1))
            m1 = int(m1)
               
    for a in range(len(x)):
        if x[a] == x[-1]:
            break
        y = y + str(x[a]) + " / "
        
    y = y.strip()
    y = y[:-1]
    y = y.strip()

    return y

#verifica se o dia é pelo menos atual
def conferirdia(dia):
    
    tempo = datetime.now()
    diaAtual = tempo.day
    mesAtual = tempo.month
    
    d, m = dia.split("/")
    d = int(d)
    m = int(m)
     
    if m < mesAtual:
        
        print("A data precisa ser pelo menos atual")
        return int("a")
    
    elif m == mesAtual and d < diaAtual:
        
        print("A data precisa ser pelo menos atual")
        return int("a")
    
    else:
        pass

#verifica se a hora é pelo menos atual
def conferirhora(hora, data):
    
    if data != 0:
        tempo = datetime.now()
        try:
            validarhora(hora)
        except:
            return 1
        horaatual = tempo.hour - 2
        minutoatual = tempo.minute
        diaAtual = tempo.day
        mesAtual = tempo.month
        d, m = data.split("/")
        h, min = hora.split(":")
        h = int(h) 
        min = int(min)
        d = int(d)
        m = int(m)
        
        if d == diaAtual and m == mesAtual:
            
            if h < horaatual:
                print("A hora pode ser no máximo 2 horas atrás! ")
                return 1
            
            if  horaatual == h and min < minutoatual:
                print("A hora pode ser no máximo 2 horas atrás! ")
                return 1
        
    else:    
        return 0

#formata a hora
def acertar(h):
    
    if h != "":
        h = int(h)
        h = str(h)
        if len(h) < 2:
            h = "0" + h
    else:
        h = ""        
    
    return h

#define um periodo entre uma dia e outro  
def periododia1(dia1, dia2):
        
        d1, m1 = dia1.split("/")
        d2, m2 = dia2.split("/")
        
        if d1 == d2 and m1 == m2:
            return dia1 
        
        elif d1 >= d2 and m1 >= m2:
            return 1
        
        elif m1 == m2 and d1 > d2:
            return 1
        
        d1 = int(d1)
        m1 = int(m1)
        d2 = int(d2)
        m2 = int(m2)
        data3 = []
        data3.append(dia1)
        n = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        while m1 < m2:
            d1 = int(d1)
            d1 = d1 + 1
            a = data_valida(d1, m1)
            
            if a == 0:
                d1 = 1
                m1 = m1 + 1
                
            if d1 in n:
                d1 = str(d1)
                d1 = "0" + d1
            d1 = str(d1)
            
            date = d1 + "/" + str(m1)    
            data3.append(date)
            
        d1 = int(d1)  
          
        while d1 < d2:
            
            d1 = d1 + 1
            
            if d1 in n:
                d1 = str(d1)
                d1 = "0" + d1
                
            d1 = str(d1)
            date = d1 + "/" + str(m1) 
            data3.append(date)
            d1 = int(d1)
            
        return data3    
      
arq.close()  
