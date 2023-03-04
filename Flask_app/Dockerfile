# image docker utilisee comme base est une image python
FROM python:3.8 

# ajout des fichiers necessaire a la creation de l'application
# a savoir : 
#	- le main.py qui contient le programme de l'application copie depuis le répertoire courant (d'ou le .)
#	- le html copie dans le dossier templates depuis le dossier templates
#	- le requirements.txt qui contient la liste des dependances necessaires a la construction de l'application copie depuis le repertoire courant 

ADD main.py .
ADD templates templates
ADD requirements.txt .

# installation des dependances inscrites dans le document requirements.txt
RUN pip install -r requirements.txt

# lancement du main python
CMD ["python","./main.py"]