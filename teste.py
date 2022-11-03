from app import * 

def teste():
    
    
    usuario = "?caio?"
    
    
    if request.method == 'POST':
        if request.form['botao'] == 'Enviar':
            
            
            
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
        
        return 0      
    

teste()