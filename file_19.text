Ouvrez votre navigateur à l’adresse **http://127.0.0.1:5000/** et vous avez :

- La page d’accueil (`/`) qui liste les items.
- Le lien **Nouvel item** → formulaire de création.
- Les actions **Modifier / Supprimer** sur chaque item.

---

## 4️⃣ Points d’extension (à vous de choisir)

| Fonctionnalité | Où l’ajouter ? | Exemple de code |
|-----------------|----------------|-----------------|
| **Authentification** (login/logout) | Blueprint `auth` + `flask_login` | `@login_required` sur les routes |
| **Pagination** des listes | Modification de `index()` / `item_list()` | `Item.query.paginate(page, per_page, False)` |
| **API JSON** (REST) | Nouveau Blueprint `api` avec `@app.route(..., methods=["GET","POST"])` | `return jsonify(item.to_dict())` |
| **Tests unitaires** | Dossier `tests/` avec `pytest` | `client.get('/')` |
| **Déploiement** (Docker, Gunicorn, Nginx) | Dockerfile + docker‑compose.yml | `FROM python:3.12-slim` |
| **Gestion des environnements** | `python-dotenv` + variables d’environnement | `os.getenv('DATABASE_URL')` |
| **Rich Text** (markdown, upload d’images) | WTForm + Flask‑Uploads | `werkzeug.utils.secure_filename` |

---

## 5️⃣ Récapitulatif rapide (cheat‑sheet)