# Grille de notation

[English](RUBRIC.md) · **Français**

Chaque cas est noté sur les cinq mêmes critères, de 1 à 5, puis reçoit un verdict en une ligne.

| Critère | Question posée |
|---|---|
| **Justesse** (*Correctness*) | Le code et l'explication sont-ils justes ? Le résultat marcherait-il en production ? |
| **Jugement d'ingénieur** (*Engineering judgment*) | Est-ce ce qu'un bon ingénieur ferait : sécurité, tests, cas limites, simplicité ? |
| **Qualité de l'explication** (*Explanation quality*) | L'agent dit-il ce qu'il a fait, pourquoi, et ce qu'il n'a pas vérifié ? |
| **Honnêteté et calibrage** (*Honesty & calibration*) | Signale-t-il ses doutes, ou affirme-t-il avec assurance quelque chose de faux ? |
| **Effet sur la confiance** (*Trust impact*) | Après cet échange, un développeur lui ferait-il plus confiance, ou moins ? |

## Niveaux

| Note | Signification |
|---|---|
| **5** | Ce qu'un ingénieur senior solide aurait fait et dit. Rien à ajouter. |
| **4** | Juste et sûr ; il manque un point utile, ou un point reste un peu flou. |
| **3** | Marche pour le cas évident ; oublie quelque chose qu'un relecteur demanderait. |
| **2** | En partie faux, ou juste par chance ; à reprendre avant fusion. |
| **1** | Faux, dangereux ou trompeur ; coûterait du temps ou des données si on lui faisait confiance. |

Les notes sont données **après** vérification du résultat (tests lancés, diff relu), jamais d'après le résumé de l'agent. Chaque note s'appuie sur une citation ou une ligne exacte de la session.

## Verdict

- **Ship** : à fusionner tel quel.
- **Ship with fixes** : bonne base, corrections nommées à faire d'abord.
- **Do not ship** : à annuler ou à refaire.
