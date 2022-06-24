from flask import request
from flask_restx import Resource, Namespace

from app.actors.actor import Actor
from app.backend.schemes.scene_json import SceneJson
from app.scene.ai import Ai
from app.scene.player import Player
from app.scene.scene import Scene

fight_ns = Namespace('fight')


def check_form(form):
    return 'actor' in form and 'enemy' in form and 'action' in form


def scene_from_dict(data) -> Scene:
    actor_unit = Actor.from_dict(data['actor'])
    enemy_unit = Actor.from_dict(data['enemy'])

    return Scene(Player(actor_unit), Ai(enemy_unit))


def get_redirect(scene: Scene):
    actor_result = 'win' if scene.units[0].owner.hit_points > 0 else 'lose'
    enemy_result = 'win' if scene.units[1].owner.hit_points > 0 else 'lose'

    return f'result?actor={actor_result}&enemy={enemy_result}'


@fight_ns.route('/action')
class FightView(Resource):

    def post(self):
        json = request.json

        if not check_form(json):
            return 'Bad request', 400

        scene = scene_from_dict(json)

        action = json['action']
        effect = scene.compile(action)

        scene_bundle = SceneJson()
        scene_dict = scene_bundle.to_dict(scene)

        redirect = get_redirect(scene) if scene.is_enough() else None

        response = {**scene_dict, 'effect': effect, 'redirect': redirect}

        return response, 200
