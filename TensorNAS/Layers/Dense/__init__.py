from enum import Enum, auto

import tensorflow as tf

from TensorNAS.Core.Layer import Layer


class Args(Enum):
    "Args needed for creating Dense layer, list not complete"
    UNITS = auto()
    ACTIVATION = auto()


class Layer(Layer):

    MAX_UNITS = 1028

    def _gen_args(self, input_shape, args):
        import random
        from TensorNAS.Core.Layer import gen_activation

        class_count = random.randint(1, self.MAX_UNITS)
        activation = gen_activation()

        if args:
            if self.get_args_enum().ACTIVATION in args:
                from TensorNAS.Core.Layer import ArgActivations

                activation = ArgActivations(args.get(self.get_args_enum().ACTIVATION))
            if self.get_args_enum().UNITS:
                class_count = args.get(self.get_args_enum().UNITS)

        return {
            self.get_args_enum().UNITS: class_count,
            self.get_args_enum().ACTIVATION: activation,
        }

    def get_output_shape(self):
        return (1, self.args.get(self.get_args_enum().UNITS))

    def get_keras_layers(self, input_tensor):
        return tf.keras.layers.Dense(
            units=self.args.get(self.get_args_enum().UNITS),
            activation=self.args.get(self.get_args_enum().ACTIVATION).value(),
            input_shape=self.inputshape.get(),
        )(input_tensor)
