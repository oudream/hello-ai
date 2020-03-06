
from matplotlib import pyplot as plt
import numpy
import math #needed for definition of pi

x = numpy.arange(0, math.pi*2, 0.05)
y = numpy.sin(x)

plt.plot(x,y)
plt.xlabel("angle")
plt.ylabel("sine")
plt.title('sine wave')
plt.show()
