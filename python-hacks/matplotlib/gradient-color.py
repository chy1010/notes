import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


# copied from https://stackoverflow.com/questions/25668828/how-to-create-colour-gradient-in-python
def colorFader(c1, c2, mix=0):
    #fade (linear interpolate) from color c1 (at mix=0) to c2 (mix=1)
    c1 = np.array(mpl.colors.to_rgb(c1))
    c2 = np.array(mpl.colors.to_rgb(c2))
    return mpl.colors.to_hex((1 - mix) * c1 + mix * c2)


def main():

    c1 = '#1f77b4'  #blue
    c2 = 'green'  #green
    n = 500

    fig, ax = plt.subplots(figsize=(8, 5))
    for x in range(n + 1):
        ax.axvline(x, color=colorFader(c1, c2, x / n), linewidth=4)
    fig.savefig('temp/color_fading.jpg')
    plt.close(fig)


if __name__ == '__main__':
    main()