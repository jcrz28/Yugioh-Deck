from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_user, login_required, current_user
from . models import Card
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():   
    if request.method == 'POST':
        card = request.form.get('card')
        num_cards = request.form.get("quantity")
        print(num_cards)
        if len(card) < 1:
            flash('Invalid Card Name', category = 'error')
        else:
            new_card = Card(data = card, quantity = num_cards, user_id = current_user.id)
            db.session.add(new_card)
            db.session.commit()
            flash('Card added!', category = 'success')

                                    #reference current usser
    return render_template("home.html", user=current_user)
@views.route('delete-note', methods=['POST'])
def delete_card():
    card = json.loads(request.data)
    cardId = card['cardId']
    card = Card.query.get(cardId)

    if card:
        if card.user_id == current_user.id:
            db.session.delete(card)
            db.session.commit()
    return jsonify({})