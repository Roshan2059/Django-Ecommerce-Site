from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import View
from django.contrib import messages
from .models import *

# Create your views here.
class BaseView(View):
    my_view = {}
    my_view['categories'] = Category.objects.all()
    my_view['brands'] = Brand.objects.all()

class HomeView(BaseView):
    def get(self,request):
        self.my_view['sliders'] = Slider.objects.all()
        self.my_view['ads'] = Ad.objects.all()
        # self.my_view['product'] = Product.objects.all()
        self.my_view['hots'] = Product.objects.filter(labels='hot')
        self.my_view['sales'] = Product.objects.filter(labels='sale')
        self.my_view['news'] = Product.objects.filter(labels='new')
        return render(request,'index.html',self.my_view)

class CategoryView(BaseView):
    def get(self,request,slug):
        ids = Category.onjects.get(slug = slug).id
        self.my_view['catproducts'] = Product.objects.filter(category_id = ids)
        return render(request, 'index.html',self.my_view)


def signup(request):
    if request.method == 'POST':
        username = request.POST['uname']
        email = request.POST['mail']
        passw = request.POST['pass']
        cpass = request.POST['cpass']
        if passw == cpass:
            if User.objects.filter(username = username).exists():
                messages.error(request,'The user name is already taken')
                return redirect('/signup')
            elif User.objects.filter(email = email).exists():
                messages.error(request, 'The email is already taken')
                return redirect('/signup')
            else:
                user = User.objects.create_user(
                    username = username,
                    email = email,
                    password = passw,
                )
                user.save()
        else:
            messages.error(request,'Password doesnot match')
            return redirect('/signup')
    return render(request, 'signup.html')


def reviews(request,slug):
    if request.method == 'POST':
        review = request.POST['review']
        star = request.POST['star']
        slug = request.POST['slug']
        username = request.user.username
        email = request.user.email
        data = Review.objects.create(
            username = username,
            email = email,
            review = review,
            star = star,
            slug = slug
        )
        data.save()
    return redirect(f'/details/{slug}')

class SearchView(BaseView):
    def get(self,request):
        self.my_view
        query = request.GET.get['query']
        if request.method == 'GET':
            if query != "":
                self.my_view['search_product'] = Product.objects.filter(description__icontains = query)
            else:
                return redirect('/')
            return render(request, 'product-list.html', self.my_view)

