from matplotlib import pyplot as plt
import numpy as np

def shade_area(x, y, above=True):
    plt.fill_between(x, y, where=(y >= 0) if above else (y <= 0), 
                     color='gray', alpha=0.5, label='Shaded Area')

def shade_between(x, y1, y2):
    plt.fill_between(x, y1, y2, where=(y1 >= y2), color='gray', alpha=0.5, label='Shaded Area')