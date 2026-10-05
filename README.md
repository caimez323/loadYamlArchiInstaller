## Pour mettre à jour les prochaines fois :

1. Compiler dans une version de python adapté:
    - Lancer le setup.py de la dernière version du repo avec les options "build"
    - Identifier la bonne version de python (c'est celle qui va marcher quand on remplace le .exe dans l'install)

2. Déplacer les fichiers compilés ainsi de la zone de test vers l'install.
    - ArchipelagoOptionsCreator.exe
    - optionscreator.kv
    - library.zip



## Historique des versions python :

v0.6.8 => python 3.13


## To create a release

```pyinstaller --onefile --add-data "data;data" main.py```
