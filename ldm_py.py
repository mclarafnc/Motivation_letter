#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 16:55:34 2020

@author: fancellomarieclara
"""


def questions():
    print("""Bonjour à vous et bienvenue sur ce programme python!
Ce que je vous promet aujourd'hui est de lire une lettre de motivation peu conventionnelle.

Je vous propose donc de poser vos quesitons dans le script et je pourrais y répondre grâce à ce programme. (merci de respecter la liste de questions et leur formulation)

L'avantage principal de ce type de lettre de motivation est que vous n'avez pas besoin de tout lire, posez uniquement la et les question.s qui vous intéresse.nt ! 

ATTENTION: mes réponses sont sérieuses, mais j'imagine que lire une lettre de motivation doit-être assez barbant, j'y intérgère donc quelques traces d'humour, j'espère que cela vous divertira !
""")
    print("Voici la liste des questions que vous pouvez me poser via ce programme:")
    print("Qui êtes-vous?")
    print("Que faites vous dans la vie?")
    print("Quelles sont vos expériences professionnelles?")
    print("Quelles sont vos motivations?")
    print("Pourquoi faire une lettre de motivation sous cette forme?")
    return 

def reponse():
    compteur=0
    while compteur<5:
        q=input("""Merci de poser votre question : 
""")
        if q=="Qui êtes-vous?":
            question=1
        elif q=="Que faites vous dans la vie?":
            question=2
        elif q=="Quelles sont vos expériences professionnelles?":
            question=3
        elif q=="Quelles sont vos motivations?":
            question=4
        elif q=="Pourquoi faire une lettre de motivation sous cette forme?":
            question=5
        if question==1:
            print("""Je m'appelle Marie Clara Fancello, j'ai 21 ans et suis actuellement en master Économétrie Statistiques à l'Université Paris I Panthéon Sorbonne. 
        Après une licence en Sciences Économiques et Gestions, j'ai décidé de poursuivre mon parcours universitaire avec un master en Sciences Économiques et Sociales.
        Ce master m'a notamment permis d'aiguiser mon esprit critique et d'effectuer un mémoire sur l'immigration européenne au Royaume Uni et son impact sur le vote en faveur du Brexit. 
        
        Il m'a également permis de réaliser que bien que passionnée par les quesitons économiques et sociales, mon intérêt majeur se porte sur l'analyse de données.
        Aussi étonnant ou flagorneur que cela puisse paraître, le recueil, traitement et finalement l'analyse de données me passionne.
        La compréhension d'un phénomène, permise par cette dernière, et toute l'information qu'elle permet d'acquérir au final en font une discipline fascinante à mes yeux. 
        """)
            compteur=compteur+1
        elif question==2:
            print(""" Je suis actuellement en master d'Économétrie Statistiques. Que de mots barbants me direz vous ? Ou vous vous demandez peut-être à quoi cela va me servir? Ce que j'y apprends?
        Et bien     ce sont des questions extrêments pertinentes auxquelles je vais essayer de répondre. Évidemment, si d'autres interrogations persistent (ce que j'espère) je serais disponible pour tout entretient en présentiel comme à distance (étant une jeune étudiante flexible et dynamique).
        Ce master a pour but de former des économétres, statisticiens et data scientists. Les cours sont donc essentiellement axés sur les statistiques, la programmation et l'anlayse. Nos cours principaux sont donc Économétrie avancée, Sondage et analyse de données et Programmation (R, SAS, Python).
        """)
            compteur=compteur+1
        elif question==3:
            print(""" Question essentielle pour vous! Car les expériences professionnelles sont extrêment importantes pour apprendre à connaître quelqu'un et pour l'embaucher par la suite. 
        Ayant 21 ans et étant en master 1, vous vous doutez certainement que je n'ai pas d'expérience en boîte de conseil ou de sondage par exemple. Je vais donc répondre à vos interrogations en deux temps.
        
        Dans un premier temps, je pense qu'une information importante à mon sujet est que je travaille tous les étés depuis mes 14 ans. J'ai donc un large panel de jobs d'étés à mon actif. Serveuse, employée polyvalant dans un fameuse chaîne de restauration rapide américaine, réceptionniste, chef de rang en restauration, jusqu'au poste de gérant d'un hôtel restaurant en l'abscence des propriétaires... La liste est longue!
        Mais rien à voir avec l'analyse de données me direz vous ! Cependant toutes ces expériences et entreprises différentes m'ont appris beaucoup de choses qui me servirons lors des missions que vous me confirez lors d'un stage (enfin, je l'espère évidemment, ne tuons pas la peau de l'ours avant de l'avoir tué!).
        En effet, ces expériences m'ont appris à être flexible, m'adapter aux différentes formes de management, à former des personnes et avoir donc un poste d'autorité et de pédagogie, etc...
        D'un autre côté, j'ai également été membre de l'association des étudiants en Sciences Économiques de Strasbourg pendant 3 ans, chargée Insertion Professionnelle pendant une année. J'ai pendant cette année organisée une vingtaine d'évènement (70 personnes en moyenne à chaque évènement), et formé 8 personnes qui étaient dans mon pôle. 
        Également, je suis acutellement dans l'association de mon master, et ai été élue déléguée de ma formation. Ce qui démontre non seulement de mes capacités d'organisation (études, vie personnelle et engagement associatif) mais également de ma motivation pour que tout se passe au mieux dans toute organisation (universitaire ou associative). VOIR SI JE LAISSE OU CHANGE OU QUOI
        
        Dans un second temps, j'ai eu l'occasion d'effectuer un stage extrêmement intéressant en troisième année de licence au Bureau d'Économie Théorique et Appliquée de l'Université de Strasbourg. Il m’a été confié durant ce stage la réalisation de l’étude d’impact des subventions aux projets artistiques et innovant, projet porté par l’association d’aide aux Startup innovantes ACCRO. Mes missions durant ce stage étaient la création et l’exploitation de bases de données, l’analyse de données d’enquête, la mise en place d’une revue bibliographique, ainsi que la mise en relation et la réalisation d'entretiens avec des acteurs du milieu créatif et numérique.
        Et finalement parlons bien, parlons prog, j'ai eu l'occasion de faire deux mémoires de recherche et trois rapports sous R, SAS et Python, ce qui m'assure un certain niveau d'aisance sur ces différents logiciels.
        """)
            compteur=compteur+1
        elif question==4:
            print(""" Ah... Les motivations. Car embaucher un bon candidat, c'est bien mais embaucher un bon candidat super motivé, c'est mieux! 
        L'avantage de ce type de lettre de motivation, c'est que vous avez pu venir à cette question directement, l'inconvénient, c'est que si vous avez déjà lu d'autres réponses je risque de me répéter (dans lequel cas je m'excuse bien évidemment!).
        Avoir une bonne formation universitaire est essentielle aujourd'hui, surtout dans le domaine de la data, mais est loin d'être suffisante! J'ai choisis ce master justement parce qu'il offre la possibilité de faire un stage et une alternance ce qui nous permet de nous familiariser avec le monde du travail et de l'entreprise, et d'apprendre des choses diverses et variées : tant sur les différentes méthodes de gestion et d'analyse des données, que sur les attentes des employeurs et les différentes organisations des entreprises.
        J'aimerais donc apprendre à vos côtés, programmer, nettoyer, supprimer, analyser des données. J'aimerais utiliser les compétences que j'ai pu acquérir jusqu'ici tant en programmation qu'en analyse et réflexion.
        Ma seule motivation est l'apprentissage. 
        
        Ah, et votre entrepirse est plutôt bien notée sur Glassdoor aussi : ça donne envie.
        """)
            compteur=compteur+1
        elif question==5:
            print("""LA question que vous devez le plus vous poser (I guess) ! Et honnetement, la question la plus intéressante je suppose. 
        Et bien pour répondre à une question si qualitative, une seule raison ne saurait suffire! Voici donc une petite énumération:
        Raison numéro 1 : Parce que rectruter un stagiaire ne doit très certainement par être la partie la plus intéressante de votre job, donc si je peux rendre cette tâche un peu moins barbante, tout le plaisir est pour moi!
        Raison numéro 2 : Parce que mentir sur son CV c'est mal donc au moins, même si ce programme est extrêment simple, vous voyez que je sais utiliser python. 
        Raison numéro 3 : Pour vous montrer que quand je dis que j'adore la programmation, c'est au point d'y passer mon temps libre! La franchise est la base de toute relation saine, et j'espère qu'il y aura relation -de type convention de stage- entre vous et moi.
        Raison numéro 4 : Parce que c'est plus interractif qu'une lettre de motivation sous word, et donc à défaut d'avoir des interractions sociales, autant avoir des interractions spyder ! 
        Raison numéro 5 : Parce qu'une lettre de motivation classique ne m'aurait pas permis de dire tout ce que je vous ai dis, et donc de vous donner une réelle idée de qui je suis.
        """)
            compteur=compteur+1

    return

          
