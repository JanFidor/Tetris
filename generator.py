# DONE

from random import choice
import block

BLOCKS = [
    block.IBlock,
    block.JBlock,
    block.LBlock,
    block.OBlock,
    block.SBlock,
    block.TBlock,
    block.ZBlock,
    ]


def generate_random_block():
    """
    Returns random block from BLOCKS

    Returned: random block
    """
    return choice(BLOCKS)()
