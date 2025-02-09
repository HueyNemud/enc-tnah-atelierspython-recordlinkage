#!/usr/bin/env python
# La ligne ci-dessus permet d'exécuter le script sans préciser d'interpréteur.
# Par exemple, si le script est exécutable (chmod +x couplage.py), on peut l'exécuter directement avec ./couplage.py

"""
   ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ .
   Fichier à compléter pour la séance n°2 sur le couplage d'enregistrements.
    ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ .

    Cette fois, le fichier n'est pas structuré en questions à compléter.
    À la place, vous allez devoir écrire entièrement le script
    à partir des questions du fichier `README.md`.

    Pour exécuter le script, vous pouvez utiliser la commande suivante :
    ```bash
    python cli_couplage.py
    ```
    ou, grace à la ligne `#!/usr/bin/env python3` en début de fichier :
    ```bash
    ./cli_couplage.py
    ```

    ℹ️ N'oubliez pas :
        - Copilot, ChatGPT et autres  assistants IA sont vos amis ...
        - ... mais des amis qu'on appelle que si on est vraiment bloqué.e !

    🙏 Essayez d'appliquer les bonnes pratiques de programmation en Python:
        - on donne des noms explicites aux variables et fonctions ;
        - un commentaire ne paraphrase pas le code, il explique POURQUOI on fait quelque chose ;
        - on n'oublie pas les types hints pour les paramètres et le retour des fonctions  !
        - une docstring concise est mieux que pas de docstring du tout !

    💡 Dans VsCode, SublimeText et d'autres éditeurs,
          le raccouci clavier `Ctrl + Shift + /` permet de commenter
          ou décommenter le code sélectionné.

    À vous de jouer ! 🚀
    """

# Déclarez ici les imports


# Et ici va le code! 🤓


# 💡 ASTOUCE POUR LA QUESTION 10
#
# Pour séparer le premier élément d'une liste des autres, on peut utiliser la syntaxe suivante :
# premier, *reste = [1, 2, 3, 4, 5,...]
# Python va affecter le premier élément à la variable `premier`, et tout le reste à la variable `reste`
# ⚠️ Notez l'astérisque "*" devant la variable `reste` !
#       Il indique à Python que cette variable doit contenir tous les éléments restants de la liste.
#
# En plus, on peut utiliser une *list comprehension* pour écrire une boucle *for* en une seule ligne.
# En combinant ces deux astuces, la ligne suivante lit les enregistrements du fichier CSV
#  et sépare l'entête des données...
# ...en une seule ligne de code ! Magique, non ?🪄
#
# Par exemple :
# entête, *enregistrements = [e for e in csv.reader(args.fichier)]
