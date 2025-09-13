If you run this code in colab you should just be able to copy and paste and not have to pip install anything and have it run fine.

If you're trying to run the program on your machine here are some instructions for windows (I recommend command prompt over powershell):

If you dont want a virtual environment you can skip steps 1 and 4

python 3.11 or later is required for the requirements.txt

1.) virtual environment (if you care about that)-
    python -m venv .venv
    .\.venv\Scripts\activate.bat (command prompt)
    .\.venv\Scripts\Activate.ps1 (powershell)

2.) install requirements-
    pip install -r requirements.txt

3.) Running-
    python Assignment1.py

4.) Deactivate virtual environment-
    deactivate 