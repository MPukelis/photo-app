from django.shortcuts import render
from basic_app.forms import UserForm,UserProfileInfoForm,UserPictureCountForm
from basic_app.models import UserPictureCount



# Extra Imports for the Login and Logout Capabilities
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    count="Failed"
    if request.method == 'POST':
        profile_form = UserProfileInfoForm(data=request.POST)
        print('first if')
    # Check to see both forms are valid
        if profile_form.is_valid():

        # Now we deal with the extra info!
            print('is valid?')
        # Can't commit yet because we still need to manipulate
            profile = profile_form.save(commit=False)

        # Set One to One relationship between
        # UserForm and UserProfileInfoForm
            profile.user = request.user


            pc = UserPictureCount.objects.get(user = request.user)
            count = str(pc.picture_count)


        # Check if they provided a profile picture
            if 'profile_pic' in request.FILES:
                print('found it')

                pc.picture_count -=1
                pc.save()
            # If yes, then grab import osit from the POST form reply
                profile.profile_pic = request.FILES['profile_pic']
                f = request.FILES['profile_pic']
                # for chunk in f.chunks():
                #     path = 'media/'+request.user.username+'/file.png'
                #     if not os.path.exists(path):
                #         os.makedirs(path)
                #     fw=open(path,'wb')
                #     fw.write(chunk)
                #     fw.close()


        # Now save model
                profile.save()

                return render(request,'basic_app/success.html')
        else:
             print('invalid image')
             profile_form = UserProfileInfoForm()



    else:
    # Was not an HTTP post so we just render the forms as blank.
        profile_form = UserProfileInfoForm()
        outofsnaps =""
        if request.user.id:
            try:
                pc = UserPictureCount.objects.get(user_id = request.user.id)
                count = str(pc.picture_count)
                if pc.picture_count == 0:
                    outofsnaps ="Out of Film :("
            except UserPictureCount.DoesNotExist:
                count = '0'
                outofsnaps ="Out of Film :("






# This is the render and context dictionary to feed
# back to the registration.html file page.

    return render(request,'basic_app/index.html',{
    'profile_form':profile_form,
    "pic_count": count,
    "top_up":outofsnaps
    })



@login_required
def special(request):
    # Remember to also set login url in settings.py!
    # LOGIN_URL = '/basic_app/user_login/'
    return HttpResponse("You are logged in. Nice!")

@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('index'))

def register(request):

    registered = False

    if request.method == 'POST':

        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_form = UserForm(data=request.POST)


        #profile_form = UserProfileInfoForm(data=request.POST)

        # Check to see both forms are valid

        if user_form.is_valid(): #and profile_form.is_valid():

            # Save User Form to Database
            user = user_form.save()
            pic_count = UserPictureCount(user = user)
            pic_count.save()

            # Hash the password
            user.set_password(user.password)



            # Update with Hashed password
            user.save()

            # Now we deal with the extra info!

            # Can't commit yet because we still need to manipulate
            #profile = profile_form.save(commit=False)

            # Set One to One relationship between
            # UserForm and UserProfileInfoForm
            #profile.user = user

            # Check if they provided a profile picture
            #if 'profile_pic' in request.FILES:
            #    print('found it')
                # If yes, then grab it from the POST form reply
            #    profile.profile_pic = request.FILES['profile_pic']

            # Now save model
            #profile.save()

            # Registration Successful!
            registered = True

        else:
            #user_form = UserForm()
            # One of the forms was invalid if this else gets called.
            print(user_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()
        #profile_form = UserProfileInfoForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'basic_app/registration.html',
                          {'user_form':user_form,

                           'registered':registered})

def user_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect(reverse('index'))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        return render(request, 'basic_app/login.html', {})
