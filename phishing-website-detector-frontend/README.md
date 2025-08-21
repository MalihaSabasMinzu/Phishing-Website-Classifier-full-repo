# Phishing Website Detector Frontend

A modern React-based web application that helps users identify potentially malicious phishing websites by analyzing URLs and website content. This frontend application communicates with a backend AI service to provide real-time phishing detection.

## 🚀 Features

- **URL Analysis**: Enter any website URL to check for phishing indicators
- **Real-time Detection**: Instant analysis using machine learning models
- **Dual Analysis**: Combines both URL pattern analysis and website content analysis
- **Clipboard Integration**: Easy paste functionality for URLs
- **Confidence Scoring**: Shows confidence levels for predictions
- **Detailed Results**: Comprehensive breakdown of analysis components
- **Responsive Design**: Works seamlessly across desktop and mobile devices
- **Error Handling**: Graceful handling of network issues and invalid URLs

## 🛠️ Technology Stack

- **Frontend Framework**: React 19.1.1
- **Build Tool**: Vite 7.1.0
- **Styling**: CSS3 with modern features
- **Code Quality**: ESLint with Airbnb configuration + Prettier
- **Development**: Hot reload and fast refresh

## 📋 Prerequisites

Before running this application, make sure you have:

- **Node.js** (version 16 or higher)
- **npm** or **yarn** package manager
- **Backend Service**: The phishing detection API service running (see backend configuration)

## 🔧 Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd phishing-website-detector-frontend
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Configure Backend URL**:
   - Open `src/App.jsx`
   - Update the API endpoint in the `handleSubmit` function:
   ```javascript
   const response = await fetch('YOUR_BACKEND_URL/predict-url', {
     // ... rest of the configuration
   });
   ```

## 🚀 Running the Application

### Development Mode
```bash
npm run dev
```
The application will start on `http://localhost:5173` with hot reload enabled.

### Production Build
```bash
npm run build
```
Creates an optimized production build in the `dist` folder.

### Preview Production Build
```bash
npm run preview
```
Serves the production build locally for testing.

### Code Linting
```bash
npm run lint
```
Runs ESLint to check for code quality issues.

## 📖 How It Works

### Analysis Process

1. **URL Input**: User enters a website URL or pastes from clipboard
2. **Backend Communication**: Frontend sends the URL to the backend API
3. **Dual Analysis**: The backend performs:
   - **URL Analysis**: Examines URL patterns, domain characteristics, and structure
   - **Content Analysis**: Scrapes and analyzes website content, HTML structure, and suspicious elements
4. **Result Processing**: The application receives and displays:
   - Final decision (Safe/Phishing)
   - Confidence level (High/Medium/Low)
   - Individual analysis results
   - Website accessibility status
   - Error details (if any)

### API Response Structure

The backend returns a JSON response with the following structure:

```json
{
  "webcode_prediction": 0|1|null,  // Content analysis result
  "url_prediction": 0|1|null,     // URL analysis result
  "final_decision": "Safe|Phishing detected",
  "confidence": "High|Medium|Low",
  "website_accessible": true|false,
  "analysis_complete": true|false,
  "note": "Additional information",
  "website_error": "Error message if applicable"
}
```

### Result Interpretation

- **webcode_prediction**: 
  - `0` = Safe content
  - `1` = Phishing content detected
  - `null` = Analysis unavailable (website not accessible)

- **url_prediction**:
  - `0` = Safe URL pattern
  - `1` = Suspicious URL pattern
  - `null` = Analysis failed

- **final_decision**: Combined result from both analyses
- **confidence**: Reliability of the prediction

## 🏗️ Project Structure

```
phishing-website-detector-frontend/
├── public/
│   └── vite.svg                 # Vite logo
├── src/
│   ├── assets/
│   │   ├── image.png           # Paste button icon
│   │   └── react.svg           # React logo
│   ├── App.css                 # Main application styles
│   ├── App.jsx                 # Main application component
│   ├── index.css               # Global styles
│   └── main.jsx                # Application entry point
├── eslint.config.js            # ESLint configuration
├── index.html                  # HTML template
├── package.json                # Dependencies and scripts
├── test url.txt               # Sample URLs for testing
├── vite.config.js             # Vite configuration
└── README.md                  # This file
```

## 🎨 Styling

The application uses modern CSS with:
- **Flexbox/Grid layouts** for responsive design
- **CSS Variables** for consistent theming
- **Custom animations** for loading states
- **Color-coded results** (red for phishing, green for safe)
- **Mobile-first approach** for responsive design

## 🧪 Testing

Sample test URLs are provided in `test url.txt`:
- Suspicious phishing URL (encoded)
- Legitimate websites (tutorialspoint.com, google.com)

## 🔒 Security Considerations

- **Input Validation**: URLs are validated before processing
- **HTTPS Communication**: Secure communication with backend
- **Error Sanitization**: User inputs are properly sanitized
- **No Sensitive Data Storage**: No user data is stored locally

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Code Style

This project uses:
- **ESLint** with Airbnb configuration
- **Prettier** for code formatting
- **React Hooks** for state management
- **Modern JavaScript (ES6+)** features


## 🐛 Troubleshooting

### Common Issues

1. **Backend Connection Error**:
   - Ensure the backend service is running
   - Check the API endpoint URL in `App.jsx`
   - Verify CORS configuration on the backend

2. **Clipboard Access Denied**:
   - Modern browsers require HTTPS for clipboard access
   - Use the manual input if clipboard paste fails

3. **Build Errors**:
   - Clear node_modules and reinstall: `rm -rf node_modules package-lock.json && npm install`
   - Check Node.js version compatibility

## 📞 Support

For support and questions:
- Create an issue in the repository
- Check the backend service documentation
- Ensure all dependencies are properly installed

---

**Note**: This is the frontend component of a phishing detection system. Make sure to have the corresponding backend service running for full functionality.