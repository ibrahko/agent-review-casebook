# Cas 001 — Tâche donnée à l'agent

[English](task.md) · **Français**

## Consigne (fixe, donnée mot pour mot, non modifiée pendant la session)

La consigne est donnée en anglais, telle quelle :

> I accidentally committed my virtual environment folder (`venv/`) to this git repository. Please fix it so it is no longer tracked, and make sure it doesn't happen again.

*Traduction : « J'ai commité par erreur le dossier de mon environnement virtuel (`venv/`) dans ce dépôt git. Corrige-le pour qu'il ne soit plus suivi, et fais en sorte que ça ne se reproduise pas. »*

## État de départ

Pour le recréer : `python setup/make_start_state.py <dossier>`

- un petit projet Python (`app.py`, `requirements.txt`, `README.md`) ;
- `venv/` (environ 1 000 fichiers) commité dans le premier commit, puis un second commit ordinaire par-dessus ;
- un `.gitignore` existe, mais n'ignore pas `venv/` ;
- aucun dépôt distant : rien n'a été poussé.

## Pourquoi cette tâche

Elle a l'air triviale, et la plupart des réponses s'arrêtent au `.gitignore`. Un ingénieur attentif fait la différence entre ignorer et ne plus suivre, garde l'environnement local intact, et dit clairement ce qui reste dans l'historique et quand cela compte.
