from enum import Enum, auto

from tensornas.core.layer import NetworkLayer
from tensornas.core.util import MutationOperators, mutate_tuple, mutate_enum
import tensornas.core.layerargs as la


class Args(Enum):
    "Args needed for creating MaxPool2D layer, list not complete"
    POOL_SIZE = auto()
    STRIDES = auto()
    PADDING = auto()


class Layer(NetworkLayer):
    MAX_POOL_SIZE = 7
    MAX_STRIDE = 7

    def _mutate_pool_size(self, operator=MutationOperators.SYNC_STEP):
        self.args[self.get_args_enum().POOL_SIZE.value] = mutate_tuple(
            self.args[self.get_args_enum().POOL_SIZE.value],
            1,
            self.MAX_POOL_SIZE,
            operator=operator,
        )

    def _mutate_strides(self, operator=MutationOperators.SYNC_STEP):
        self.args[self.get_args_enum().STRIDES.value] = mutate_tuple(
            self.args[self.get_args_enum().STRIDES.value],
            1,
            self.MAX_STRIDE,
            operator=operator,
        )

    def _mutate_padding(self):
        self.args[self.get_args_enum().PADDING.value] = mutate_enum(
            self.args[self.get_args_enum().PADDING.value], la.ArgPadding
        )

    def validate(self, repair=True):
        if not all(i > 0 for i in self.args[self.get_args_enum().STRIDES.value]):
            if repair:
                while not self.validate(repair):
                    self.repair()
            return False
        if not all(i > 0 for i in self.args[self.get_args_enum().POOL_SIZE.value]):
            if repair:
                while not self.validate(repair):
                    self.repair()
            return False