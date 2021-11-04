from TensorNASDemos.Datasets.MNIST import input_tensor_shape, mnist_class_count
from TensorNAS.BlockTemplates.BlockArchitectures import ClassificationBlockArchitecture
from TensorNAS.Core.Crossover import crossover_cutting_point

print("###########################")
print("Auto example")
print("###########################")

print("First model architecture\n")
model1 = ClassificationBlockArchitecture.ClassificationBlockArchitecture(
    input_tensor_shape, mnist_class_count
)
print(model1.get_ascii_tree() + "\n\n")

print("###########################")
print("Second model architecture\n")
model2 = ClassificationBlockArchitecture.ClassificationBlockArchitecture(
    input_tensor_shape, mnist_class_count
)
print(model2.get_ascii_tree() + "\n\n")

print("###########################")
crossover_cutting_point(model1, model2, 2)
print("Crossed over")
print("###########################")

print("First model architecture\n")
print(model1.get_ascii_tree() + "\n\n")
print("###########################")

print("Second model architecture\n")
print(model2.get_ascii_tree() + "\n\n")

model2.print()
