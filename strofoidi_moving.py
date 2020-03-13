import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from math import *
#Рациональное параметрическое представление строфоиды u = tg(φ):
#x=a*(t**2-1)(t**2+1)
#y=at(t**2-1)(t**2+1)

t = np.linspace(-2, 2, 2000)
all_a = [2, 5]                                 # набор а

for a in all_a:
    x = a * (t * t - 1) / (t * t + 1)
    y = a * t * (t * t - 1) / (t * t + 1)
    plt.plot(x, y, label="a = {}".format(a))


plt.plot([0 for i in y], 2 * y, color="black")  # ось X
plt.plot(2 * x, [0 for i in x], color="black")  # ось Y
# plt.grid()                                      # сетка
# plt.legend(shadow=True)                         # легенда
# plt.show()

xm = np.min(x) - 2.5
xM = np.max(x) + 2.5
ym = np.min(y) - 2.5
yM = np.max(y) + 2.5
N = 50
s = np.linspace(-2, 2, N)
xx = a * (s * s - 1) / (s * s + 1)
yy = a * s * (s * s - 1) / (s * s + 1)


# Create figure
fig = go.Figure(
    data=[go.Scatter(x=x, y=y,
                     mode="lines",
                     line=dict(width=2, color="blue")),
          go.Scatter(x=x, y=y,
                     mode="lines",
                     line=dict(width=2, color="blue"))],
    layout=go.Layout(
        xaxis=dict(range=[xm, xM], autorange=False, zeroline=False),
        yaxis=dict(range=[ym, yM], autorange=False, zeroline=False),
        title_text="Moving Point on a Curve", hovermode="closest",
        updatemenus=[dict(type="buttons",
                          buttons=[dict(label="Play",
                                        method="animate",
                                        args=[None])])]),
    frames=[go.Frame(
        data=[go.Scatter(
            x=[xx[k]],
            y=[yy[k]],
            mode="markers",
            marker=dict(color="red", size=10))])

        for k in range(N)]
)

fig.show()
