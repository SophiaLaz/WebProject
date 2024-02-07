import pytest
from actor import Actor


def _get_actor():
    name, info, image, link = "Alex", "The best programmer", "His photo", "https://t.me/Alex2_000"
    return Actor(name, info, image, link)


def test_dict_correctness():
    actor = _get_actor()
    assert actor.create_dict() == {'name': actor.name, 'info': actor.info, 'image': actor.image,
                                   'link': actor.link, 'color': actor._get_color()}, \
        "Fields in actor's dictionary are incorrect!"


def test_color_correctness():
    actor = _get_actor()
    color = actor._get_color()
    correct_color = "rgb(64, 201, 116)"
    assert color == correct_color, "Color is incorrect!"
