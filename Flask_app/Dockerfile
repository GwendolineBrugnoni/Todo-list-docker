# image docker utilisée comme base est une image python
FROM python:3.8 

# ajout des fichiers nécessaire à la création de l'application
# a savoir : 
#	- le main.py qui contient le programme de l'application copié depuis le répertoire courant (d'où le .)
#	- le html copié dans le dossier templates depuis le dossier templates
#	- le requirements.txt qui contient la liste des dépendances necessaires à la construction de l'application copié depuis le répertoire courant 

ADD main.py .
ADD templates templates
ADD requirements.txt .

# installation des dépendances inscrites dans le document requirements.txt
RUN pip install -r requirements.txt

# lancement du main python
CMD ["python","./main.py"]