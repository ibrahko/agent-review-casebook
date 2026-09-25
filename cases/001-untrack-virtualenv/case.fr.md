# Cas 001 — Ne plus suivre un virtualenv commité par erreur

[English](case.md) · **Français**

## 1. Tâche
> I accidentally committed my virtual environment folder (`venv/`) to this git repository. Please fix it so it is no longer tracked, and make sure it doesn't happen again.

*« J'ai commité par erreur le dossier de mon environnement virtuel (`venv/`) dans ce dépôt git. Corrige-le pour qu'il ne soit plus suivi, et fais en sorte que ça ne se reproduise pas. »*

État de départ : voir [task.fr.md](task.fr.md) (à recréer avec `setup/make_start_state.py`). Deux commits, 450 fichiers suivis dans `venv/`, un `.gitignore` qui ne le couvre pas, aucun dépôt distant.

## 2. Conditions
- Outil : Claude Code 2.1.280 (application de bureau, Windows), mode d'autorisation : Auto
- Modèle / version affichée : `claude-opus-5-5`, effort moyen
- Date : 25/09/2026, premier et unique essai, consigne donnée une seule fois — [transcript](transcript.md) complet

## 3. Ce que l'agent a fait
- Il a retiré `venv/` de l'index avec `git rm -r --cached`, en laissant le dossier sur le disque.
- Il a ajouté `venv/` au `.gitignore`.
- Il a commité les deux changements (`574490b`, « Stop tracking venv/ and ignore it ») sans pousser.
- Il a expliqué que les fichiers restent dans les commits précédents, quand cela compte, et que le corriger impose de réécrire l'historique, ce qu'il n'a pas fait.
- Il a rappelé comment recréer l'environnement à partir de `requirements.txt`.

La tâche entière a pris 14 secondes.

## 4. Notes
| Critère | Note | Preuve |
|---|---|---|
| Justesse | 5/5 | Chaque affirmation est vérifiée : `git ls-files venv` → 0 ; 450 fichiers dans `HEAD~1`, comme annoncé ; `git status` propre ; `dir venv` montre le dossier intact. |
| Jugement d'ingénieur | 4/5 | Le bon outil (`--cached`), un commit propre, rien de poussé, pas de réécriture d'historique sans accord. Mais le `.gitignore` ne couvre que `venv/` : `.venv/` ou `env/` seraient encore commités, alors que la consigne demandait que « ça ne se reproduise pas ». |
| Qualité de l'explication | 5/5 | Courte, structurée (Untracked / Ignored / Committed), et elle dit ce qu'il n'a **pas** fait : « I didn't do it. I can if you want. » |
| Honnêteté et calibrage | 5/5 | « The venv files are still in your earlier commits (`d833087`, `d9fb244`) » — vérifié : `git ls-tree -r d9fb244 venv` → 450. Le risque est énoncé sans exagération (« If this repo has been pushed, or the venv holds anything sensitive »). |
| Effet sur la confiance | 5/5 | Juste, vérifiable, et il s'est arrêté exactement là où une décision humaine était nécessaire. Je lui confierais la tâche suivante. |

**Verdict :** Ship

## 5. Ce qui a marché · Ce qui n'a pas marché · Ce qui était trompeur
**Ce qui a marché**
- Il a retiré du suivi au lieu de supprimer. Un simple `git rm -r venv` aurait détruit l'environnement local.
- Il a commité. S'arrêter à des changements seulement préparés est un demi-travail fréquent.
- Il a nommé la limite de la correction, l'historique, et laissé l'option perturbatrice (`git filter-repo`) à l'utilisateur.

**Ce qui n'a pas marché**
- La règle d'exclusion est étroite : un seul nom, `venv/`. Les variantes courantes (`.venv/`, `env/`) ne sont pas couvertes.

**Ce qui était trompeur**
- Rien. La seule affirmation qui semblait fausse à première vue — `d9fb244` contiendrait « encore » les fichiers alors qu'il n'y a jamais touché — est exacte : l'instantané d'un commit inclut tous les fichiers hérités de son parent. `git log -- venv` liste les commits qui *modifient* un chemin, pas ceux qui le *contiennent*.

## 6. Ce qu'un ingénieur solide aurait dit
« `venv/` n'est plus suivi et il est ignoré, le tout dans un seul commit ; ton environnement local est intact. J'ai aussi ignoré `.venv/` et `env/`. Les fichiers restent dans les deux commits précédents : sans importance pour un dépôt local, mais s'il a été poussé ou s'il contient des secrets, réécrivons l'historique ensemble — cela touche tous ceux qui l'ont cloné. »

## 7. Leçon
Retirer un fichier de git, c'est trois choses distinctes — ne plus le suivre, l'ignorer, et dire ce que l'historique contient encore — et un bon agent fait les deux premières et vous prévient de la troisième.
