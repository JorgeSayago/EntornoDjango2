import os

from django.urls import reverse
import pandas as pd
from sklearn.pipeline import Pipeline
from tensorflow.python.keras.models import load_model, model_from_json
from keras import backend as K
import pickle
import keras

class modeloSNN():
    """Clase modelo Preprocesamiento y SNN"""
    #Función para cargar preprocesador
    def cargarPipeline(self,nombreArchivo):
        with open(nombreArchivo+'.pickle', 'rb') as handle:
            pipeline = pickle.load(handle)
        return pipeline
    #Función para cargar red neuronal 
    def cargarNN(self,nombreArchivo):  
        model = keras.models.load_model(nombreArchivo+'.h5')
        print("Red Neuronal Cargada desde Archivo") 
        return model
    #Función para integrar el preprocesador y la red neuronal en un Pipeline
    def cargarModelo(self):
        #Se carga el Pipeline de Preprocesamiento
        nombreArchivoPreprocesador='Recursos/pipePreprocesador'
        pipe=self.cargarPipeline(self,nombreArchivoPreprocesador)
        print('Pipeline de Preprocesamiento Cargado')
        cantidadPasos=len(pipe.steps)
        print("Cantidad de pasos: ",cantidadPasos)
        print(pipe.steps)
        #Se carga la Red Neuronal
        modeloOptimizado=self.cargarNN(self,'Recursos/modeloRedNeuronalBase')
        #Se integra la Red Neuronal al final del Pipeline
        pipe.steps.append(['modelNN',modeloOptimizado])
        cantidadPasos=len(pipe.steps)
        print("Cantidad de pasos: ",cantidadPasos)
        print(pipe.steps)
        print('Red Neuronal integrada al Pipeline')
        return pipe
    #La siguiente función permite predecir si se aprueba o no un crédito a un nuevo cliente. 
    #En la función se define el valor por defecto de las variables, se crea el dataframe con los nuevos valores y 
    #los nombres de las variables. 
    #El método "predict" ejecuta el Pipeline: los pasos de transformación y la clasificación (mediante la red neuronal). 
    #Así se predice si el cliente es bueno (1) o malo (0). 
    def predecirNuevoCliente(self,gender='Female', SeniorCitizen=0, Partner=1, Dependents=0, tenure=12,
                 PhoneService=1, MultipleLines=1, InternetService='Fiber optic', OnlineSecurity=0,
                 OnlineBackup=0, DeviceProtection=0, TechSupport=0, StreamingTV=0,
                 StreamingMovies=0, Contract='Month-to-month', PaperlessBilling=1,
                 PaymentMethod='Electronic check', MonthlyCharges=64, TotalCharges=768):  
        pipe=self.cargarModelo(self)
        cnames=['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure', 'PhoneService', 'MultipleLines',
                'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
                'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod',
                'MonthlyCharges', 'TotalCharges']
        Xnew=[gender,SeniorCitizen,Partner,Dependents
              ,tenure,PhoneService,MultipleLines,InternetService,OnlineSecurity,OnlineBackup,DeviceProtection,TechSupport,StreamingTV,
              StreamingMovies,Contract,PaperlessBilling,PaymentMethod,MonthlyCharges,TotalCharges]
        Xnew_Dataframe = pd.DataFrame(data=[Xnew],columns=cnames)
        print(Xnew_Dataframe)
        pred = (pipe.predict(Xnew_Dataframe) > 0.5).astype("int32")
        print(pred)
        pred = pred.flatten()[0]# de 2D a 1D
        if pred==1:
            pred='se queda'
        else:
            pred='No se queda'
        return pred
    
    #Función para integrar el preprocesador y la red neuronal en un Pipeline
    
    def cargarPipeNB(self):
        try:
            print(" PIPE cargando modelo AHORA  NB NB NB NB ")
            directorio_actual = os.path.abspath(os.path.dirname(__file__))
            #Se carga el Pipeline de Preprocesamiento
            nombreArchivoPreprocesador= os.path.join(directorio_actual, 'Recursos','pipePreprocesador.pickle')
            #nombreArchivoPreprocesador='Recursos/pipePreprocesadores.pickle'
            print(nombreArchivoPreprocesador)
            pipe=self.cargarPipeline(self, nombreArchivoPreprocesador)
            print('Pipeline de Preprocesamiento Cargado')
            cantidadPasos=len(pipe.steps)
            print("Cantidad de pasos: ", cantidadPasos)
            print(pipe.steps)
            cantidadPasos=len(pipe.steps)
            print("Cantidad de pasos: ",cantidadPasos)
            print(pipe.steps)
            print('PIPE PARA NB CARGADO CORRECTAMENTE')
            return pipe
        except FileNotFoundError as e:
            print(f"Error archivo no encontrado: {e.filename}")
        except Exception as e:
            print(f"Error inesperado: {e}")
        return None
    




    print("llego aqui NB Modelo ")
        #Función para integrar el preprocesador y la red neuronal en un Pipeline
    def cargarModeloNB(self):
        try:
            print(" PIPE cargando modelo AHORA  NB  ")
            directorio_actual = os.path.abspath(os.path.dirname(__file__))
            #Se carga el modelo
            modeloOptimizado=self.cargar_naive_bayes(self , os.path.join(directorio_actual, 'Recursos', 'modeloNaiveBayesBase.pkl'))
            #Se integra la Red Neuronal al final del Pipeline
            return modeloOptimizado
        except FileNotFoundError as e:
            print(f"Error archivo no encontrado: {e.filename}")
        except Exception as e:
            print(f"Error inesperado: {e}")
        return None
    




    def predecirNuevoClienteNB(self,gender='Female', SeniorCitizen=0, Partner=1, Dependents=0, tenure=12,
                 PhoneService=1, MultipleLines=1, InternetService='Fiber optic', OnlineSecurity=0,
                 OnlineBackup=0, DeviceProtection=0, TechSupport=0, StreamingTV=0,
                 StreamingMovies=0, Contract='Month-to-month', PaperlessBilling=1,
                 PaymentMethod='Electronic check', MonthlyCharges=64, TotalCharges=768
    ):
        print("NB NB entro el Cliente")

        cnames = ['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure', 'PhoneService', 'MultipleLines',
                'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
                'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod',
                'MonthlyCharges', 'TotalCharges'
    ]


        Xnew=[gender,SeniorCitizen,Partner,Dependents
              ,tenure,PhoneService,MultipleLines,InternetService,OnlineSecurity,OnlineBackup,DeviceProtection,TechSupport,StreamingTV,
              StreamingMovies,Contract,PaperlessBilling,PaymentMethod,MonthlyCharges,TotalCharges]

        pipeNB = modeloSNN.cargarPipeNB(self)

        Xnew_Dataframe = pd.DataFrame(data=[Xnew],columns=cnames)
        #pipe=cargarPipeline("pipePreprocesadores")
        Xnew_Transformado=pipeNB.transform(Xnew_Dataframe)
        modelo=modeloSNN.cargarModeloNB(self)

        y_pred=modelo.predict(Xnew_Transformado)
        predicciones, marcas, certezas= modeloSNN.obtenerResultadosyCertezas(y_pred)
        dataframeFinal_pred=pd.DataFrame({'Resultado':marcas , 'Certeza': certezas})


        resultado = dataframeFinal_pred.to_string(index=False , header=False)

        return resultado