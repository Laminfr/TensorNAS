from enum import Enum, auto

from TensorNAS.Core.Block import Block
from TensorNAS.Layers.Dense import Args as dense_args


class SqueezeExpansionBlockLayerTypes(Enum):

    """Contains Global Average Pool layer and then Fully connected Layers with ReLu types and output dense layer with sigmoid activation function"""

    GLOBAL_AVERAGE_POOLING2D = auto()
    HIDDENDENSE = auto()
    OUTPUTDENSE = auto()


class Block(Block):

    MAX_SUB_BLOCKS = 2
    SUB_BLOCK_TYPES = SqueezeExpansionBlockLayerTypes

    def __init__(self, input_shape, parent_block, class_count, layer_type=-1):
        self.class_count = class_count

        super().__init__(input_shape, parent_block, layer_type)

    def generate_constrained_input_sub_blocks(self, input_shape):
        from TensorNAS.Layers.Pool.GlobalAveragePool2D import (
            Layer as GlobalAveragePool2D,
        )

        return [
            GlobalAveragePool2D(
                input_shape=None,
                parent_block=self,
            )
        ]

    def generate_constrained_output_sub_blocks(self, input_shape):
        """Use of input_shape=None causes the input shape to be resolved from the previous layer."""
        from TensorNAS.Layers.Dense.OutputDense import Layer as OutputDense

        return [
            OutputDense(
                input_shape=None,
                parent_block=self,
                args={dense_args.UNITS: self.class_count},
            )
        ]

    def generate_random_sub_block(self, input_shape, layer_type):
        from TensorNAS.Layers.Dense.HiddenDense import Layer as HiddenDense

        return [
            HiddenDense(
                input_shape=None,
                parent_block=self,
                args={dense_args.UNITS: self.class_count},
            )
        ]
