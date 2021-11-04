from enum import Enum, auto

import TensorNAS.Core.LayerArgs as la
from TensorNAS.Core.Layer import Layer
from TensorNAS.Core.LayerArgs import *
from TensorNAS.Core.Util import mutate_unit_interval


class Args(Enum):
    "Args needed for creating Dropout layer, list not complete"
    RATE = auto()


class Layer(Layer):
    MAX_RATE = 0.5

    def _gen_args(self, input_shape, args):

        max = la.gen_dropout(self.MAX_RATE)

        if args:
            if self.get_args_enum().RATE in args:
                max = args.get(self.get_args_enum().RATE)

        return {self.get_args_enum().RATE: max}

    def _mutate_rate(self):
        self.args[self.get_args_enum().RATE] = mutate_unit_interval(
            self.args[self.get_args_enum().RATE], 0, self.MAX_RATE
        )

    def get_output_shape(self):
        return self.inputshape.get()

    def get_keras_layers(self, input_tensor):
        import tensorflow as tf

        return tf.keras.layers.Dropout(
            rate=self.args.get(self.get_args_enum().RATE),
            input_shape=self.inputshape.get(),
        )(input_tensor)
