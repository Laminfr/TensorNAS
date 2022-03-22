from TensorNAS.Core.BlockArchitecture import ClassificationBlockArchitecture
from enum import Enum, auto


class Block(ClassificationBlockArchitecture):

    MAX_SUB_BLOCKS = 2
    MIN_SUB_BLOCKS = 1

    class SubBlocks(Enum):

        FEATURE_EXTRACTION_BLOCK = auto()
        CLASSIFICATION_BLOCK = auto()

    def generate_constrained_output_sub_blocks(self, input_shape):
        from TensorNAS.Blocks.SubBlocks.TwoDClassificationBlock import (
            Block as TwoDClassificationBlock,
        )

        return [
            TwoDClassificationBlock(
                input_shape=input_shape,
                parent_block=self,
                class_count=self.class_count,
            )
        ]

    def generate_random_sub_block(self, input_shape, subblock_type):
        from TensorNAS.Blocks.SubBlocks.FeatureExtractionBlock import (
            Block as FeatureExtractionBlock,
        )
        from TensorNAS.Blocks.SubBlocks.TwoDClassificationBlock import (
            Block as ClassificationBlock,
        )

        if subblock_type == self.SubBlocks.FEATURE_EXTRACTION_BLOCK:
            return [FeatureExtractionBlock(input_shape=input_shape, parent_block=self)]
        elif subblock_type == self.SubBlocks.CLASSIFICATION_BLOCK:
            return [
                ClassificationBlock(
                    input_shape=input_shape,
                    parent_block=self,
                    class_count=self.class_count,
                )
            ]
        return []
