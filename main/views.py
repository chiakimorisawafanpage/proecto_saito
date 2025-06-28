from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .models import ContactMessage 

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Спасибо, ваше сообщение отправлено!')
            return redirect('index')
        else:
            messages.error(request, 'Ошибка при отправке формы.')
    else:
        form = ContactForm()

    # Получаем все сообщения только для админа
    all_messages = ContactMessage.objects.order_by('-created_at')
    return render(request, 'main/index.html', {
        'form': form,
        'all_messages': all_messages
    })

def messages_view(request):
    if not request.user.is_superuser:
        return redirect('index')
    
    all_messages = ContactMessage.objects.order_by('-created_at')
    return render(request, 'main/messages.html', {'all_messages': all_messages})
