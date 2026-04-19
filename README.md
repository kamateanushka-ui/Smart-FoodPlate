# SmartFoodPlate 🍽️

AI-powered food analysis platform. Upload a photo of your meal and get instant nutritional insights.

---

## 📁 Project Structure

```
SmartFoodPlate/
├── Backend/
│   ├── app.py              ← Flask API (all routes)
│   ├── requirements.txt    ← Python dependencies
│   └── venv/               ← Python virtual environment
├── Frontend/
│   ├── index.html          ← Landing page + upload
│   ├── result.html         ← Results page
│   └── config.js           ← Centralized API URL config
└── README.md
```

---

## 🚀 How to Run

### Step 1 — Start the Backend

```bash
cd Backend
venv\Scripts\activate          # Windows
# source venv/bin/activate     # Mac/Linux

pip install -r requirements.txt
python app.py
```

Backend will start at → **http://localhost:5000**

---

### Step 2 — Open the Frontend

Open `Frontend/index.html` directly in your browser, **or** use a simple server to avoid CORS file-path issues:

```bash
# Option A: Python one-liner (recommended)
cd Frontend
python -m http.server 3000
# then open http://localhost:3000

# Option B: VS Code
# Install "Live Server" extension → right-click index.html → Open with Live Server
```

---

## 🔗 API Endpoints

| Method | Route | Description |
|--------|-------|-------------|
| GET | `/ping` | Health check |
| POST | `/analyze` | Upload image → nutritional analysis |
| POST | `/chatbot` | Ask DietBuddy a nutrition question |
| GET | `/history` | View all past analyses |
| GET | `/download-report/<id>` | Download PDF report |

### `/analyze` request format
```
Content-Type: multipart/form-data
Field: image  (file — JPG/PNG/WEBP/GIF/BMP, max 16MB)
```

### `/analyze` response format
```json
{
  "success": true,
  "message": "Analysis complete.",
  "analysis_id": "uuid-here",
  "data": {
    "detected_food": "Pizza",
    "calories": 285,
    "protein": 12,
    "carbs": 35,
    "fat": 11,
    "fiber": 2.5,
    "sugar": 3.6,
    "confidence": 0.93,
    "timestamp": "2024-01-01 12:00:00",
    "advice": ["⚠️ Low Fiber: Add some vegetables..."],
    "analysis_id": "uuid-here"
  }
}
```

---

## ⚙️ Configuration

To change the backend URL (e.g. for deployment), edit **`Frontend/config.js`**:

```js
const CONFIG = {
  API_BASE_URL: "http://localhost:5000"
  // Change ↑ to your deployed backend URL
};
```

---

## 🐛 Troubleshooting

| Problem | Fix |
|---------|-----|
| Upload button does nothing | Make sure you click "Upload Photo" — it opens your file picker |
| "Server Offline" badge shows | Backend is not running. Run `python app.py` first |
| Blank result page | You navigated to result.html directly without uploading. Go back to index.html |
| PDF download fails | The analysis session may have expired. Upload a new image |
| CORS errors in console | Make sure backend is running on port 5000 and `flask-cors` is installed |
