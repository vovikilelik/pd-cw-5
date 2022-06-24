from random import choice

from flask import render_template, request

from app.actors.actor import Actor
from app.actors.classes.random import get_light_armor, get_light_weapon, get_heavy_weapon, get_heavy_armor, \
    get_middle_armor
from app.actors.classes.thief import get_thief_actor_class, get_thief_skill
from app.actors.classes.warrior import get_warrior_actor_class, get_warrior_skill
from app.backend.api import fight_ns
from app.backend.config import app, app_api
from app.backend.schemes.scene_json import SceneJson
from app.items.armor import Armor
from app.items.weapon import Weapon
from app.scene.ai import Ai
from app.scene.player import Player
from app.scene.scene import Scene


def create_class(actor_class_name):
    if actor_class_name == 'thief':
        return get_thief_actor_class()
    else:
        return get_warrior_actor_class()


def create_weapon(actor_class_name):
    if actor_class_name == 'thief':
        return get_light_weapon()
    else:
        return get_heavy_weapon()


def create_skill(actor_class_name):
    if actor_class_name == 'thief':
        return get_thief_skill()
    else:
        return get_warrior_skill()


def create_items(actor_class_name, character):
    base = {
        'weapon': create_weapon(actor_class_name),
        'skill': create_skill(actor_class_name)
    }

    if character == 'light':
        return {
            'armor': get_light_armor(),
            **base
        }
    elif character == 'middle':
        return {
            'armor': get_middle_armor(),
            **base
        }
    else:
        return {
            'armor': get_heavy_armor(),
            **base
        }


def create_actor(name, actor_class_name, character) -> Actor:
    return Actor(
        name=name,
        actor_class=create_class(actor_class_name),
        **create_items(actor_class_name, character)
    )


CLASS_NAMES = ['thief', 'warrior']
CHARACTERS = ['light', 'middle', 'heavy']


def create_random_actor(name='Компуктер'):
    return create_actor(name, choice(CLASS_NAMES), choice(CHARACTERS))


def create_scene(player: Actor):
    ai = Ai(create_random_actor())
    return Scene(Player(player), ai)


@app.route('/hero')
def index():
    return render_template('index.html')


@app.route('/fight', methods=['POST', 'GET'])
def fight():
    name = request.form.get('name', 'Нейм, Ноу Нейм')
    actor_class_name = request.form.get('actorClass', choice(CLASS_NAMES))
    character = request.form.get('character', choice(CHARACTERS))

    player = create_actor(name=name, actor_class_name=actor_class_name, character=character)

    scene = create_scene(player)

    scene_bundle = SceneJson()
    player_data = scene_bundle.to_json(scene)

    return render_template('fight.html', init_data=f"'{player_data}'")


@app.route('/result', methods=['GET'])
def result():
    actor_result = request.args.get('actor')
    enemy_result = request.args.get('enemy')

    message = ''

    if actor_result == 'lose' and enemy_result == 'lose':
        message = 'Вы оба пали, как козявки!'
    elif actor_result == 'win':
        message = 'Ты победил, Герой!'
    else:
        message = 'Это фиаско, братан!'

    return render_template('result.html', message=message)


def init_routes():
    app_api.add_namespace(fight_ns)
