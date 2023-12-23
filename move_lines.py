import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.use("TkAgg")


def show_normalize(x, y):
    plt.plot(x, y)
    plt.show()


if __name__ == '__main__':
    x_arr = np.arange(-100, 100, 1).astype(np.float32)
    y_arr = np.random.normal(loc=1, scale=2, size=(200,))
    show_normalize(x_arr, y_arr)
