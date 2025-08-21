# Phishing Website Classifier

A full-stack machine learning project for detecting phishing websites using both URL and website content analysis. This repository contains:

- **Backend**: Node.js + Python API for ML-powered phishing detection
- **Frontend**: React web app for user interaction
- **Training**: Jupyter notebooks for model development

---

## 🚀 Features

- **Dual Analysis**: Detects phishing using both URL patterns and website HTML content
- **Machine Learning Models**: Trained with scikit-learn, XGBoost, and more
- **Real-Time Detection**: Fast API for instant results
- **Confidence Scoring**: Shows reliability of predictions
- **Robust Error Handling**: Graceful handling of inaccessible sites and API failures
- **Modern UI**: Responsive React frontend

---

## 🏗️ Project Structure

```
phishing-website-detector-backend/   # Node.js + Python backend API
phishing-website-detector-frontend/  # React frontend
training/                            # Jupyter notebooks for model training
```

---

## 🧠 Model Training

- Jupyter notebooks in `training/` show the full process:
  - Data loading, cleaning, and exploration
  - Feature engineering for both URLs and HTML code
  - Training multiple ML models (SVC, XGBoost, Random Forest, etc.)
  - Model comparison and selection
  - Exporting best models as `.joblib` files for backend use

---

## 🖥️ Backend

- **Node.js Express server** (`src/index.js`): Handles API requests, fetches website content using Puppeteer, communicates with Python ML service
- **Python Flask API** (`src/api.py`): Loads trained models and performs predictions
- **Model files** (`utilities/`): Pre-trained `.joblib` models for URL and content analysis

### Backend Setup

1. **Install Node.js and Python (3.7+)**
2. **Install Python dependencies**:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install flask joblib scikit-learn==1.2.2 xgboost numpy==1.26.4 pandas
   ```
3. **Install Node.js dependencies**:
   ```bash
   npm install
   ```
4. **Start services**:
   - Python ML API: `python src/api.py`
   - Node.js server: `npm start`

### API Endpoints

- `POST /predict-url` — Analyze a URL for phishing
- `GET /` — Health check

See backend README for full details.

---

## 🌐 Frontend

- **React 19 + Vite** for fast development
- **Main component**: `src/App.jsx`
- **Sample URLs**: `test url.txt`

### Frontend Setup

1. **Install Node.js (16+)**
2. **Install dependencies**:
   ```bash
   npm install
   ```
3. **Configure backend URL** in `src/App.jsx`
4. **Run development server**:
   ```bash
   npm run dev
   ```
5. **Build for production**:
   ```bash
   npm run build
   ```

See frontend README for more info.

---

## 🔬 How It Works

1. **User enters a URL** in the frontend
2. **Frontend sends request** to backend API
3. **Backend fetches website content** and runs both URL and content analysis
4. **ML models predict** phishing status and confidence
5. **Frontend displays results** with detailed breakdown

---

## 📊 Training Notebooks

- Located in `training/`
- Show full ML workflow for both URL and HTML code analysis
- Export models for backend use

---

## 🛡️ Security & Best Practices

- Input validation and sanitization
- CORS enabled for API
- No sensitive data stored
- Rate limiting and resource monitoring recommended for production

---

## 🐞 Troubleshooting

- Ensure all dependencies are installed
- Check model files in backend `utilities/`
- Verify backend API URL in frontend
- See individual component READMEs for more help

---


For more details, see the individual READMEs in each folder.

---
