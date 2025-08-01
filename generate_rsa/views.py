from django.shortcuts import render
import os

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def generate_rsa_key(request):
    """
    Render the RSA key generation page.
    """

    if(request.method == 'POST'):
        username = request.POST.get('username')

        # Create user directory in project_data folder
        user_dir = os.path.join('project_data', username)
        os.makedirs(user_dir, exist_ok=True)

        private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        pem_private_format = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )

        # Save private key in user's folder
        private_key_path = os.path.join(user_dir, f'{username}_private_key.pem')
        with open(private_key_path, 'wb') as f:
            f.write(pem_private_format)

        public_key = private_key.public_key()
        pem_public_format = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

        # Save public key in user's folder
        public_key_path = os.path.join(user_dir, f'{username}_public_key.pem')
        with open(public_key_path, 'wb') as f:
            f.write(pem_public_format)

    return render(request, 'generate_rsa.html')