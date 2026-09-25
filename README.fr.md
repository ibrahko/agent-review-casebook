# Agent Review Casebook

[English](README.md) · **Français**

> **Travail en cours — v0.1.** Grille de notation, gabarit et cas 001.

Que vaut vraiment la réponse d'un agent de code IA ? Ce carnet de cas juge des sessions réelles avec Claude Code, Cursor et OpenAI Codex sur des tâches back-end Python réalistes, comme un ingénieur senior relit une pull request : la réponse est-elle juste, est-elle trompeuse, et laquelle de deux réponses est la meilleure, preuves à l'appui.

## Comment le lire (3 minutes)

1. La [grille](RUBRIC.md) : cinq critères notés de 1 à 5, et un verdict (*Ship / Ship with fixes / Do not ship*).
2. N'importe quel cas ci-dessous : 400 à 700 mots, chaque note justifiée par une citation de la session.

## Cas

| N° | Tâche | Outil | Verdict |
|---|---|---|---|
| [001](cases/001-untrack-virtualenv/case.fr.md) | Ne plus suivre un virtualenv commité par erreur | Claude Code (`claude-opus-5-5`) | **Ship** |
| [002](cases/002-slow-orders-endpoint/case.fr.md) | Endpoint des commandes trop lent (requêtes N+1) | — | *en cours* |

## Méthode

- Chaque tâche part d'un état connu que chacun peut recréer (script `setup/` dans chaque cas).
- La consigne est écrite **avant** la session et n'est jamais modifiée ensuite.
- Les comparaisons utilisent la même consigne, le même état de départ et le **premier essai** de chaque outil (pas de meilleur de trois).
- Les notes sont données après vérification du résultat (tests lancés, diff relu), jamais d'après le résumé de l'agent.
- Aucun code client, aucune donnée réelle, aucun secret. On ne classe pas les marques : on juge des réponses.

Chaque document existe en anglais et en français ; les fiches de cas sont rédigées d'abord en anglais, puis traduites.

## Auteur

**Ibrahima Koné** — ingénieur back-end Python et IA, Bamako, Mali  
[GitHub](https://github.com/ibrahko) · [LinkedIn](https://www.linkedin.com/in/ibrahima-koné-632006a1)

## Licence

Textes : CC BY 4.0 · Code : MIT — © 2026 Ibrahima Koné
