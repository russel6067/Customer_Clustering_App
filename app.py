import streamlit as st
import pandas as pd
from src.data_loader import load_customer_data
from src.preprocessing import preprocess_data
from src.model import train_model
from src.utils import plot_clusters

# App title
st.set_page_config(page_title="Customer Segmentation App", layout="centered")
st.title("🛍️ Customer Segmentation using K-Means Clustering")
st.markdown("Upload your dataset or use the default Mall Customers dataset to explore customer segments.")

# Load default data
DATA_PATH = "data/mall_customers.csv"
df = load_customer_data(DATA_PATH)

# Show dataset preview
with st.expander("🔍 Preview Dataset"):
    st.dataframe(df)

# Choose number of clusters
n_clusters = st.slider("Select Number of Clusters (K):", min_value=2, max_value=10, value=5)

# Preprocess data
X_scaled = preprocess_data(df)

# Train K-Means model
model, cluster_labels = train_model(X_scaled, n_clusters)

# Display cluster counts
cluster_counts = pd.Series(cluster_labels).value_counts().sort_index()
st.write("### 📊 Number of Customers in Each Cluster")
st.bar_chart(cluster_counts)

# Plot clusters
fig = plot_clusters(X_scaled, cluster_labels, n_clusters)
st.pyplot(fig)

# Add a note
st.markdown("""
---
Made with ❤️ using Streamlit · [GitHub](https://github.com)
""")