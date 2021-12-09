# DONE

from generator import BLOCKS, generate_random_block
import pytest


@pytest.mark.parametrize("index", range(len(BLOCKS)))
def test_generate_block(index, monkeypatch):
    def get_not_random(iterable):
        return iterable[index]

    monkeypatch.setattr("generator.choice", get_not_random)
    assert isinstance(generate_random_block(), BLOCKS[index])
