# Customer Clustering App

This project segments mall customers into meaningful clusters using KMeans unsupervised learning. Built with Streamlit and modularized in Python.

## 🎯 Project Goals

- 📈 Cluster customers based on income and spending behavior
- 📊 Visualize clusters to understand market segmentation
- 🧪 Apply unsupervised learning using `KMeans`

## 📁 Folder Structure

Customer_Clustering_App/
│
├── data/
│ └── mall_customers.csv
├── src/
│ ├── dataloader.py
│ ├── preprocessing.py
│ ├── model.py
│ └── utils.py
├── app.py
├── requirements.txt
├── README.md
└── .streamlit/
└── config.toml

## ⚙️ How to Run

1. Clone the repo  
2. Install required libraries:

```bash
pip install -r requirements.txt
streamlit run app.py
📘 Dataset
File: mall_customers.csv

Columns used:

Annual Income (k$)

Spending Score (1-100)

📦 Features
Allows user to select number of clusters (K)

Performs standard scaling

Trains KMeans model and visualizes customer segments

Displays cluster centers and color-coded customer groups
## 🌐 Live App

You can try the deployed Streamlit app here:  
🔗 [Customer Clustering App](https://customerclusteringapp-russel.streamlit.app/)
