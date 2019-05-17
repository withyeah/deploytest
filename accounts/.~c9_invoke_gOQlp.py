import hashlib
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .models import Profile
from movies.models import Movie, Comment, Genre
from .forms import UserCustomChangeForm, ProfileForm, UserCustomCreationForm



# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect('movies:list')
      
    if request.method == 'POST':
        form = UserCustomCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            auth_login(request, user)
            return redirect('movies:list')
    else:
        form = UserCustomCreationForm()
    context = {'form': form}
    return render(request, 'accounts/signup.html', context)
    


def login(request):
    if request.user.is_authenticated:
        return redirect('movies:list')
        
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.POST.get('next') or 'movies:list')
    
    else:
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)
    
def logout(request):
    auth_logout(request)
    return redirect('movies:list')

def people(request, username):
    # if request.user.is_authenticated:
    #     gravatar_url = hashlib.md5(request.user.email.strip().lower().encode('utf-8')).hexdigest()
    # else:
    #     gravatar_url = None # 변수 선언은 해야하니까 None 값을 할당.
    
    people = get_object_or_404(get_user_model(), username=username)
    gravatar_url = hashlib.md5(people.email.strip().lower().encode('utf-8')).hexdigest()
    
    # 추천
    user_comment = Comment.objects.filter(user=request.user).order_by('-score').values_list('movie', flat=True).distinct()[:1]
    if user_comment:
        movie_genre = Movie.objects.filter(pk=user_comment[0]).order_by('pk').values_list('genre', flat=True).distinct()
        recommend_movies = Movie.objects.filter(genre=movie_genre[0]).all()[:10]
        recommend_genre = Genre.objects.filter(pk=movie_genre[0]).all()
    
    
    
    
    
        context = {
            'people':people,
            'gravatar_url': gravatar_url,
            'recommend_movies': recommend_movies,
            'movie_genre':recommend_genre[0],
        }
        return render(request, 'accounts/profile.html', context)
    else:
        context = {
            'people':people,
            'gravatar_url': gravatar_url,

        }
        return render(request, 'accounts/profile.html', context)
    
# @require_POST
@login_required 
def update(request):
    if request.method == 'POST':
        user_change_form = UserCustomChangeForm(request.POST, instance = request.user)
        if user_change_form.is_valid():
            user_change_form.save()
            return redirect('people', request.user.username)
        
        
    else:
        user_change_form = UserCustomChangeForm(instance = request.user)
        
    context={
        'user_change_form':user_change_form,
    }
    return render(request, 'accounts/update.html', context)
    
@login_required 
def delete(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
    return redirect('movies:list')
    
@login_required 
def password(request):
    if request.method == "POST":
        password_change_form = PasswordChangeForm(user=request.user, data=request.POST)
        if password_change_form.is_valid():
            user = password_change_form.save()
            update_session_auth_hash(request, user)
            return redirect('movies:list')
            
    else:
        password_change_form = PasswordChangeForm(request.user)
    context = {
        'password_change_form':password_change_form,
    }
    return render(request, 'accounts/password.html', context)
    

@login_required
def profile_update(request):
    profile = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('people', request.user.username)
    else:
        profile_form = ProfileForm(instance=request.user.profile)
    context = {'profile_form': profile_form,}
    return render(request, 'accounts/profile_update.html', context)
    
@login_required
def follow(request, user_pk):
    people = get_object_or_404(get_user_model(), pk=user_pk)
    if request.user in people.followers.all():
        people.followers.remove(request.user)
    else:
        people.followers.add(request.user)
    return redirect('people', people.username)
    





