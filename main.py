import os
import shutil
from pathlib import Path

# Dictionnaire associant le nom du dossier de destination aux extensions correspondantes
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".csv", ".pptx"],
    "Archives": [".zip", ".tar", ".gz", ".7z", ".rar"],
    "Audio": [".mp3", ".wav", ".flac", ".aac"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Executable_Et_Code": [".exe", ".msi", ".py", ".js", ".html", ".css", ".sh"],
}


def organiser_dossier(chemin_cible):
    """
    Parcourt le dossier cible et déplace chaque fichier dans un sous-dossier
    correspondant à son extension.
    """
    dossier = Path(chemin_cible)

    # Vérification de l'existence du dossier
    if not dossier.exists() or not dossier.is_dir():
        print(f"❌ Le dossier '{chemin_cible}' n'existe pas ou n'est pas un répertoire valide.")
        return

    print(f"\n📂 Traitement du dossier : {dossier.resolve()}\n")

    fichiers_deplaces = 0

    # Parcours de tous les éléments du dossier
    for element in dossier.iterdir():
        # Ignorer les sous-dossiers déjà existants et le script lui-même
        if element.is_dir() or element.name == Path(__file__).name:
            continue

        extension = element.suffix.lower()
        categorie_trouvee = None

        # Recherche de la catégorie correspondant à l'extension
        for categorie, extensions in FILE_CATEGORIES.items():
            if extension in extensions:
                categorie_trouvee = categorie
                break

        # Si l'extension n'est pas répertoriée, classer dans 'Autres'
        if not categorie_trouvee and extension != "":
            categorie_trouvee = "Autres"

        if categorie_trouvee:
            # Création du sous-dossier de destination s'il n'existe pas
            dossier_destination = dossier / categorie_trouvee
            dossier_destination.mkdir(exist_ok=True)

            # Gestion des doublons pour ne pas écraser de fichiers existants
            fichier_destination = dossier_destination / element.name
            compteur = 1
            while fichier_destination.exists():
                nom_base = element.stem
                extension_base = element.suffix
                fichier_destination = dossier_destination / f"{nom_base}_{compteur}{extension_base}"
                compteur += 1

            # Déplacement du fichier
            shutil.move(str(element), str(fichier_destination))
            print(f"🚚 [{categorie_trouvee}] {element.name} -> {fichier_destination.name}")
            fichiers_deplaces += 1

    print(f"\n✅ Organisation terminée ! {fichiers_deplaces} fichier(s) déplacé(s).")


if __name__ == "__main__":
    print("—" * 45)
    print("  AUTOMATE D'ORGANISATION DE FICHIERS")
    print("—" * 45)

    chemin = input("\nEntrez le chemin du dossier à organiser (ex: /path/to/Downloads ou C:\\Users\\User\\Downloads) : ").strip()

    # Si l'utilisateur valide sans rien écrire, utiliser le répertoire courant
    if not chemin:
        chemin = "."

    organiser_dossier(chemin)