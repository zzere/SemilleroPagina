import pandas as pd

class Pregunta:
    def __init__(self,letra,n,rspP,pBis,discrim,lower,mid50,mid75,upper,correcta):
        self.letra = letra
        self.n = n
        self.rspP = rspP
        self.pBis = pBis
        self.discrim = discrim
        self.lower = lower
        self.mid50 = mid50
        self.mid75 = mid75
        self.upper = upper
        self.correcta = correcta

    @staticmethod
    def correcta(correcta):
        return True if correcta == "*" else False
        
    def __str__(self):
        return f"{self.correcta} {self.letra} {self.n} {self.rspP} {self.pBis} {self.discrim} {self.mid50} {self.mid75} {self.upper} \n"
    
    def __repr__(self):
        return f"{self.correcta} {self.letra} {self.n} {self.rspP} {self.pBis} {self.discrim} {self.mid50} {self.mid75} {self.upper} \n"


class Item:
    def __init__(self,numero_item,preguntas):
        self.numero_item = numero_item
        self.preguntas = preguntas
    
    @staticmethod
    def primera_P(i,key):
        return key if i != 0 else "P1"
    
    def preguntaCorrecta(self):
        for i in range(len(self.preguntas)):
            if self.preguntas[i].correcta:
                correcta = self.preguntas[i]
                break
            else:
                correcta = "no se encuentra pregunta correcta"
        return correcta
        
    
    def __str__(self):
        return f"{self.numero_item}\n{self.preguntas}"

    def __repr__(self):
        return f"{self.numero_item}\n{self.preguntas}"
    

class Csv:
    def __init__(self,uArchivo):
        self.uArchivo = uArchivo
        self.df = None
        self.items = []

    
    def crearDf(self):
        self.df = pd.read_csv(self.uArchivo)


    def skiprows(self):
        i = 0
        while self.df.shape[1] <= 2:
            i+=1
            self.df = pd.read_csv(self.uArchivo, skiprows=i)

    def iniciar(self):
        self.crearDf()
        self.skiprows()
        self.list_Items()

    
    def nombreItems(self):
        nombres = []
        for i in self.items:
            nombres.append(i.numero_item)
        
        return nombres
    
    def colores(self, valor):
        colores = []
        valorMinimo = 0
        valores = self.valoresPreguntasC(valor)
        for i in valores:
            if float(i) <= valorMinimo:
                colores.append('rgba(175, 6, 6, 1)') 
            else:
                colores.append('rgba(54, 162, 235, 1)')
            
        return colores
    
    def valoresPreguntasC(self, valor):
        # Mapeo de valores a atributos
        atributos = {
            'n': 'n',
            'rspP': 'rspP',
            'pBis': 'pBis',
            'discrim': 'discrim',
            'lower': 'lower',
            'mid50': 'mid50',
            'mid75': 'mid75',
            'upper': 'upper'
        }

        # Verificar si el valor está en el diccionario
        if valor in atributos:
            # Utilizar list comprehension para obtener los valores
            valores = [getattr(i.preguntaCorrecta(), atributos[valor]) for i in self.items]
            return valores
        else:
            return 'valor invalido'        

    def list_Items(self):
        for i in range(self.df.shape[0]):   
            #si encuentra la letra "A" crea un dataframe el cual va a ser un nuevo itetm.
            if self.df.iloc[i,1] == "A":        #i representa las filas y el 1 es el numero de columna donde se encuentran las letras de las preguntas    

                data = self.df.iloc[i:(i+4)]    #el 4 representa el numero de preguntas (A, B, C, D) 4 preguntas en total, asumiendo que son solo 4 preguntas 

                preguntas = []                  
                for j in range(data.shape[0]):  
                    #j representa el numero de preguntas del item 
                    p = Pregunta(data.iloc[j,1],              #define la letra de la pregunta j
                           data.iloc[j,2],              #define n de la pregunta j
                           data.iloc[j,3],              #define el rspP de la pregunta j
                           data.iloc[j,4],              #define el pBis de la pregunta j
                           data.iloc[j,5],              #define el discriminante de la pregunta j
                           data.iloc[j,6],              #define el lower de la pregunta j
                           data.iloc[j,7],              #define el mid50 de la pregunta j
                           data.iloc[j,8],              #define el mid75 de la pregunta j
                           data.iloc[j,9],              #define el upper de la pregunta j
                           Pregunta.correcta(data.iloc[j,0])) #define si la pregunta j es correcta o no
                    preguntas.append(p)     #se agrega la pregunta y se repite de ser necesario debido al for

                #se crea un objeto item al cual se le definen las preguntas
                itm = Item(Item.primera_P(i,self.df.iloc[(i-2),1]),preguntas)
                #it.primera_P comprueba si es la primera pregunta, de ser asi se asigna "P1" como nombre del item
                #"(i-2),1" reprenta la posicion del nombre del item, asumiendo que esta 2 posiciones arriba de la pregunta "A"
                self.items.append(itm)

