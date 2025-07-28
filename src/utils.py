import matplotlib.pyplot as plt
import seaborn as sns

def plot_clusters(X, labels, n_clusters):
    """
    Plot clusters using the first two features in X.

    Parameters:
        X: 2D array or DataFrame with at least two features
        labels: Cluster labels
        n_clusters: Number of clusters

    Returns:
        matplotlib Figure object
    """
    # Use .iloc for Pandas DataFrame, or trust numpy slicing
    try:
        x_vals = X.iloc[:, 0]
        y_vals = X.iloc[:, 1]
    except AttributeError:
        # If it's a NumPy array, use direct slicing
        x_vals = X[:, 0]
        y_vals = X[:, 1]

    plt.figure(figsize=(8, 6))
    palette = sns.color_palette("Set2", n_colors=n_clusters)
    sns.scatterplot(x=x_vals, y=y_vals, hue=labels, palette=palette, s=100, alpha=0.8, edgecolor='k')
    plt.xlabel("Annual Income (scaled)")
    plt.ylabel("Spending Score (scaled)")
    plt.title("Customer Segments")
    plt.legend(title="Cluster")
    plt.tight_layout()
    return plt
