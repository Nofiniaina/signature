from django.shortcuts import render
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from datetime import datetime
import hashlib
import os
import base64
import json

def save_signature(username, signature):
    user_dir = os.path.join('sig_data', username)
    os.makedirs(user_dir, exist_ok=True)

    signature_path = os.path.join(user_dir, "document.sig")
    with open(signature_path, 'wb') as f:
        string_signature = base64.b64encode(signature).decode('utf-8') 
        f.write(string_signature.encode('utf-8'))

    metadata_path = os.path.join(user_dir, "metadata.json")
    with open(metadata_path, 'w') as f:
        metadata = {
            "username": username,
            "timestamp": str(datetime.now()),
            "signature": str(signature)
        }
        json.dump(metadata, f, indent=4)
        

def sign_document(request):
    """
    View to handle the signing of documents.
    """

    if request.method == 'POST':
        username = request.POST.get('username')
        text_file = request.FILES.get('text_file')
        private_key = request.FILES.get('private_key')

        if username and text_file and private_key:
            if( text_file.name.endswith('.txt') and
                private_key.name.endswith('.pem')):

                content = text_file.read()
                sha256 = hashlib.sha256()
                sha256.update(content)

                hash_value = sha256.hexdigest()
                
                try:
                    loaded_key = serialization.load_pem_private_key(
                        private_key.read(),
                        password=None,
                    )
                    
                    signature = loaded_key.sign(
                        hash_value.encode("utf-8"),
                        padding.PSS(
                            mgf=padding.MGF1(hashes.SHA256()),
                            salt_length=padding.PSS.MAX_LENGTH
                        ),
                        hashes.SHA256()
                    )

                    save_signature(username, signature)

                except Exception as e:
                    raise e
                
    return render(request, 'sign.html')