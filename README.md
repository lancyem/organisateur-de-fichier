# Projet 2 : Script d'Automatisation de Fichiers (File Organizer)

Un script Python d'automatisation système qui trie et nettoie automatiquement n'importe quel répertoire encombré (par exemple le dossier *Téléchargements*) en classant les fichiers dans des sous-dossiers thématiques selon leurs extensions.

## 📌 Fonctionnalités
- **Classification automatique** : Tri par types (Images, Documents, Archives, Audio, Vidéos, etc.).
- **Gestion des extensions inconnues** : Création automatique d'un dossier `Autres`.
- **Protection contre le remplacement** : Renommage automatique en cas de doublons.
- **Sécurité** : Exclusion automatique des sous-dossiers et du script principal lors du balayage.

## 🛠️ Concepts Python appliqués
- Manipulation avancée du système de fichiers via `pathlib` et `shutil`
- Parcours dynamique de répertoires (`iterdir()`)
- Structure de données par dictionnaires et listes
- Traitement de chaînes et gestion des extensions

## 🚀 Lancement du projet
```bash
python main.py