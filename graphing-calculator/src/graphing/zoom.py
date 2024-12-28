def zoom_in(ax, factor=1.2):
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    
    ax.set_xlim([x / factor for x in xlim])
    ax.set_ylim([y * factor for y in ylim])
    ax.figure.canvas.draw()

def zoom_out(ax, factor=1.2):
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    
    ax.set_xlim([x * factor for x in xlim])
    ax.set_ylim([y / factor for y in ylim])
    ax.figure.canvas.draw()