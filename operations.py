from block_falling import BlockFalling


class Operation:
    """
    Operation model representing possible transforations of tetris block
    position, implements strategy design pattern
    """
    def _new_blocks_positions(block):
        """
        Returns new block relations to center after applying transformation

        Keyword arguments: block - falling block to which transformation will
        apply
        """
        pass

    @classmethod
    def next_position(cls, block: BlockFalling):
        """
        Returns positions of blocks after applying transformation inside the
        board

        Keyword arguments: cls - class
        Keyword arguments: block - falling block to which transformation will
        apply
        """
        loc_x, loc_y = block.location
        blocks = cls._new_blocks_positions(block)
        return tuple((x + loc_x, y + loc_y) for x, y in blocks)

    def change_position(block):
        """
        Changes position of block inside board

        Keyword arguments: block - falling block to which transformation will
        apply
        """
        pass


class GoLeft(Operation):
    def _new_blocks_positions(block: BlockFalling):
        return tuple((x - 1, y) for x, y in block.get_blocks())

    def change_position(block: BlockFalling):
        x, y = block.location
        block.location = x - 1, y


class GoRight(Operation):
    def _new_blocks_positions(block: BlockFalling):
        return tuple((x + 1, y) for x, y in block.get_blocks())

    def change_position(block: BlockFalling):
        x, y = block.location
        block.location = x + 1, y


class GoDown(Operation):
    def _new_blocks_positions(block: BlockFalling):
        return tuple((x, y - 1) for x, y in block.get_blocks())

    def change_position(block: BlockFalling):
        x, y = block.location
        block.location = x, y - 1


class TurnLeft(Operation):
    def _new_blocks_positions(block: BlockFalling):
        return block.get_inner_block().get_left_position()

    def change_position(block: BlockFalling):
        block.get_inner_block().turn_left()


class TurnRight(Operation):
    def _new_blocks_positions(block: BlockFalling):
        return block.get_inner_block().get_right_position()

    def change_position(block: BlockFalling):
        block.get_inner_block().turn_right()
