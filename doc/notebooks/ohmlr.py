import ohmlr

n_features = 16
n_x_classes = np.random.randint(2, 10, size=n_features)
n_y_classes = 8

model = ohmlr.ohmlr().random(n_features, n_x_classes, n_y_classes)
x, y = model.generate_data(n_samples=1000)
model.fit(x, y)
print(model.score(x, y))

# fig, ax = plt.subplots(1, 2, figsize=(8, 4))
# ax[0].plot(d, 'k-')
# lo = min(v.min(), np.vstack(w).min())
# hi = max(v.max(), np.vstack(w).max())
# grid = np.linspace(lo, hi)
# ax[1].plot(grid, grid, 'k--', alpha=0.5)
# ax[1].scatter(model.v, v, c='r', s=10)
# ax[1].scatter(np.vstack(model.w).flatten(), np.vstack(w).flatten(), c='b', s=1)
# ax[0].set_xlabel('iteration')
# ax[0].set_ylabel('discrepancy')
# ax[1].set_xlabel('fitted')
# ax[1].set_ylabel('true')
# plt.tight_layout()
# plt.show()
