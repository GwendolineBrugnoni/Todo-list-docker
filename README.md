# Todo-list-docker
Ce projet permet d'enregister des types de codes malicieux (example: cheval de troie) et de les classifiers à travers 3 catégorie: 

- Virus 
- Worm
- Memory based

Pour pouvoir utiliser ce projet il suffit de :

Se deplacer dans le dossier Flask app : 

```
cd Flask_app
```

Et de lancer le docker compose :

```
docker-compose up
```

Les images utilisées (mongo et gwendolinebrugnoni/flask) sont sur dockerhub. Il n'est donc pas nécessaire de build une image. De plus un workflow est associé à ce projet qui fais
que l'image de l'applications flask est mise à jours dès que quelqu'un push sur la branch main.
