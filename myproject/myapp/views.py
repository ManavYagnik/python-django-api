from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import FileResponse
from django.urls import reverse
import subprocess
import os
import platform

from django.http import HttpResponse

def home(request):
    if request.method == 'POST' and request.FILES.get('file_upload'):
        file = request.FILES['file_upload']
        # Define the directory within your 'myapp' directory where you want to save the uploaded files
        #upload_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')
        # Create the directory if it doesn't exist
        
        #if not os.path.exists(upload_dir):
         #   os.makedirs(upload_dir)
        # Save the uploaded file to the specified directory
        with open(os.path.join('/home/jizong/workspace/nerfstudio/deploy/shared/video', file.name), 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        return HttpResponseRedirect(reverse('success', kwargs={'file_name': file.name}))
    return render(request, 'home.html')

def success(request, file_name):
    if request.method == 'POST':
        
         return HttpResponseRedirect(reverse('generate', kwargs={'file_name': file_name}))
    
    return render(request, 'success.html', {'file_name': file_name})


def generate(request, file_name):
  
    rundocker(file_name)

    return render(request, 'generate.html',{'file_name': file_name})

   




def download_file(request):
    file_path = '/home/jizong/workspace/nerfstudio/deploy/shared/export/yagnik_test/point_cloud.ply'

    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            response = HttpResponse(file.read(), content_type='application/octet-stream')
            response['Content-Disposition'] = 'attachment; filename="' + os.path.basename(file_path) + '"'
            return response
    else:
        return HttpResponse("File not found", status=404)



    


import subprocess

def rundocker(file):
    docker_command = f"ping -c 5 8.8.8.8"
    #docker_command = f"docker exec -it ns python3 pipeline.py --video-path ./shared/video/{file} --output-dir ./shared/export/test_fix_focus"
    #process = subprocess.Popen(docker_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    process = subprocess.Popen(docker_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=1, universal_newlines=True)
    for line in iter(process.stdout.readline, ''):
        print(line, end='')
    # Wait for the command to finish
    #stdout, stderr = process.communicate()
    #print(process)
    # Check for errors
    #if process.returncode != 0:
    #    print(f"Error executing Docker command: {stderr.decode('utf-8')} {file}")
    #else:
    #    print(f"Docker command executed successfully:\n{stdout.decode('utf-8')}, {file} name")

    
