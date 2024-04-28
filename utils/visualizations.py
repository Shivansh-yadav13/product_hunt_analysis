import seaborn as sns
import matplotlib.pyplot as plt

def bar_plot(data, x, hue, y, legend):
    # visualizing using histogram
    ax = sns.barplot(
        data=data,
        x=x,
        y=y,
        hue=hue,
        legend=legend
    )

    for p in ax.patches:
        ax.text(p.get_x() + p.get_width() / 2., p.get_height(),
                '{:1.0f}'.format(p.get_height()),
                ha="center", va="bottom")

    plt.show()

def pie_plot(data, x=None, labels=None, pcolor='muted6'):

    palette_color = sns.color_palette(pcolor)

    x_ = None
    if x:
        x_ = x
    
    labels_ = None
    if labels:
        labels_ = labels

    plt.pie(
            data=data,
            x=x_,
            autopct="%1.2f%%",
            colors=palette_color,
            labels=labels_
        )

    plt.title("Ranks of Products")
    plt.show()