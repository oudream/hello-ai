import mnist_loader
import network


training_data, validation_data, test_data = mnist_loader.load_data_wrapper()
training_data = list(training_data)

# training_data = (training_data[0][:500], training_data[1][:100])
# validation_data = (validation_data[0][:100], validation_data[1][:100])
# test_data = (test_data[0][:100], test_data[1][:100])

net = network.Network([784, 30, 10])
net.SGD(training_data, 30, 10, 3.0, test_data=test_data)
