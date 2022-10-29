from django.shortcuts import render
from django.urls import reverse
from django.core import serializers
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from faq.models import Question, Like

# @login_required(login_url='/uhealths/login/')
def show_faq_page(request):
    data_faq = Question.objects.all()
    status_user = False
    user = request.user
    if request.user.is_authenticated:
        status_user = True
    context = {
    'data_faq': data_faq,
    'status_user' : status_user,
    'user': user
    }
    return render(request, "faq.html", context)



# def like_card(request, id):
#     question = Question.objects.get(id=id)
#     question.liked = question.liked + 1
#     question.save()
#     return redirect('faq:faq')


def like_unlike_post(request):
    user = request.user
    if request.method == 'POST':
        if request.user.is_authenticated:
            
            question_id = request.POST.get('post_id')
            question_obj = Question.objects.get(id=question_id)
            

            if user in question_obj.liked.all():
                question_obj.liked.remove(user)
                question_obj.num_liked = question_obj.num_liked -1
            else:
                question_obj.liked.add(user)
                question_obj.num_liked = question_obj.num_liked +1

            
            question_obj.save()
            # data = {
            #     'value': like.value,
            #     'likes': post_obj.liked.all().count()
            # }

            # return JsonResponse(data, safe=False)
            return redirect('faq:faq')

    return redirect('faq:faq')