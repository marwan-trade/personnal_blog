# 🕌 Mon Blog Personnel - Performances, Découvertes & Actualité Islamique

Ce projet est un blog personnel développé avec **Python/Django** et **SQLite**, conçu pour partager mes performances personnelles, mes découvertes et des articles liés à l'islam et son actualité.

---

## 🚀 Fonctionnalités

- 🔐 Authentification utilisateur
- ✍️ Création et gestion d’articles
- 🗃️ Classement par catégories : Performances, Découvertes, Religion
- 🧠 Interface d’administration Django
- 🔎 (À venir) Recherche et filtrage d’articles
- 💬 (Optionnel) Système de commentaires

---

## 🛠️ Technologies Utilisées

| Outil/Technologie | Rôle |
|-------------------|------|
| [Python](https://www.python.org/) | Langage principal |
| [Django](https://www.djangoproject.com/) | Framework web |
| [SQLite](https://www.sqlite.org/) | Base de données légère |
| [VS Code](https://code.visualstudio.com/) | Environnement de développement |
| [Git](https://git-scm.com/) / [GitHub](https://github.com/) | Gestion de version & hébergement |

---

## 📁 Structure de base du projet

```bash
monblog/
├── blog/              # App principale
│   ├── models.py      # Modèles de données
│   ├── views.py       # Logique métier
│   ├── urls.py        # Routes de l'application
│   └── templates/     # Fichiers HTML
├── monblog/           # Paramètres du projet Django
│   ├── settings.py    # Configuration globale
│   └── urls.py        # Routes principales
├── db.sqlite3         # Base de données
├── manage.py          # Utilitaire de commande
└── README.md
