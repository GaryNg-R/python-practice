
## Setup python vitrual environment :
   python3 -m venv path/to/venv 
   source path/to/venv/bin/activate 
   pip install -r requirements.txt
   or 
   pipenv install 
   
   
# use conda 
  * conda info --env 
  conda create --name myenv python=3.12
  conda activate env_name 
   conda deactivate
   
# to pull installed libs to requirements.txt 
    pip freeze > requirements.txt 

    conda env export > environment.yml
