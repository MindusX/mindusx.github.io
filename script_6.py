# app/routes.py
from flask import (
    Blueprint, render_template, request,
    redirect, url_for, flash, abort
)
from . import db
from .models import Item
from .forms import ItemForm

main_bp = Blueprint("main", __name__)

# ----------------------------------------------------------------------
# Page d'accueil – liste tous les items
# ----------------------------------------------------------------------
@main_bp.route("/")
def index():
    items = Item.query.order_by(Item.id.desc()).all()
    return render_template("index.html", items=items)


# ----------------------------------------------------------------------
# Affichage d'un item (detail)
# ----------------------------------------------------------------------
@main_bp.route("/item/<int:item_id>")
def item_detail(item_id):
    item = Item.query.get_or_404(item_id)
    return render_template("item_detail.html", item=item)


# ----------------------------------------------------------------------
# Liste paginée d'items (facultatif)
# ----------------------------------------------------------------------
@main_bp.route("/items")
def item_list():
    items = Item.query.all()
    return render_template("item_list.html", items=items)


# ----------------------------------------------------------------------
# Création d'un nouvel item (GET + POST)
# ----------------------------------------------------------------------
@main_bp.route("/item/create", methods=["GET", "POST"])
def item_create():
    form = ItemForm()
    if form.validate_on_submit():
        # Création de l’objet en base
        new_item = Item(name=form.name.data, description=form.description.data)
        db.session.add(new_item)
        db.session.commit()
        flash("Item créé avec succès !", "success")
        return redirect(url_for("main.item_detail", item_id=new_item.id))
    return render_template("item_form.html", form=form, title="Créer un item")


# ----------------------------------------------------------------------
# Modification d'un item
# ----------------------------------------------------------------------
@main_bp.route("/item/<int:item_id>/edit", methods=["GET", "POST"])
def item_edit(item_id):
    item = Item.query.get_or_404(item_id)
    form = ItemForm(obj=item)               # pré‑remplir le formulaire
    if form.validate_on_submit():
        item.name = form.name.data
        item.description = form.description.data
        db.session.commit()
        flash("Item mis à jour !", "success")
        return redirect(url_for("main.item_detail", item_id=item.id))
    return render_template("item_form.html", form=form, title="Modifier un item")


# ----------------------------------------------------------------------
# Suppression d'un item (POST uniquement)
# ----------------------------------------------------------------------
@main_bp.route("/item/<int:item_id>/delete", methods=["POST"])
def item_delete(item_id):
    item = Item.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    flash("Item supprimé !", "success")
    return redirect(url_for("main.index"))