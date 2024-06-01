import sys
import os
import py_compile

def timelimit(timeout, func, args=(), kwargs={}):
    import threading
    class FuncThread(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)
            self.result = None
        def run(self):
            self.result = func(*args, **kwargs)
    it = FuncThread()
    it.start()
    it.join(timeout)
    if it.is_alive():
        return "\nIl tuo programma sta eseguendo un ciclo infinito.\nPer ucciderlo non basta premere invio\n devi chiudere la finesta con il mouse"
    else:
        return it.result
  
f=open("config.txt","r", encoding="UTF8")
for i in range(6):
    s=f.readline().strip()
if s != "NoHelperModules":
    exec("import " + s)
for i in range(2):
    s=f.readline().strip()
try:    
    print("Compilo ",s)
    print("--------------------------------------------")
    print("========================")
    py_compile.compile(s,doraise=True)
except py_compile.PyCompileError:
    tb=sys.exc_info()[2]
    tbb=tb.tb_next
    tbbb=tbb.tb_next
    print("Si è verificato un errore di compilazione")
    #print(sys.exc_info()[0])
    print(sys.exc_info()[1])
    tb=sys.exc_info()[2]
    h=input("Premere invio per terminare...")
    sys.exit()
try:
    exec("import "+s[0:len(s)-3])
    metodoStu=s[0:len(s)-3]
    s=f.readline().strip()
    s=f.readline().strip()
    metodiStudente = []
    metodiStudente.append(metodoStu+"."+s.split(",")[0])
    metodiStudente.append(metodoStu+"."+s.split(",")[1])
    metodiStudente.append(metodoStu+"."+s.split(",")[2])
    metodiStudente.append(metodoStu+"."+s.split(",")[3])
    metodiStudente.append(metodoStu+"."+s.split(",")[4])
    metodiStudente.append(metodoStu+"."+s.split(",")[5])
    metodiStudente.append(metodoStu+"."+s.split(",")[6])
    commandTraduttore="traduttore=Es10.Traduttore()"
    commandTraduttore1="traduttore.inserisci(\"ciao\",\"hello\")"
    commandTraduttore2="traduttore.inserisci(\"macchina\",\"car\")"
    commandTraduttore3="traduttore.inserisci(\"cane\",\"dog\")"
    print("Dizionario IT <--> EN:")
    print("ciao <--> hello")
    print("macchina <--> car")
    print("cane <--> dog")
    print("--------------------------------------------")
    exec(commandTraduttore)
    exec(commandTraduttore1)
    exec(commandTraduttore2)
    exec(commandTraduttore3)
    
    while s[0]!="(":
        s=f.readline().strip()
    i=1
    errori=0
    contatore = 0
    while len(s)>0:
        coppiaInputRisultato = s.strip().split("-->") #FL COPIA INPUT RISULTATO
        print("========================")
        #print(metodoStu[6:]+coppiaInputRisultato[0]) #ELIMINATO SA
        if(contatore == 0):
            print(metodiStudente[0].split(".")[1]+coppiaInputRisultato[0])
            nomeFile = metodiStudente[0].split(".")[0]
            nomeMetodo = metodiStudente[0].split(".")[1]
            command="stu=timelimit(3,traduttore."+nomeMetodo+",["+coppiaInputRisultato[0][1:-1]+"])"
        elif(contatore == 1):
            print(metodiStudente[1].split(".")[1]+coppiaInputRisultato[0])
            nomeFile = metodiStudente[1].split(".")[0]
            nomeMetodo = metodiStudente[1].split(".")[1]
            command="stu=timelimit(3,traduttore."+nomeMetodo+",["+coppiaInputRisultato[0][1:-1]+"])"
        elif(contatore == 2):
            print(metodiStudente[2].split(".")[1]+coppiaInputRisultato[0])
            nomeFile = metodiStudente[2].split(".")[0]
            nomeMetodo = metodiStudente[2].split(".")[1]
            command="stu=timelimit(3,traduttore."+nomeMetodo+",["+coppiaInputRisultato[0][1:-1]+"])"
        elif(contatore == 3):
            print(metodiStudente[3].split(".")[1]+coppiaInputRisultato[0])
            nomeFile = metodiStudente[3].split(".")[0]
            nomeMetodo = metodiStudente[3].split(".")[1]
            command="stu=timelimit(3,traduttore."+nomeMetodo+",["+coppiaInputRisultato[0][1:-1]+"])"
        elif(contatore == 4):
            print(metodiStudente[4].split(".")[1]+coppiaInputRisultato[0])
            nomeFile = metodiStudente[4].split(".")[0]
            nomeMetodo = metodiStudente[4].split(".")[1]
            command="stu=timelimit(3,traduttore."+nomeMetodo+",["+coppiaInputRisultato[0][1:-1]+"])"
        elif(contatore == 5):
            print(metodiStudente[5].split(".")[1]+coppiaInputRisultato[0])
            nomeFile = metodiStudente[5].split(".")[0]
            nomeMetodo = metodiStudente[5].split(".")[1]
            command="stu=timelimit(3,traduttore."+nomeMetodo+",["+coppiaInputRisultato[0][1:-1]+"])"
        elif(contatore == 6):
            print(metodiStudente[6].split(".")[1]+coppiaInputRisultato[0])
            nomeFile = metodiStudente[6].split(".")[0]
            nomeMetodo = metodiStudente[6].split(".")[1]
            command="stu=timelimit(3,traduttore."+nomeMetodo+",["+coppiaInputRisultato[0][1:-1]+"])"
        
        print("========================")
        #exec("doc="+metodoDoc+s) #ELIMINATO FL
        exec("doc="+coppiaInputRisultato[1]) #FL RISULTATO GIUSTO
        print("Il risultato giusto:",doc,"\n***********")    
        exec(command)
        print("Il tuo risultato:",stu,"\n***********")
        if stu==doc:
            print("Il tuo risultato è giusto!")
        else:
           print("Il tuo risultato è sbagliato!")
           errori=errori+1
        print("--------------------------------------------")   
        s=f.readline().strip()
        i=i+1
        contatore+=1
    if errori>0:
        print("ATTENZIONE !!!! Il tuo metodo ha fallito ",errori, " volte")
    else:
        print("CONGRATULAZIONI!!! Il tuo programma ha superato tutti i test")
    
except BaseException:
    tb=sys.exc_info()[2]
    tbb=tb.tb_next
    tbbb=tbb.tb_next
    print("Durante l'esecuzione del tuo codice")
    print("si è verificato un errore alla linea:", tbbb.tb_lineno)
    #print(sys.exc_info()[0])
    print(sys.exc_info()[1])
    tb=sys.exc_info()[2]
    
h=input("Premere invio per terminare...")     
