from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from berita.forms import ChoiceCheckForm
import random

def index(request):
    print(request.POST)
    choices = ['rock','paper','scissors']
    if request.POST:
        print("###################")
        form = ChoiceCheckForm(request.POST)
        choice = dict(request.POST)['choice'][0]
        your_choice = choice
        title = choice + " is clicked"
        computer_choice = random.choice(choices)
        if computer_choice == choice:
            result = "Draw"
        else:
            if (computer_choice == "rock" and your_choice == "scissors") or \
               (computer_choice == "paper" and your_choice == "rock") or \
               (computer_choice == "scissors" and your_choice == "paper"):
                result = "Computer won"
            else:
                result = "You Won"
        variables = {
            'form': form, 'title': title, 'result': result, 
            'computer_choice': "Computer chose : " + computer_choice}
        return render(request=request, template_name='result.html', context=variables)
    else:
        form = ChoiceCheckForm()
        print(")))))))))))))")
        title = None
        variables = {'form': form, 'title': title}
        return render(request=request, template_name='index.html', context=variables)