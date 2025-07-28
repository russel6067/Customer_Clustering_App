from sklearn.cluster import KMeans

def train_model(X, n_clusters):
    """
    Trains a KMeans model and returns both the model and predicted labels.

    Parameters:
        X (ndarray): Scaled input data with features (e.g., income and spending score)
        n_clusters (int): Number of clusters to form

    Returns:
        model (KMeans): Trained KMeans model
        labels (ndarray): Cluster labels assigned to each data point
    """
    model = KMeans(n_clusters=n_clusters, random_state=42, n_init='auto')
    labels = model.fit_predict(X)
    return model, labels
