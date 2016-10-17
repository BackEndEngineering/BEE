from django.shortcuts import render
from .models import Article, Skill
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

#@login_required
def dashboard(request):

    return render(request, 'Beehive/dashboard.html', context)

def create_user(request):
    if request.method == 'POST':
        caretaker_form = CareTakerForm(request.POST)
        user_form = CreateUserForm(request.POST)
        family_form = CreateFamilyForm(request.POST)
        if user_form.is_valid() and caretaker_form.is_valid() and family_form.is_valid():
            user = user_form.save()
            family = family_form.save()
            phone = caretaker_form.cleaned_data['phone_number']
            relation = caretaker_form.cleaned_data['relation']
            caretaker = CareTaker.objects.create(user=user, family=family, phone_number=phone, relation=relation)
            return HttpResponseRedirect('/login/')
    else:
        caretaker_form = CareTakerForm()
        family_form = CreateFamilyForm()
        user_form = CreateUserForm()


    return render(request, 'MBF/create_user.html',
                 {'caretaker_form': caretaker_form,
                  'user_form': user_form,
                  'family_form': family_form})

def skill(request):
    recent_skills = Skill.objects.order_by('-publish_date')[:10]
    context = {'recent_skills': recent_skills}
    return render(request, 'Beehive/skill.html', context)

def view_skill(request, skill_id):

    try:
        skill = Skill.objects.get(pk=skill_id)
    except Skill.DoesNotExist:
        raise Http404("No such skill!")

    return render(request, 'Beehive/skills.html', context)



def index(request):
    recent_articles = Article.objects.order_by('-publish_date')[:10]
    context = {'recent_articles': recent_articles}
    return render(request, 'Beehive/index.html', context)

def view_article(request, article_id):

    try:
        article = Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        raise Http404("No such article!")

    return render(request, 'Beehive/articles.html')

def home(request):
    context = {}
    return render(request, 'Beehive/home.html', context)
