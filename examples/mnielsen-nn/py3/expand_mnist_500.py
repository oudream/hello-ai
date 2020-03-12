"""expand_mnist.py
~~~~~~~~~~~~~~~~~~

Take the 50,000 MNIST training images, and create an expanded set of
250,000 images, by displacing each training image up, down, left and
right, by one pixel.  Save the resulting file to
../data/mnist_expanded.pkl.gz.

Note that this program is memory intensive, and may not run on small
systems.

"""

from __future__ import print_function

#### Libraries

# Standard library
import _pickle as cPickle
import gzip
import os.path
import random

# Third-party libraries
import numpy as np

print("Expanding the MNIST training set")

if os.path.exists("../data/mnist_expanded.pkl.gz"):
    print("The expanded training set already exists.  Exiting.")
else:
    f = gzip.open("../data/mnist.pkl.gz", 'rb')
    training_data, validation_data, test_data = cPickle.load(f, encoding="latin1")
    f.close()

    training_data = (training_data[0][:500], training_data[1][:100])
    validation_data = (validation_data[0][:100], validation_data[1][:100])
    test_data = (test_data[0][:100], test_data[1][:100])
    print("Saving expanded data. This may take a few minutes.")
    f = gzip.open("../data/mnist_expanded.pkl.gz", "w")
    cPickle.dump((training_data, validation_data, test_data), f)
    f.close()
