import numpy as np
import matplotlib.pyplot as plt

xs = np.linspace(-10, 10, 10)
ys = np.linspace(-10, 10, 10)
X, Y = np.meshgrid(xs, ys)

S1 = X
S2 = Y

r0 = 100

# Define the gain function (resistor h bridge)
def gain(r0, dr1, dr2, dr3, dr4):
    r1 = r0 + dr1
    r2 = r0 + dr2
    r3 = r0 + dr3
    r4 = r0 + dr4

    return r3/(r1+r3) - r4/(r2+r4)


plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


surfs = []

# Plot the surfaces
surfs.append(ax.plot_surface(X, Y, gain(r0, dr1=S1, dr3=S2, dr2=S1, dr4=S2), color='b', alpha=0.5, label="S1 top S2 bottom"))
surfs.append(ax.plot_surface(X, Y, gain(r0, dr1=S1, dr3=S2, dr2=S2, dr4=S1), color='r', alpha=0.5, label="Diagonal mirror"))
surfs.append(ax.plot_surface(X, Y, gain(r0, dr1=0, dr3=0, dr2=0, dr4=S1), color='purple', alpha=0.5, label="R4=S1"))
surfs.append(ax.plot_surface(X, Y, gain(r0, dr1=0, dr3=0, dr2=S2, dr4=S1), color='orange', alpha=0.5, label="R2=S2, R4=S1"))
surfs.append(ax.plot_surface(X, Y, gain(r0, dr1=S1, dr3=0, dr2=0, dr4=S2), color='green', alpha=0.5, label="R1=S1, R4=S2"))

for surf in surfs:
    surf._edgecolors2d = surf._edgecolor3d
    surf._facecolors2d = surf._facecolor3d

ax.legend(loc="upper left")

# Set labels
ax.set_xlabel('dr sensor 1')
ax.set_ylabel('dr sensor 2')
ax.set_zlabel('gain')

# Show the plot
plt.show()
