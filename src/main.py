import os
import subprocess

def run_django_server():
    # Caminho relativo para o diretório do projeto Django
    project_directory = os.path.join(os.path.dirname(__file__), 'PSF_GESTAO_FINANCEIRA')
    manage_py = os.path.join(project_directory, 'manage.py')
    
    # Navegar para o diretório do projeto
    os.chdir(project_directory)
    
    # Executar o comando para iniciar o servidor Django
    subprocess.run(['python', manage_py, 'runserver'])

if __name__ == "__main__":
    run_django_server()