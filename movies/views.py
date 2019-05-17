import hashlib
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from .models import Movie, Comment
from .forms import CommentForm

# Create your views here.
def list(request):
    # movies = get_list_or_404(Movie)
    # context = {'movies': movies,}
    return render(request, 'movies/index.html')
    
# def listings(request):
#     movies_list = Movie.objects.all()
#     paginator = Paginator(movies_list, 12)
    
#     page = request.GET.get('page')
#     movies = paginator.get_page(page)
#     context = {'movies': movies,}
#     return render(request, 'movies/listings.html', context)
    
def genre_listings(request, genre_pk):
    movies = Movie.objects.filter(genre=genre_pk).all()
    context = {'movies':movies, }
    return render(request, 'movies/listings.html', context)
    
def listings(request):
    movies = Movie.objects.all()
    context = {'movies': movies,}
    return render(request, 'movies/listings.html', context)
    
    
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    
    comment_form = CommentForm()
    context = {'movie': movie, 'comment_form': comment_form,}
    return render(request, 'movies/listing.html', context) # list말고 디테일로 보내야 함

@login_required    
def create_comment(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.movie_id = movie_pk
            comment.user_img = hashlib.md5(request.user.email.strip().lower().encode('utf-8')).hexdigest()
            comment.save()
    return redirect('movies:detail', movie_pk) # list 말고 디테일로 보내야 함
    
@login_required
def update_comment(request, movie_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if comment.user == request.user:
        if request.method == 'POST':
            comment_form = CommentForm(request.POST, instance=comment)
            if comment_form.is_valid():
                comment_form.save()
                return redirect('movies:detail', movie_pk) # list 말고 디테일로 보내야 함
        else:
            comment_form = CommentForm(instance=comment)
        context = {'comment_form': comment_form,}
        return render(request, 'movies/update.html', context) # list 말고 update html 로 보내야 함
    return redirect('movies:detail', movie_pk) # list 말고 디테일로 보내야 함
    
@login_required
def delete_comment(request, movie_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if comment.user == request.user:
        if request.method == 'POST':
            comment.delete()
    return redirect('movies:detail', movie_pk) # list 말고 디테일로 보내야 함

