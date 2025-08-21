# Phishing Website Detector Backend

A comprehensive backend system for detecting phishing websites using machine learning models. This system analyzes both URL patterns and website content to provide accurate phishing detection.

## 🔍 What This Project Does

This backend service provides an API that can analyze websites and URLs to determine if they are potentially phishing sites. It uses two different machine learning approaches:

1. **URL Analysis**: Analyzes the structure and patterns in URLs using a LinearSVC model
2. **Website Content Analysis**: Analyzes the actual HTML content of websites using an XGBoost model

The system fetches websites using Puppeteer (headless browser) to get fully rendered HTML content and then applies both analysis methods to provide a comprehensive assessment.

## 🏗️ Architecture

The project consists of two main components:

- **Node.js Express Server** (`src/index.js`): Main API server that handles requests, fetches website content, and communicates with the Python ML service
- **Python Flask API** (`src/api.py`): Machine learning service that runs the trained models for prediction

## 🚀 Features

- **Dual Analysis**: Combines URL pattern analysis and website content analysis
- **Robust Error Handling**: Gracefully handles inaccessible websites and API failures
- **Headless Browser Support**: Uses Puppeteer to fetch fully rendered website content
- **CORS Enabled**: Ready for frontend integration
- **Confidence Scoring**: Provides confidence levels based on analysis results
- **Fallback Analysis**: Can analyze URL patterns even when websites are inaccessible

## 📋 Prerequisites

Before running this project, make sure you have the following installed:

### Required Software

- **Node.js** (v14 or higher)
- **Python** (v3.7 or higher)
- **npm** (comes with Node.js)

### Python Dependencies

The Python service requires the following packages:

- Flask
- joblib
- scikit-learn
- xgboost
- numpy
- pandas

### Node.js Dependencies

The Node.js server requires the following packages (already defined in package.json):

- express
- axios
- puppeteer
- cors
- nodemon (for development)

## 🛠️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/MalihaSabasMinzu/phishing-website-detector-backend.git
cd phishing-website-detector-backend
```

### 2. Set Up Python Environment

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Linux/macOS:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install Python dependencies
pip install flask joblib scikit-learn==1.2.2 xgboost numpy==1.26.4 pandas
```

### 3. Install Node.js Dependencies

```bash
npm install
```

### 4. Verify Machine Learning Models

Ensure the following model files are present in the `utilities/` directory:

- `linearsvc_url.joblib` - URL analysis model
- `vectorizer_url.joblib` - URL vectorizer
- `xgboost_webcode.joblib` - Website content analysis model
- `vectorizer_webcode.joblib` - Website content vectorizer

## 🏃‍♂️ How to Run

### Option 1: Manual Start (Recommended for Development)

1. **Start the Python ML Service** (Terminal 1):

```bash
source venv/bin/activate
python /workspaces/phishing-website-detector-backend/src/api.py
```

The Python service will start on `http://localhost:5000`

2. **Start the Node.js API Server** (Terminal 2):

```bash
npm start
```

The main API server will start on `http://localhost:3000`

### Option 2: Using the Command List

You can also use the commands listed in `command list.txt`:

```bash
# Terminal 1:
source venv/bin/activate
python /workspaces/phishing-website-detector-backend/src/api.py

# Terminal 2:
npm start
```

## 📡 API Usage

### Base URL

```
http://localhost:3000
```

### Endpoints

#### 1. Health Check

```http
GET /
```

Returns a welcome message to verify the server is running.

#### 2. Analyze URL for Phishing

```http
POST /predict-url
Content-Type: application/json

{
  "url": "https://example.com"
}
```

**Response Format:**

```json
{
	"website_accessible": true,
	"webcode_prediction": 0,
	"url_prediction": 1,
	"final_decision": "Likely Safe",
	"confidence": "Medium-High",
	"analysis_complete": true
}
```

**Response Fields:**

- `website_accessible`: Boolean indicating if the website could be fetched
- `webcode_prediction`: Result from content analysis (0=safe, 1=phishing, null=failed)
- `url_prediction`: Result from URL analysis (0=safe, 1=phishing, null=failed)
- `final_decision`: Human-readable final assessment
- `confidence`: Confidence level (High, Medium-High, Medium)
- `analysis_complete`: Boolean indicating if both analyses completed successfully

### Decision Logic

The system uses the following logic to determine the final result:

- **Both predictions available**:

  - Both predict phishing (1,1) → "Phishing" (High confidence)
  - Content=phishing, URL=safe (1,0) → "Likely Phishing" (Medium-High confidence)
  - Content=safe, URL=phishing (0,1) → "Likely Safe" (Medium-High confidence)
  - Both predict safe (0,0) → "Safe" (High confidence)

- **Only one prediction available**: Medium confidence with appropriate message

## 🔧 Configuration

### Port Configuration

- Node.js server: Port 3000 (configurable in `src/index.js`)
- Python ML service: Port 5000 (configurable in `src/api.py`)

### Puppeteer Configuration

The system uses headless Chrome via Puppeteer. You can modify browser settings in the `getRenderedHTML` function in `src/index.js`.

## 🧪 Testing

You can test the API using curl, Postman, or any HTTP client:

```bash
# Test with a legitimate website
curl -X POST http://localhost:3000/predict-url \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.google.com"}'

# Test with a suspicious URL pattern
curl -X POST http://localhost:3000/predict-url \
  -H "Content-Type: application/json" \
  -d '{"url": "https://paypal-security-update.suspicious-domain.com"}'
```

## 🐛 Troubleshooting

### Common Issues

1. **Python service not starting**:

   - Ensure all Python dependencies are installed
   - Check that model files exist in the `utilities/` directory
   - Verify Python virtual environment is activated

2. **Node.js service connection errors**:

   - Ensure Python service is running on port 5000
   - Check for port conflicts
   - Verify axios requests are pointing to correct Python service URL

3. **Puppeteer errors**:

   - Install Chrome dependencies: `sudo apt-get install -y chromium-browser`
   - For Docker environments, ensure proper Chrome setup

4. **Model loading errors**:
   - Verify all `.joblib` files are present and not corrupted
   - Check file permissions
   - Ensure compatible scikit-learn/xgboost versions

### Debug Mode

Enable debug logging by modifying the console.log statements in the code or by setting appropriate log levels.

## 📁 Project Structure

```
phishing-website-detector-backend/
├── src/
│   ├── index.js          # Main Node.js Express server
│   └── api.py            # Python Flask ML service
├── utilities/
│   ├── linearsvc_url.joblib       # URL analysis model
│   ├── vectorizer_url.joblib      # URL text vectorizer
│   ├── xgboost_webcode.joblib     # Content analysis model
│   └── vectorizer_webcode.joblib  # Content text vectorizer
├── package.json          # Node.js dependencies
├── command list.txt      # Quick start commands
└── README.md            # This file
```

## 🔒 Security Considerations

- Always validate and sanitize URLs before processing
- Consider implementing rate limiting to prevent abuse
- Monitor resource usage when fetching external websites
- Be cautious when analyzing suspicious websites in production

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📞 Support

For issues and questions, please open an issue on the GitHub repository.
