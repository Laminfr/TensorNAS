from enum import Enum, auto
from TensorNAS.Layers import SupportedLayers
from TensorNAS.BlockTemplates.SubBlocks.TwoDClassificationBlock import (
    Block as TwoDClassificationBlock,
)
from TensorNAS.Core.LayerBlock import Block as LayerBlock
from TensorNAS.BlockTemplates.SubBlocks.GhostBlock import Block as GhostBlock
from TensorNAS.Core.BlockArchitecture import BlockArchitecture


class GhostNetArchitectureSubBlocks(Enum):
    GHOST_BLOCK = auto()
    CLASSIFICATION_BLOCK = auto()
    CONV2D = auto()


class Block(BlockArchitecture):
    MAX_SUB_BLOCKS = 3
    SUB_BLOCK_TYPES = GhostNetArchitectureSubBlocks

    def __init__(self, input_shape, class_count, batch_size, optimizer):
        self.class_count = class_count

        super().__init__(
            input_shape,
            parent_block=None,
            layer_type=None,
            batch_size=batch_size,
            optimizer=optimizer,
        )

    def generate_constrained_input_sub_blocks(self, input_shape):
        return [
            LayerBlock(
                input_shape=input_shape,
                parent_block=self,
                layer_type=SupportedLayers.CONV2D,
            )
        ]

    def generate_constrained_output_sub_blocks(self, input_shape):
        return [
            TwoDClassificationBlock(
                input_shape=input_shape,
                parent_block=self,
                class_count=self.class_count,
                layer_type=self.SUB_BLOCK_TYPES.CLASSIFICATION_BLOCK,
            )
        ]

    def generate_random_sub_block(self, input_shape, layer_type):
        return [
            GhostBlock(
                input_shape=input_shape, parent_block=self, layer_type=layer_type
            )
        ]
