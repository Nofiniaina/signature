import os
from django.shortcuts import render
import json

def register_user(username, public_key):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    registration_file_path = os.path.join(current_dir, "../json_data/registration.json")

    try:
        with open(registration_file_path, "r") as registration_file:
            data = json.load(registration_file)
    except (json.JSONDecodeError, FileNotFoundError):
        data = {}
    
    user_registration = {}
    user_registration[username] = public_key
    data.update(user_registration)

    with open(registration_file_path, "w") as registration_file:
        json.dump(data, registration_file, indent=4)

def register(request):

    if(request.method == 'POST'):
        username = request.POST.get('username')
        file = request.FILES.get('file')
        if username and file:
            if(file.name.endswith('.pem')):
                filename = f"{username}.pem"
                register_user(username, filename)

    return render(request, 'register/register.html') 