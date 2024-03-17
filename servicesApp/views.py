from django.shortcuts import render,redirect
from django.urls import reverse
from servicesApp.models import EventPost,Booking
from django.views.decorators.http import require_POST,require_http_methods
from .forms import RegistrationForm,LoginForm,ServicesPostForm,ServicesPostFormUpadte,bookingForm
from .models import User,ServicePostByUser
import logging
from django.http import  JsonResponse
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib.auth import authenticate, login,logout
logger = logging.getLogger(__name__)
from django.contrib import messages
from django.shortcuts import get_object_or_404
import json
from django.views.decorators.csrf import csrf_protect

def services(request):
    user_service_posts = ServicePostByUser.objects.all()[:10]
    return render(request, 'pages/services.html',{'user_service_posts': user_service_posts})

def index(request):
    if request.method == 'POST':
        form = bookingForm(request.POST)
        if form.is_valid():
            try:
                # Extract form data
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                contact_number = form.cleaned_data['contact_number']
                other_description = form.cleaned_data['other_description']
                user_id = request.POST.get('user_id')  # Extract user_id from request.POST
                service_post_id = request.POST.get('service_post_id')  # Extract service_post_id from request.POST
                
                # Save data to the database or perform other actions
                user = Booking.objects.create(user_id=user_id,service_post_id=service_post_id,email=email, other_description=other_description, name=name, contact_number=contact_number)

                
                return JsonResponse({'success': True, 'message': 'Booking added successfully.'})
            except Exception as e:
                return JsonResponse({'success': False, 'message': str(e)}, status=500)
        else:
            errors = dict([(field, error[0]) for field, error in form.errors.items()])
            return JsonResponse({'success': False, 'errors': errors}, status=400)
    else:
        user_service_posts = ServicePostByUser.objects.all()[:10]
        form = bookingForm()
        return render(request, 'pages/home.html', {'form': form, 'user_service_posts': user_service_posts})
    
    
def register(request):
    if request.method == 'POST' :
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Process the form data
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            contact_number = form.cleaned_data['contact_number']
            try:
                # Insert into your model create_user perform other actions as needed
                user = User.objects.create_user(email=email, password=password, full_name=full_name, contact_number=contact_number)
                # Redirect to profile page after successful registration
                return JsonResponse({'success': True}) 
            except IntegrityError:
                # Email already exists, provide error message to user
                return JsonResponse({'errors': {'email': ['Email already exists.']}}, status=400)
            except Exception as e:
                # Handle other exceptions
                return JsonResponse({'errors': {'general': ['An internal error occurred. Please contact the administrator.']}}, status=500)
        else:
            errors = dict([(field.name, field.errors) for field in form])
            return JsonResponse({'errors': errors}, status=400)
    else:
        form = RegistrationForm()
    return render(request, 'pages/register.html', {'form': form})


def postServices(request):
    return render(request, 'pages/postServices.html')

def loginUser(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # Authenticate user
            user = authenticate(request, email=email, password=password)
        
            if user is not None:
                # If authentication succeeds, log the user in
                login(request, user)
                # Redirect the user to the profile page or any other page
                return JsonResponse({'success': True})  # Assuming 'profile' is the name of the URL pattern for the profile page
            else:
                # If authentication fails, add an error message and render the login page again
                messages.error(request, 'Invalid email or password.')
                return JsonResponse({'errors': {'general': ['Invalid email or password.']}})
        else:
            # If form is not valid, return form errors
            errors = dict([(field.name, field.errors) for field in form])
            return JsonResponse({'errors': errors}, status=400)
    else:
        # For GET requests, initialize an empty form
        form = LoginForm()
    return render(request, 'pages/login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('index') 

@login_required
def profile(request):
    user = request.user
    form = ServicesPostForm()
    formUpadte=ServicesPostFormUpadte()
    user_service_posts = ServicePostByUser.objects.filter(user=user)
    BookingUser = Booking.objects.filter(user=user)
    return render(request, 'pages/profile.html', {'user': user, 'form': form,'user_service_posts':user_service_posts,'formUpadte':formUpadte,'BookingUser':BookingUser})

@csrf_protect
def addPost(request):
    if request.method == 'POST':
        user = request.user
        form = ServicesPostForm(request.POST, request.FILES)
        if form.is_valid():
            # Extract form data
            name = form.cleaned_data['name']
            category = form.cleaned_data['category']
            description = form.cleaned_data['description']
            experience = form.cleaned_data['experience']
            available_date = form.cleaned_data['available_date']
            open_to_work = form.cleaned_data.get('open_to_work', False)
            email = form.cleaned_data['email']
            contact_number = form.cleaned_data['contact_number']
            per_hour_rate = form.cleaned_data['per_hour_rate']
            service_img = form.cleaned_data['service_img']

            # Create and save model instance
            service_post = ServicePostByUser.objects.create(
                user=user,
                name=name,
                category_name=category,  # Make sure this field matches your model
                description=description,
                experience=experience,
                available_date=available_date,
                open_to_work=open_to_work,
                email=email,
                contact_number=contact_number,
                per_hour_rate=per_hour_rate,
                service_img=service_img
            )

           
            # Redirect the user to a success page
            return JsonResponse({'success': True,"message":"Post are upload seccufully"}) 
        
        else:
             errors = dict([(field.name, field.errors) for field in form])
             return JsonResponse({'errors': errors}, status=400)
    else:
        # Handle other HTTP methods if needed
        return JsonResponse({'error': 'Method not allowed'}, status=405)
        
def errorPage(request):
    return render(request, 'pages/404Page.html')

@require_POST
def delete_post(request):
    post_id = request.POST.get('post_id')
    try:
        post_to_delete = ServicePostByUser.objects.get(pk=post_id)
        post_to_delete.delete()
        
        return JsonResponse({'success': True})
    except ServicePostByUser.DoesNotExist:
        return JsonResponse({'error': 'Service post does not exist'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    
def get_post(request):
    if request.method == 'GET':
        service_post_id = request.GET.get('service_post_id')
        service_post = get_object_or_404(ServicePostByUser, pk=service_post_id)
        data = {
            'id':service_post_id,
            'name': service_post.name,
            'category_name': service_post.category_name,
            'experience': service_post.experience,
            'description': service_post.description,
            'available_date': service_post.available_date,
            'email': service_post.email,
            'contact_number': service_post.contact_number,
            'per_hour_rate': service_post.per_hour_rate,
            # Add other fields as needed
        }
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)






@csrf_protect    
@require_POST
def update_service_post(request):
    try:
        # Retrieve form data
        post_id = request.POST.get('id')
        name = request.POST.get('name')
        category_name = request.POST.get('category_name')
        description = request.POST.get('description')
        experience = request.POST.get('experience')
        available_date = request.POST.get('available_date')
        email = request.POST.get('email')
        contact_number = request.POST.get('contact_number')
        per_hour_rate = request.POST.get('per_hour_rate')

        # Retrieve the object from the database
        service_post = ServicePostByUser.objects.get(pk=post_id)

        # Update the object with the new values
        service_post.name = name
        service_post.category_name = category_name
        service_post.description = description
        service_post.experience = experience
        service_post.available_date = available_date
        service_post.email = email
        service_post.contact_number = contact_number
        service_post.per_hour_rate = per_hour_rate

        # Check if a file was uploaded
        if 'service_img' in request.FILES:
            service_img = request.FILES['service_img']
            service_post.service_img = service_img

        # Save the updated object
        service_post.save()

        # Return a success response
        return JsonResponse({'success': True})

    except ServicePostByUser.DoesNotExist:
        return JsonResponse({'error': 'Service post not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)