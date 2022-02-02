from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_user, login_required, current_user
from . models import Card
from . import db
import json, requests
from sqlalchemy.sql import func

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():   
    
    response = requests.get("https://db.ygoprodeck.com/api/v7/cardinfo.php")
    data = response.text
    parse_json = json.loads(data)
    languages = parse_json['data']

    if request.method == 'POST':

        card = request.form.get('card')
        num_cards = request.form.get("quantity")
        
        query = db.session.query(db.func.sum(Card.quantity)).scalar()

        if len(card) < 1:
            flash('Invalid Card Name', category = 'error')

        elif query != None and query + int(num_cards) > 18:
            flash('Maximum quantity has been reached', category = 'error')

        else:
            new_card = Card(data = card, quantity = num_cards, user_id = current_user.id)
            db.session.add(new_card)
            db.session.commit()
            flash('Card added!', category = 'success')


                                    #reference current usser
    return render_template("home.html", user=current_user, languages=languages)
@views.route('/delete-card', methods=['POST'])
def delete_card():
    card = json.loads(request.data)
    cardId = card['cardId']
    card = Card.query.get(cardId)

    if card:
        if card.user_id == current_user.id:
            db.session.delete(card)
            db.session.commit()
    return jsonify({})