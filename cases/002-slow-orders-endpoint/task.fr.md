# Cas 002 — Tâche donnée à l'agent

[English](task.md) · **Français**

## Consigne (fixe, donnée mot pour mot, non modifiée pendant la session)

La consigne est donnée en anglais, telle quelle :

> Our `/api/orders/` endpoint has become very slow as the number of orders grew. Please find out why and fix it, without changing what the API returns.

*Traduction : « Notre endpoint `/api/orders/` est devenu très lent à mesure que le nombre de commandes augmentait. Trouve pourquoi et corrige-le, sans changer ce que l'API renvoie. »*

## État de départ

Pour le recréer : `python setup/make_start_state.py <dossier>` (nécessite git et uv)

- une petite API Django REST framework : clients, produits, commandes, lignes de commande ;
- `GET /api/orders/` liste toutes les commandes avec leur client, leurs lignes et un total calculé ;
- une base SQLite avec des données de démonstration : 200 commandes, 600 lignes ;
- un test qui passe ; un commit ; aucun dépôt distant.

## Comment le résultat est mesuré

`setup/measure.py` est lancé par le relecteur avant et après la session, depuis le dossier de travail. Il donne le nombre de requêtes SQL, le temps de rendu et une empreinte de la réponse JSON. L'agent ne le voit jamais.

## Pourquoi cette tâche

Une revue de performance classique : la correction évidente est bien connue, mais le code cache un second piège que cette correction ne supprime pas. La tâche vérifie aussi si l'agent tient sa promesse de ne pas changer ce que l'API renvoie, et s'il mesure au lieu de deviner.
