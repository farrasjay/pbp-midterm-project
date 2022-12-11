from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from faq.models import Question, QuestionForm
from faq.forms import SendQuestionForm
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

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

def set_session(request, id):
    recently_viewed_question = None
    if 'recently_viewed_ques' in request.session:
        if id in request.session['recently_viewed_ques']:
            request.session['recently_viewed_ques'].remove(id)
        else:
            request.session['recently_viewed_ques'].insert(0, id)
        recently_viewed_question = list(request.session['recently_viewed_ques'])
    else:
        request.session['recently_viewed_ques'] = [id]
        recently_viewed_question = list(request.session['recently_viewed_ques'])


    request.session.modified = True
    context = {
        'recently_viewed_question': recently_viewed_question
    }
    # return render(request, 'faq.html', context)
    return JsonResponse(context)

def get_session(request):
    if 'recently_viewed_ques' in request.session:
        recently_viewed_question = list(request.session['recently_viewed_ques'])
    else:
        recently_viewed_question = None
    context = {
        'recently_viewed_question': recently_viewed_question
    }
    return JsonResponse(context)

@csrf_exempt
def like_unlike_post(request, id):
    user = request.user
    if request.method == 'POST':
        if request.user.is_authenticated:
            question_obj = Question.objects.get(id=id)
            
            if user in question_obj.liked.all():
                question_obj.liked.remove(user)
                question_obj.num_liked = question_obj.num_liked -1
            else:
                question_obj.liked.add(user)
                question_obj.num_liked = question_obj.num_liked +1

            question_obj.save()
            return redirect('faq:faq')
    print("TIDAK BISA YA HEHE")
    return redirect('faq:faq')

@csrf_exempt
def send_question(request):
    form = SendQuestionForm()
    context = ""
    if request.method == "POST":
        question = request.POST.get("question")
        if(question!=context and request.user!=None):
            user = request.user
            new_data = QuestionForm(user_form=user, question_in_form=question)
            new_data.save()
            context = {
            'question': question
            }
            return JsonResponse(context)

    return  redirect("faq:faq")

def get_json(request):
    
    faq_json = serializers.serialize("json", Question.objects.all())
    
    return HttpResponse(faq_json, content_type="application/json")

def get_status_json(request):
    user = request.user
    user_json = user.id
    status_user = False
    
    if request.user.is_authenticated:
        status_user = True
    
    context = {
    'status_user' : status_user,
    'user': user_json
    }
    return JsonResponse(context)

