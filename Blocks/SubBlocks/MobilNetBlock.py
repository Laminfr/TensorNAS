from TensorNAS.Core.Block import Block
from enum import Enum, auto


class Block(Block):

    MAX_SUB_BLOCKS = 2

    class SubBlocks(Enum):

        SEPARABLE_CONV = auto()

    # input constrained layer for SqueezeBlock: 1x1xN_c Conv layer

    def generate_random_sub_block(self, input_shape, layer_type):
        from TensorNAS.Layers.Conv2D.SeparableConv2D import Layer as SeperableConv2D

        if layer_type == self.SubBlocks.SEPARABLE_CONV:
            return [
                SeperableConv2D(
                    input_shape=input_shape,
                    parent_block=self,
                )
            ]
