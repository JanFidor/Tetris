from block_falling import BlockFalling


class OperationStrategy:
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


class GoLeft(OperationStrategy):
    def _new_blocks_positions(block: BlockFalling):
        return tuple((x - 1, y) for x, y in block.get_blocks())

    def change_position(block: BlockFalling):
        x, y = block.location
        block.location = x - 1, y


class GoRight(OperationStrategy):
    def _new_blocks_positions(block: BlockFalling):
        return tuple((x + 1, y) for x, y in block.get_blocks())

    def change_position(block: BlockFalling):
        x, y = block.location
        block.location = x + 1, y


class GoDown(OperationStrategy):
    def _new_blocks_positions(block: BlockFalling):
        return tuple((x, y - 1) for x, y in block.get_blocks())

    def change_position(block: BlockFalling):
        x, y = block.location
        block.location = x, y - 1


class TurnLeft(OperationStrategy):
    def _new_blocks_positions(block: BlockFalling):
        return block.block().get_left_position()

    def change_position(block: BlockFalling):
        block.block().turn_left()


class TurnRight(OperationStrategy):
    def _new_blocks_positions(block: BlockFalling):
        return block.block().get_right_position()

    def change_position(block: BlockFalling):
        block.block().turn_right()
