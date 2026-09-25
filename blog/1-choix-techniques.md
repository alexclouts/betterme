# Mes choix techniques

## Contexte du projet
L'idée derrière l'application web `BetterSelf` est d'offrir une solution Open Source gratuite pour les gens qui suivent attentivement leur alimentation et qui consignent ce qu'ils mangent. 

### Le public cible

L'utilisateur typique se fixe des objectifs en matière de nutrition. À chaque jour, il pèse et consigne ses aliments dans un journal de bord. Selon le besoin, il cherche à créer un léger déficit calorique quotidien par rapport à ses besoins de maintenance ou il se concentre à manger davantage de protéines. Finalement, il souhaite comparer sa consommation réelle à ses objectifs (calories, protéines) pour suivre sa progression.

### Problème rencontré

Le problème principal est que cette tâche est fastidieuse et peut être la source de plusieurs erreurs. Elle implique, par exemple, de consulter les emballages, de faire des calculs à la main, de saisir toutes les valeurs nutritionnelles dans un tableau par écrit et de calculer l'apport calorique en fonction du poids des aliments et des portions.

### La solution offerte

La solution offerte par `BetterSelf` est de rendre ce processus plus rapide, plus fiable et plus facile à maintenir au quotidien, en automatisant une grande partie de la saisie et en centralisant l’historique alimentaire dans une interface simple et rapide d'utilisation.

## Choix techniques retenus

### Frontend : React et Progressive Web Application – PWA

Pour l’interface utilisateur, j’ai choisi d’utiliser **React**, une bibliothèque JavaScript très répandue pour construire des interfaces web interactives. Cette technologie, combinée avec l'approche des **PWA**, permettra à l'application de se comporter comme s'il s'agissait d'une application native. L'utilisateur pourra donc utiliser ses fonctionnalités à partir de son téléphone cellulaire directement sans avoir à se connecter à une interface Web à chaque fois. Ce choix permet également d'éviter les restrictions imposées par les Apps Store, tels que `Google Play`, qui ont souvent plusieurs exigences à satisfaire pour que l'application soit accessible.

De plus, l'objectif est que l’application soit également utilisable sur ordinateur (pour les tests, le développement et l’évaluation). Cette technologie est le meilleur des deux mondes. Elle est également très répandue au sein des applications modernes, ce qui rend la documentation exhaustive et facile d'accès.

### Backend : Python et FastAPI

Côté backend, j’ai choisi d'utiliser le language **Python**, couplé au framework **FastAPI**. D'abord, je suis déjà familié avec la syntaxe de Python pour l'avoir déjà utilisé au sein de projets divers. Je considère que la syntaxe est simple et bien adaptée à ce projet et à ses besoins en terme d'infrastructures. Python est également un language qui intègre bien des fonctionnalités clés de l'application, telles que la gestion des bases de données, l'authentification d'un utilisateur et les appels à des API externes (comme Open Food Facts dans notre cas). Je ne suis pas familier avec FastAPI, mais ce framework a été choisi pour la construction d'un API Web afin d'acheminer les requêtes du frontend au bases de données intégrées. Cette technologie est facile à exécuter localement et à déployer dans un conteneur Docker. J'utiliserai la librairie `Pydantic` afin de valider les données et les schémas. Mon backend exposera des endpoints via le protocole HTTP afin de transiger les informations demandées par l'utilisateur. Voici des exemples de requête :

- `GET /api/foods?search=...` – rechercher des aliments;
- `GET /api/foods/by-barcode?barcode=...` – obtenir les infos d’un produit via son code-barres;
- `POST /api/consumptions` – enregistrer un aliment consommé;
- `GET /api/consumptions?date=...` – consulter l’historique d’une journée;
- `GET /api/goals`, `PUT /api/goals` – gérer les objectifs caloriques et protéiques.

### Base de données : SQL (SQLite, évolution possible vers PostgreSQL)

Pour stocker les données locales (utilisateurs, aliments, repas, consommations, objectifs), j’ai choisi la **base de données relationnelle (SQL)**. Une fois de plus, j'ai déjà utilisé cette technologie précédemment, donc je suis familié avec son fonctionnement et sa syntaxe pour effectuer le traitement de données. Le modèle relationnel comprend plusieurs avantages pour les cas d'utilisation de `BetterSelf`. Par exemple, les aliments consommés par un utilisateur sont associés à une date précise et à un moment précis (déjeuner, dîner, souper, collation, etc.). Un repas peut contenir plusieurs aliments, et un aliment peut être consigné à plusieurs endroits. L'agrégation des données est également facile à réaliser depuis les requêtes SQL, ce qui permet de calculer le nombre de macronutriments ou de calories consommés quotidiennement. Son intégration avec Python est facile: plusieurs outils et bibliothèques existent déjà. Pour mon application, je compte utiliser `SQLAlchemy`, un logiciel gratuit et open-source qui offre un accès flexible aux fonctionnalités de SQL.

### Hébergement

Pour le choix d'hébergement, **Railway** est envisagé comme option d'hébergement provisoire du backend et du framework `FastAPI`. Le plan gratuit offre jusqu'à 0,5 Go d'espace disque par projet, permettant un hébergement à faible coût, et offre un support natif pour les applications Python. Cette plateforme offre également la possibilité d'héberger la base de données dans le même environnement. Selon les besoins grandissants de l'application, il se pourrait que cette décision soit révisée ultérieurement.

Pour ce qui est du frontend React, celui-ci sera hébergé sur GitHub Pages afin de minimiser les coûts associés à Railway. Cette solution a l'inconvénient d'augmenter la complexité de gestion puisqu'elle nécessite le déploiement du projet sur deux plateformes différentes. À ce stade, la solution idéale n'est pas encore fixée. La complexité de sa mise en oeuvre et les coûts d'implémentation pourraient apporter des changements aux choix d'hébergement.

## Alternatives considérées

### Frontend
#### Application native Android (Kotlin/Java)
L'utilisation de Kotlin, en particulier la technologie `Kotlin Multiplatform` est une solution intéressante. Pour l'avoir déjà utilisé dans le passé, elle est très complexe à mettre en place et récente. Certaines librairies ne sont pas encore compatibles avec cette technologie, ce qui exige une double implémentation (soit en Kotlin pour Android et en Swift pour iOs). Dans le cadre du travail, on nous demande de concevoir une **application Web**, et cette solution ne répond pas à ce critère, ce pourquoi elle n'a pas été envisagée plus sérieusement.

#### Vue.js
Pour avoir déjà entendu parler de React, j'avais déjà un intérêt à utiliser ce framework avant même de considérer des alternatives. Après m'être renseigné davantage, `Vue.js` serait une alternative intéressante pour ce projet. Par contre, je conserve mon choix initial puisqu'il est très répandu au sein de la communauté et qu'il y a une abondance de ressources et d'exemples d'utilisation pour un projet comme celui-ci.

### Backend

#### Node.js (Express / NestJS)
  Cette alternative aurait été intéressant pour avoir un seul langage (JavaScript/TypeScript) à la fois pour le frontend et le backend. Cependant, je crois que mes connaissances actuelles en Python me permettront de comprendre, d'écrire et de déboguer plus facilement le code utilisé pour construire la logique de l'application. La courbe d'apprentissage sera moins prononcée lors de son développement.

#### Django
Ce framework Python est très complet (ORM, authentification, admin, etc.) et offre des fonctionnalités plus avancées que FastAPI. Malgré cela, mon choix a été fait en tenant compte de la grande flexibilité offerte par FastAPI, par le biais d'interactions en temps réel avec des fonctionnalités via des WebSockets. D'ailleurs, l'option choisie est également plus facile à apprendre et à intégrer que Django, bien que ce dernier soit plus mature et mieux documenté. Dans le contexte où FastAPI aura une architecture frontend/backend séparée, la flexibilité de FastAPI est une priorité selon moi.

Référence : https://blog.jetbrains.com/pycharm/2023/12/django-vs-fastapi-which-is-the-best-python-web-framework/

#### Flask
Flask est également une alternative très simple et légère. J'ai choisi FastAPI puisque la validation des données et la documentation interactive de l’API répondent directement à mes besoins : je devrai définir clairement les données échangées entre React et le backend, puis tester mes routes pendant le développement. Avec Flask, la gestion des extensions et des librairies peut devenir laborieuse lorsque l'application augmente en complexité et que plusieurs fonctionnalités doivent être ajoutées.


### Base de données

#### Base de données NoSQL (MongoDB)
Une base de données NoSQL, comme MongoDB, pourrait stocker les informations sous forme de documents. Cependant, SQL correspond très bien aux données utilisées par mon application. Par exemple, un utilisateur enregistre des aliments et des repas à des moments spécifiques, plusieurs aliments peuvent composer un repas, etc. Un modèle relationnel facilite la création de ces liens et le calcul des bilans alimentaires. Dans une base de données NoSQL, les requêtes d'agrégation sont plus complexes à mettre en place.

#### PostgreSQL d’emblée
PostgreSQL est une autre possibilité parmi les bases SQL. Je ne l’écarte pas, mais son utilisation dès le début du projet nécessite la configuration et l’hébergement d’un serveur de base de données, ce qui augmente la complexité du projet. Je préfère commencer avec SQLite pour développer et tester les premières fonctionnalités de l'application et réévaluer ce choix avant le déploiement. Je devrai également vérifier que l’hébergement choisi offre un stockage persistant pour conserver l'historique des utilisateurs d'une session à l'autre.

## Incertitudes et remise en question

À ce stade, plusieurs points restent à préciser :

### Choix exact de la plateforme d’hébergement
Le choix d'hébergement est encore un choix qui n'est pas définitif. Plusieurs considérations sont encore inconnues pour le moment et dépendent de l'avancé du projet. Elles comprennent, par exemple, la simplicité de configuration du service utilisé, la facilité à intégrer une base de données SQL et les coûts associés à l'hébergement des services offerts.

### Gestion de l’authentification  
Plusieurs options sont possibles. Lors de mes recherches, j'ai vu que FastAPI supporte la méthode OAuth 2.0 d'emblée, ce qui est une avenue intéressante. Autrement, un service d'authentification traditionnel (combinaison email/mot de passe) peut également être offerte. Cette décision sera prise en fonction des besoins en matière de sécurité et du temps de développement requis pour sa mise en place.

### Structure exacte du frontend React
Comme React n'est pas encore familier, j'ignore pour le moment la structure à employer au sein du projet. Le choix des librairies et des fonctionnalités à utiliser est encore à déterminer, par exemple ce qui concerne la gestion des états, le fonctionnement de la navigation, etc.

### Intégration de l’API Open Food Facts
Plusieurs questions ne sont pas encore répondues concernant la gestion des requêtes à l'API externe Open Food Facts. Par exemple, comment gérer les cas où un code-barres n’est pas reconnu ? Faut-il prévoir un mécanisme de cache local pour limiter les appels externes ?

Ces incertitudes seront répondues au fur et à mesure que les premières fonctionnalités seront développées (authentification, recherche d’aliments, enregistrement de consommations, tableau de bord).


## Conclusion

Pour résumé, les choix techniques actuels pour `BetterSelf` sont :

- **Frontend :** React, en mode PWA, pour une interface moderne utilisable sur ordinateur et mobile.
- **Backend :** Python + FastAPI, pour une API claire, performante et facile à tester.
- **Base de données :** SQLite, adapté aux relations entre utilisateurs, aliments, repas et consommations.
- **Hébergement :** la plateforme Railway, avec une architecture prévue pour être containerisée (Docker).
