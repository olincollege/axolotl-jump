"""
Pytest for model.py file
"""

import pytest
import model

collision_cases = [
    # Check that the first obstacle does not collide.
    (model.Obstacle(30, 200), False),
    # Check that obstacle does not colide when off the window.
    (model.Obstacle(30, 1000), False),
    # Check that there is no collision if location is negative.
    (model.Obstacle(30, -80), False),
    # Check that the given obstacle triggers collision when fully overlapped.
    (model.Obstacle(30, 0), True),
    # Check that the obstacle triggers collision.
    (model.Obstacle(30, 10), True),
    # Check that collision from the behind is detected
    (model.Obstacle(30, -10), True),
]

boundary_case = [
    # Check that the character never goes below the boundary.
    False,
    # Check that the character doesn't go below the boundary while jumping.
    True
]

@pytest.mark.parametrize("obstacle, output", collision_cases)
def test_collision(obstacle, output):
    """
    Check that collisions are detected as expected.

    Args:
        states: a list containing state data
        output: list containg only swing state data.
    """
    model_test = model.Model()
    assert model_test.collision(obstacle) == output

@pytest.mark.parametrize("jumping", boundary_case)
def test_boundary(jumping):
    """
    Check that the character never goes below the boundary.

    Args:
        states: a list containing state data
        output: list containg only swing state data.
    """
    model_test = model.Model()
    for i in range(10):
        model_test.update(jumping)
        assert model_test.characterpos[1] >= 0

def test_jump():
    """
    Check that the character is jumping when jump is True.
    """
    model_test = model.Model()
    last_y = model_test.characterpos[1]
    model_test.update(True)
    assert model_test.characterpos[1] > last_y

def test_mid_jump():
    """
    Check that the character will not jump again if it is already jumping.
    """
    model_test = model.Model()
    model_test.characterpos[1] = 5
    last_y = model_test.characterpos[1]
    model_test.update(True)
    assert model_test.characterpos[1] == last_y
