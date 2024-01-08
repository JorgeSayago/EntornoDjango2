from django.shortcuts import render
from appServicioPrediccion.Logica import modeloSNN #para utilizar el método inteligente
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
import json
from django.http import JsonResponse

class Clasificacion():
    def determinarAprobacion(request):
        return render(request, "aprobacionrn.html")
    
    @api_view(['GET','POST'])
    def predecir(request):
        try:
            #Formato de datos de entrada
            GENERO = request.POST.get('gender')
            PERSONAMAYOR = int(request.POST.get('SeniorCitizen'))
            PAREJA = int(request.POST.get('Partner'))
            DEPENDIENTES = int(request.POST.get('Dependents'))
            MESES = int(request.POST.get('tenure'))
            SERVICIOTELEFONICO = int(request.POST.get('PhoneService'))
            LINEASMULTIPLES = int(request.POST.get('MultipleLines'))
            SERVICIOINTERNET = request.POST.get('InternetService')
            SEGURIDADONLINE = int(request.POST.get('OnlineSecurity'))
            COPIASEGURIDAD = int(request.POST.get('OnlineBackup'))
            PROTECCIONDISPOSITIVO = int(request.POST.get('DeviceProtection'))
            SOPORTETECNICO = int(request.POST.get('TechSupport'))
            STREAMINGTV = int(request.POST.get('StreamingTV'))
            STREAMINGMOVIES = int(request.POST.get('StreamingMovies'))
            CONTRATO = request.POST.get('Contract')
            FACTURACIONELECTRONICA = int(request.POST.get('PaperlessBilling'))
            METODOPAGO = request.POST.get('PaymentMethod')
            CARGOSMENSUALES = float(request.POST.get('MonthlyCharges'))
            CARGOSTOTALES = int(request.POST.get('TotalCharges'))
            #Consumo de la lógica para predecir si se aprueba o no el crédito
            resul = modeloSNN.modeloSNN.predecirNuevoCliente(modeloSNN.modeloSNN, gender=GENERO, SeniorCitizen=PERSONAMAYOR, Partner=PAREJA, Dependents=DEPENDIENTES,
                                                             tenure=MESES,PhoneService=SERVICIOTELEFONICO,MultipleLines=LINEASMULTIPLES,InternetService=SERVICIOINTERNET,
                                                             OnlineSecurity=SEGURIDADONLINE,OnlineBackup=COPIASEGURIDAD,DeviceProtection=PROTECCIONDISPOSITIVO,
                                                             TechSupport=SOPORTETECNICO,StreamingTV=STREAMINGTV,StreamingMovies=STREAMINGMOVIES,Contract=CONTRATO,
                                                             PaperlessBilling=FACTURACIONELECTRONICA,PaymentMethod=METODOPAGO,MonthlyCharges=CARGOSMENSUALES,
                                                             TotalCharges=CARGOSTOTALES)
        except Exception as e:
            print(f'Error: {str(e)}')
            resul='Datos inválidos'
        return render(request, "informe.html",{"e":resul})
    
    @api_view(['GET','POST'])
    def predecirNB(request):
        try: 
            #Formato de datos de entrada
            GENERO = request.POST.get('gender')
            PERSONAMAYOR = int(request.POST.get('SeniorCitizen'))
            PAREJA = int(request.POST.get('Partner'))
            DEPENDIENTES = int(request.POST.get('Dependents'))
            MESES = int(request.POST.get('tenure'))
            SERVICIOTELEFONICO = int(request.POST.get('PhoneService'))
            LINEASMULTIPLES = int(request.POST.get('MultipleLines'))
            SERVICIOINTERNET = request.POST.get('InternetService')
            SEGURIDADONLINE = int(request.POST.get('OnlineSecurity'))
            COPIASEGURIDAD = int(request.POST.get('OnlineBackup'))
            PROTECCIONDISPOSITIVO = int(request.POST.get('DeviceProtection'))
            SOPORTETECNICO = int(request.POST.get('TechSupport'))
            STREAMINGTV = int(request.POST.get('StreamingTV'))
            STREAMINGMOVIES = int(request.POST.get('StreamingMovies'))
            CONTRATO = request.POST.get('Contract')
            FACTURACIONELECTRONICA = int(request.POST.get('PaperlessBilling'))
            METODOPAGO = request.POST.get('PaymentMethod')
            CARGOSMENSUALES = float(request.POST.get('MonthlyCharges'))
            CARGOSTOTALES = int(request.POST.get('TotalCharges'))
            #Consumo de la lógica para predecir si se aprueba o no el crédito
            resul = modeloSNN.modeloSNN.predecirNuevoCliente(modeloSNN.modeloSNN, gender=GENERO, SeniorCitizen=PERSONAMAYOR, Partner=PAREJA, Dependents=DEPENDIENTES,
                                                             tenure=MESES,PhoneService=SERVICIOTELEFONICO,MultipleLines=LINEASMULTIPLES,InternetService=SERVICIOINTERNET,
                                                             OnlineSecurity=SEGURIDADONLINE,OnlineBackup=COPIASEGURIDAD,DeviceProtection=PROTECCIONDISPOSITIVO,
                                                             TechSupport=SOPORTETECNICO,StreamingTV=STREAMINGTV,StreamingMovies=STREAMINGMOVIES,Contract=CONTRATO,
                                                             PaperlessBilling=FACTURACIONELECTRONICA,PaymentMethod=METODOPAGO,MonthlyCharges=CARGOSMENSUALES,
                                                             TotalCharges=CARGOSTOTALES)
            
            
        except Exception as e:
            print(f'Error: {str(e)}')
            resul='Datos inválidos'
        return render(request, "informenb.html",{"e":resul})          
    
    @csrf_exempt
    @api_view(['GET','POST'])
    def predecirIOJson(request):
        print(request)
        print('***********************************************')
        print(request.body)
        print('***********************************************')
        body = json.loads(request.body.decode('utf-8'))
        #Formato de datos de entrada
        GENERO = int(body.get("gender"))
        PERSONAMAYOR = int(body.get('SeniorCitizen'))
        PAREJA = int(body.get('Partner'))
        DEPENDIENTES = int(body.get('Dependents'))
        MESES = int(body.get('tenure'))
        SERVICIOTELEFONICO = int(body.get('PhoneService'))
        LINEASMULTIPLES = int(body.get('MultipleLines'))
        SERVICIOINTERNET = str(body.get('InternetService'))
        SEGURIDADONLINE = int(body.get('OnlineSecurity'))
        COPIASEGURIDAD = int(body.get('OnlineBackup'))
        PROTECCIONDISPOSITIVO = int(body.get('DeviceProtection'))
        SOPORTETECNICO = int(body.get('TechSupport'))
        STREAMINGTV = int(body.get('StreamingTV'))
        STREAMINGMOVIES = int(body.get('StreamingMovies'))
        CONTRATO = str(body.get('Contract'))
        FACTURACIONELECTRONICA = int(body.get('PaperlessBilling'))
        METODOPAGO = str(body.get('PaymentMethod'))
        CARGOSMENSUALES = float(body.get('MonthlyCharges'))
        CARGOSTOTALES = int(body.get('TotalCharges'))
        
        print(GENERO)
        print(PERSONAMAYOR)
        print(PAREJA)
        print(DEPENDIENTES)
        print(MESES)
        print(SERVICIOTELEFONICO)
        print(LINEASMULTIPLES)
        print(SERVICIOINTERNET)
        print(SEGURIDADONLINE)
        print(COPIASEGURIDAD)
        print(PROTECCIONDISPOSITIVO)
        print(SOPORTETECNICO)
        print(STREAMINGTV)
        print(STREAMINGMOVIES)
        print(CONTRATO)
        print(FACTURACIONELECTRONICA)
        print(METODOPAGO)
        print(CARGOSMENSUALES)
        print(CARGOSTOTALES)                                


        resul = modeloSNN.modeloSNN.predecirNuevoCliente(modeloSNN.modeloSNN, gender=GENERO, SeniorCitizen=PERSONAMAYOR, Partner=PAREJA, Dependents=DEPENDIENTES,
                                                             tenure=MESES,PhoneService=SERVICIOTELEFONICO,MultipleLines=LINEASMULTIPLES,InternetService=SERVICIOINTERNET,
                                                             OnlineSecurity=SEGURIDADONLINE,OnlineBackup=COPIASEGURIDAD,DeviceProtection=PROTECCIONDISPOSITIVO,
                                                             TechSupport=SOPORTETECNICO,StreamingTV=STREAMINGTV,StreamingMovies=STREAMINGMOVIES,Contract=CONTRATO,
                                                             PaperlessBilling=FACTURACIONELECTRONICA,PaymentMethod=METODOPAGO,MonthlyCharges=CARGOSMENSUALES,
                                                             TotalCharges=CARGOSTOTALES)  
        data = {'result': resul}
        resp=JsonResponse(data)
        resp['Access-Control-Allow-Origin'] = '*'
        return resp
    
    