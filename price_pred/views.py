from math import exp
from django.shortcuts import render
import numpy as np
from .predictor import predict_price




def predict(request):
    if request.method == 'POST':
        company = request.POST['company']
        type_name = request.POST['typename']
        ram = request.POST['ram']
        weight = request.POST['weight']
        touchscreen= request.POST['Touchscreen']
        ips = request.POST['Ips']
        ppi= None
        cpu = request.POST['cpu']
        hdd = request.POST['hdd']
        ssd = request.POST['ssd']
        gpu = request.POST['gpu']
        os = request.POST['os']
        screen_size = request.POST['Screensize']
        resolution = request.POST['Resolution']


        if touchscreen == 'YES':
            touchscreen = 1
        touchscreen = 0

        if ips == 'YES':
            ips = 1
        ips = 0

        x_res = int(resolution.split('x')[0])
        y_res = int(resolution.split('x')[1])
        ppi = (((x_res**2)+(y_res**2))**0.5)/int(screen_size)

        
        

        
        features = np.array([company,type_name,ram, weight, touchscreen,ips,ppi,cpu, hdd, ssd, gpu, os ])
        
        features= features.reshape(1,12)
        price = predict_price(features)
        
        price = {'price': int(exp(price))}
        print(price)
        return render(request, 'predict.html', price)
    
    else:
        return render(request, 'predict.html')
        
