# CryptoQuik
Real-time ML System, quick predictions for crypto markets

## Building a Real-Time ML System
Together, we will create a real-time machine learning system for predicting cryptocurrency prices. This document outlines the required tools, steps, and progress.
![CryptoQuik System Diagram](D:\CryptoQuik\media\image.png "ML-System for Real time Crpto Price Prediction")


---

## Tools

1. **Code Editors**
   - **Cursor**: [https://www.cursor.com/](https://www.cursor.com/)
   - **Visual Studio Code**: [https://code.visualstudio.com/](https://code.visualstudio.com/)

2. **Feature Pipeline Steps**
   - **Ingest trades from external API**: Fetch real-time trade data from external APIs.
   - **Transform trades into technical indicators**: Convert raw trade data into meaningful technical indicators (e.g., moving averages, RSI).
   - **Save these tech indicators to a Feature Store**: Store these indicators efficiently for model training and inference.

3. **UV Tool**
   - Documentation: [https://docs.astral.sh/uv/getting-started/installation/](https://docs.astral.sh/uv/getting-started/installation/)

4. **Docker**
   - Used for containerization and orchestration.

---

## About the Project
CryptoQuik is a real-time machine learning system for predicting cryptocurrency prices. The system ingests data from APIs, processes it into meaningful features, and makes predictions using advanced ML models. Predictions are displayed on a dashboard, enabling quick decision-making in the fast-paced crypto markets.

### Features
- **Real-Time Data Ingestion**: Pull data from News APIs and Trade APIs.
- **Feature Engineering**: Generate technical indicators and sentiment scores.
- **Feature Store**: Store processed features for model training and prediction.
- **Prediction API**: Expose predictions via an API for real-time use.
- **Monitoring**: ElasticSearch integration for tracking predictions and model errors.

### ML System Overview
1. **Data Ingestion**: Collect real-time data from multiple sources, including News APIs (for sentiment analysis) and Trades APIs (for OHLC data).
2. **Feature Engineering**: Convert raw data into market sentiment scores and technical indicators, saving these to a centralized feature store.
3. **Model Training**: Use features from the store to train predictive models, storing model files and metadata in a model registry.
4. **Real-Time Prediction**: Deploy models for live price predictions via an API.
5. **Monitoring and Alerts**: Use ElasticSearch for logging predictions and model errors, and trigger alerts for anomalies or significant market events.

---

Stay tuned for further updates as development progresses!

