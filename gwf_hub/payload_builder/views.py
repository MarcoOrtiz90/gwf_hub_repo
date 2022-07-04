from django.shortcuts import render

def payloadBuilder(request):
    if request.method == 'post':
        if request.POST.get('buildPayload'):
            inputs = request.POST
            iterationCount = inputs['builderIterations']
            iteration = 1
            categories = ['string', 'step', 'answer']
            currentMain = ''
            export = ''
            while iteration <= iterationCount:                
                for category in categories:                    
                    if category is "string" :
                        loopData = ''

    return render(request, 'builder.html')
