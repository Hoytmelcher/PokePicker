from . import bp as poke_bp
from flask import render_template, redirect, url_for
import requests
from app.forms import PokemonForm
from flask_login import login_required, current_user
from app.blueprints.user.models import User
from .models import CollectedPokemon


user_input = []
@poke_bp.route('/pokemon', methods=['GET', 'POST'])
@login_required
def pick_pokemon():
    poke = PokemonForm()
    pokemon = poke.pokemon.data
    if poke.validate_on_submit():
        user_input.clear() 
        req = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}')
        data = req.json()
        
        user_input.append(data['name'])
        
        abilities = data['abilities']
        abilities = list(map(lambda x: x['ability']['name'], abilities))
    
        types = data['types']
        types = list(map(lambda x: x['type']['name'], types))
    
        stats = data['stats']
        stats = list(map(lambda x: x['stat']['name'], stats))
    
        base_stat = data['stats']
        base_stat = list(map(lambda x: x['base_stat'], base_stat))
        return render_template('pokemon.jinja', poke=poke, data=data, abilities=abilities, types=types, stats=stats, base_stat=base_stat)  
    
    return render_template('pokemon.jinja', poke=poke)

@poke_bp.route('/user/<username>')
def user(username):
    user_match = User.query.filter_by(username=username).first()
    if not user_match:
        redirect('/')
    box = user_match.box
    return render_template('collection.jinja', user=user_match, box=box)

@poke_bp.route('/pokemon', methods=['GET', 'POST'])
def collect_card():
    poke = PokemonForm()
    pokemon = user_input[0]
    card = CollectedPokemon(pokemon=pokemon, user_id=current_user.id)
    card.commit()
    return render_template('collection.jinja', poke=poke)

@poke_bp.route('/poke/<pokemon>,<username>', methods=['GET', 'POST'])
def show_card(pokemon, username):
    user_match = User.query.filter_by(username=username).first()
    if not user_match:
        redirect('/')
    box = user_match.box
    req = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}')
    data = req.json()
    
    
    abilities = data['abilities']
    abilities = list(map(lambda x: x['ability']['name'], abilities))

    types = data['types']
    types = list(map(lambda x: x['type']['name'], types))

    stats = data['stats']
    stats = list(map(lambda x: x['stat']['name'], stats))

    base_stat = data['stats']
    base_stat = list(map(lambda x: x['base_stat'], base_stat))
    return render_template('collection.jinja', user=user_match, box=box, data=data, abilities=abilities, types=types, stats=stats, base_stat=base_stat)


