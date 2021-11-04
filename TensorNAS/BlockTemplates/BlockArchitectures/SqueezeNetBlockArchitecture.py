from enum import Enum, auto

from TensorNAS.Core.BlockArchitecture import BlockArchitecture


class SqueezeNetArchitectureSubBlocks(Enum):
    FIRE_BLOCK = auto()
    """Classification block some of the Layers like flatten is added to the input constrained block and  
     output dense is already added to the constrained output block"""


class Block(BlockArchitecture):
    MAX_SUB_BLOCKS = 3
    SUB_BLOCK_TYPES = SqueezeNetArchitectureSubBlocks

    def __init__(self, input_shape, class_count, batch_size, optimizer):
        self.class_count = class_count

        super().__init__(
            input_shape,
            parent_block=None,
            batch_size=batch_size,
            optimizer=optimizer,
        )

    def generate_constrained_output_sub_blocks(self, input_shape):
        from TensorNAS.BlockTemplates.SubBlocks.TwoDClassificationBlock import (
            Block as TwoDClassificationBlock,
        )

        return [
            TwoDClassificationBlock(
                input_shape=input_shape,
                parent_block=self,
                class_count=self.class_count,
            )
        ]

    def generate_random_sub_block(self, input_shape, layer_type):
        from TensorNAS.BlockTemplates.SubBlocks.FireBlock import Block as FireBlock

        if layer_type == self.SUB_BLOCK_TYPES.FIRE_BLOCK:
            return [FireBlock(input_shape=input_shape, parent_block=self)]
        return []