import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    return (r1, r2, np.array([[mandelbrot(complex(r, i), max_iter) for r in r1] for i in r2]))

def mandelbrot_image(xmin, xmax, ymin, ymax, width=10, height=10, max_iter=256, cmap='hot'):
    dpi = 72
    img_width = dpi * width
    img_height = dpi * height
    x, y, m_set = mandelbrot_set(xmin, xmax, ymin, ymax, img_width, img_height, max_iter)

    fig, ax = plt.subplots(figsize=(width, height), dpi=dpi)
    ticks = np.arange(0, img_width, 3*dpi)
    x_ticks = xmin + (xmax-xmin)*ticks/img_width
    plt.xticks(ticks, np.round(x_ticks, 2))
    ticks = np.arange(0, img_height, 3*dpi)
    y_ticks = ymin + (ymax-ymin)*ticks/img_height
    plt.yticks(ticks, np.round(y_ticks, 2))

    ax.set_title("Mandelbrot Set")
    plt.imshow(m_set.T,origin='lower', cmap=cmap, extent=(xmin, xmax, ymin, ymax))
    plt.colorbar()
    plt.show()

mandelbrot_image(-2.0, 0.5, -1.25, 1.25, width=6, height=6, max_iter=256, cmap='hot')
