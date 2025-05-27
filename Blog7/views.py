from django.shortcuts import redirect, render, get_object_or_404
from . models import Posts, Category, Tag, Comment, Contact, Author, Team
from django.core.paginator import Paginator
from django.contrib import messages
# Create your views here.
def home(request):
    recent_posts = Posts.objects.order_by('-id')[:5]
    featured_posts = Posts.objects.filter(category__name='Forex').order_by('-date_posted')[:3]
    category = Category.objects.all()
    latest_posts = Posts.objects.order_by('-date_posted')[:6]
    category_posts= []
    for cat in category:
        post = Posts.objects.filter(category=cat).order_by('-date_posted').first()
        if post:
            category_posts.append(post)

    return render(request, "blog/index.html", {
        'recent_posts': recent_posts,
        'latest_posts': latest_posts,
        'featured_posts': featured_posts,
        'category_posts': category_posts,})

def about(request):
    teams = Team.objects.all()
    return render(request, 'blog/about.html',{
        "teams": teams
    })

    


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        service = request.POST.get('subject')
        message = request.POST.get('message')

        if name and email and phone and service and message:
            contact = Contact.objects.create(
                name = name,
                email = email,
                phone = phone,
                service = service,
                message = message,
            )
            messages.success(request, "Your message has been sent. Thank you!")
            return redirect('contact')
        else:
            messages.error(request, "Please fill in all fields.")
            return redirect('contact')

    return render(request, "blog/contact.html",{
        'contact': Contact,
    })
        
                  


def blog_details(request, pk):
    posts = get_object_or_404(Posts, pk=pk)
    category = Category.objects.all()
    tag = Tag.objects.all()
    recent_posts = Posts.objects.order_by('-id')[:5]
    comments = Comment.objects.filter(posts=posts, parent__isnull=True).order_by('-created_at')

    if request.method =="POST":
        name = request.POST.get('name')
        email= request.POST.get('email')
        website = request.POST.get('website')
        content = request.POST.get('comment')
        parent_id = request.POST.get('parent_id')


        if name and email and content:
            comment = Comment.objects.create(
                posts=posts,
                name=name,
                email=email,
                website=website,
                content=content,
                parent = Comment.objects.get(id=parent_id) if parent_id else None
            )
            return redirect('blog_details', pk=posts.pk)
        
    return render(request, 'blog/blog-details.html',{
        'posts': posts,
        'category': category,
        'tag': tag,
        'recent_posts': recent_posts,
        'comments': comments, 
    })
    

def search_results(request):
    query = request.GET.get('q')
    category_id = request.GET.get('category')
    posts = Posts.objects.all().order_by('-id')

    # if query:
    #     posts= posts.filter(title_icontains=query)

    # if category_id:
    #     posts = posts.filter(category__id=category_id)

    if category_id and query:
        posts = posts.filter(category__id=category_id).filter(tittle_icontains=query)

    paginator = Paginator(posts, 6)
    pageNumber = request.GET.get('page')
    pagObj = paginator.get_page(pageNumber)

    return render(request, 'blog/search-results.html',{
        'query': query,
        'pagObj': pagObj,
        'category_id': category_id,
    })



def category(request):
    posts = Posts.objects.all().order_by('id')
    category = Category.objects.all()
    tag = Tag.objects.all()
    recent_posts = Posts.objects.order_by('-id')[:5]
    paginator =Paginator(posts,6)
    pageNumber = request.GET.get('page')
    pagObj = paginator.get_page(pageNumber)
    return render(request, 'blog/category.html',
                  {'posts': posts,
                  'category': category,
                  'tag': tag,
                  'pagObj': pagObj,
                  'recent_posts': recent_posts,
                  })


def author_profile(request):
    # author = get_object_or_404(Author, pk=pk)
    authors = Author.objects.all()
    return render(request, 'blog/author-profile.html',{
        "authors": authors
    })






def not_found(request):
    return render(request, 'blog/404.html')