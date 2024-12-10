from django.shortcuts import render, get_object_or_404
from .models import Trail, Review, Athlete
import random
from django.shortcuts import redirect

def trail_list(request):
    trails = Trail.objects.all()
    random_num1 = random.randint(1, 9)
    random_num2 = random.randint(1, 9)
    random_num3 = random.randint(1, 9)
    context = {
        'trails': trails,
        'random_num1': random_num1,
        'random_num2': random_num2,
        'random_num3': random_num3
    }
    return render(request, 'pages/trail_list.html', context)

def trail_detail(request, trail_id):
    trail = get_object_or_404(Trail, id=trail_id)
    reviews = Review.objects.filter(trail=trail)
    if reviews.exists():
        average_rating = sum(review.rating for review in reviews) / len(reviews)
    else:
        average_rating = None
    return render(request, 'pages/trail_detail.html', {'trail': trail, 'average_rating': average_rating})

def about_page(request):
    return render(request, 'pages/about.html')

def contact_page(request):
    return render(request, 'pages/contact.html')

def admin_page(request):
    return render(request, 'admin.py')


def athlete_detail(request):
    athlete_instance = Athlete.objects.first()  
    return render(request, 'pages/athlete.html', {'athlete': athlete_instance})

def magic(request, num1=None, num2=None, num3=None):
    context = {
        'random_num1': num1,
        'random_num2': num2,
        'random_num3': num3
    }
    return render(request, 'pages/magic.html', context)
def magic1(request):
    random_num1 = random.randint(1, 9)
    random_num2 = random.randint(1, 9)
    random_num3 = random.randint(1, 9)

    
    return redirect('magic', num1=random_num1, num2=random_num2, num3=random_num3)
