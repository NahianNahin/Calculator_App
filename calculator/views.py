from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    return render(request, 'calculator.html')
def contact(request):
    return render(request, 'contact.html')
def about(request):
    return render(request, 'about.html')

def calculate(request):
    if request.method == 'POST':
        try:
            num1 = float(request.POST.get('num1', 0))
            num2 = float(request.POST.get('num2', 0))
            operation = request.POST.get('operation', '')
            result = None

            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'multiply':
                result = num1 * num2
            elif operation == 'divide':
                result = num1 / num2 if num2 != 0 else 'Error: Division by zero'
            
            return JsonResponse({'result': result})
        except Exception as e:
            return JsonResponse({'error': str(e)})

    return JsonResponse({'error': 'Invalid request'})
