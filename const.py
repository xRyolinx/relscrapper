# CHANGEZ ICI LES PARAMETRES
params = {
    # nom du fichier excel (gardez le .xlsx a la fin du nom)
    'filename': 'DBlinkedin.xlsx',
    
    # combien de profils cherchez-vous ?
    # (n'abusez pas sinon vous serez potentiellement bloqué, jamais sratli mais voila)
    'nb': 10,
    
    # si vous voulez sauter des profils que vous avez deja
    # par ex vous avez chercher deja 23 f'un fichier, diro direct 24
    'start': 0,

    # les mots que vous VOULEZ trouver f'ga3 les resultats (pas sur ydjo ga3 ga3 fihom mais voila)
    'mustInclude': [
    ],
    
    # une liste de mots qui vous interessent
    # ya9der ydji wahad fihom berk, wela plusieurs 3la derba
    # c un OR quoi
    'searchFor': [
        'commercial',
    ],
    
    # rako thawsso f'linkedin logique lol, touchez pas à ca
    'site': "linkedin.com%2Fin",
}