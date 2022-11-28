# Local Development Installation

    git clone git@bitbucket.org:consumerchoicemvp/ida-backend.git

## Init virtualenv, optional

    virtualenv .venv
    source .venv/bin/activate

## Install 
    #for test 1
    pip install -U spacy
    python3 -m spacy download en_core_web_sm
    
    #for test 2
    pip install sympy 

## Start shell-файл     
    python3 test_1/models.py test_1/test_test1.txt
    python3 test_2/permute.py 5

