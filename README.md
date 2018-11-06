# Blockchain pour assurance agricole

## Mise en place du projet

### Développement
1. Installer pip et python (version 3.6)
2. Créer un virtualenv (pas dans le projet)
   > virtualenv3.6 venv-blockchain
3. Activer le virtualenv

	Linux:
	> source venv-blockchain/bin/activate

	Windows:
	> venv-blockchain/jesaisplus

4. Installer les dépendances
   > pip install -r requirements.txt
5. Faire les migrations de la base de données
   > pyhton manage.py migrate
6. Lancer le serveur de tests
   > python manage.py runserver
   (cette commande lance un serveur en localhost:8000)

### Production

## Base de données
La base de donnée contiendra les informations client, les
coordonnées banquaires, ainsi que le contrat.

La blockchain contiendra l'ID du contrat, ainsi que l'ID de
l'assuré.

## UI

Le formulaire de contact contiendra les champs suivants:

- Civilité Mme	Mlle M.
- Nom
- Prénom
- Code postal
- Ville
- Adresse
- Téléphone
- Email
- Numéro de contrat
- Votre message
- Contact

Bootstrap sera utilisé.

## Contenu de l'archive
- doc: contient les documents à rendre et les ressources.

# Todo
- [ ] Finir les specs
- [ ] Faire une courte présentation dans le Readme
