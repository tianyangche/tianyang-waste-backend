# tianyang-waste-backend

A Flask-based backend API for intelligent waste classification using OpenAI's GPT-4o-mini model. Classify items as Recycle, Compost, or Trash to help with proper waste disposal.

## Features

- 🤖 AI-powered waste classification using OpenAI GPT-4o-mini
- 📡 RESTful API endpoint for easy integration
- 🚀 Vercel deployment ready
- 🛠️ Local development support with auto port selection
- 🔒 Environment-based configuration for API keys

## Tech Stack

- **Python 3.13**
- **Flask** - Web framework
- **OpenAI API** - AI model for classification
- **python-dotenv** - Environment variable management
- **Vercel** - Deployment platform

## Prerequisites

- Python 3.13 or higher
- OpenAI API key
- pip (Python package manager)

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd tianyang-waste-backend
   ```

2. **Create and activate a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the root directory:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Usage

### Local Development

Run the Flask development server:
```bash
python api/classify.py
```

The server will automatically find an available port starting from 5000 and display the URL:
```
🚀 Flask server running on http://127.0.0.1:5000
```

### API Endpoint

**POST** `/classify`

Classify a waste item as Recycle, Compost, or Trash.

#### Request

```json
{
  "item": "plastic bottle"
}
```

#### Response

```json
{
  "item": "plastic bottle",
  "result": "Recycle - Plastic bottles are recyclable and should be placed in the recycling bin."
}
```

#### Error Responses

**400 Bad Request**
```json
{
  "error": "missing 'item'"
}
```

**500 Internal Server Error**
```json
{
  "error": "API error message"
}
```

### Example Usage

Using `curl`:
```bash
curl -X POST http://localhost:5000/classify \
  -H "Content-Type: application/json" \
  -d '{"item": "apple core"}'
```

Using Python:
```python
import requests

response = requests.post(
    "http://localhost:5000/classify",
    json={"item": "apple core"}
)
print(response.json())
```

## Deployment

### Vercel

This project is configured for easy deployment on Vercel:

1. **Install Vercel CLI** (optional)
   ```bash
   npm i -g vercel
   ```

2. **Deploy**
   ```bash
   vercel
   ```

3. **Set environment variables in Vercel**
   - Go to your project settings on Vercel
   - Add `OPENAI_API_KEY` in the Environment Variables section

The `vercel.json` configuration handles:
- Automatic Python build
- Route configuration for the debounce endpoint
- Serverless function setup

## Project Structure

```
tianyang-waste-backend/
├── api/
│   └── classify.py      # Main Flask application and classification endpoint
├── venv/                # Virtual environment (excluded from git)
├── requirements.txt     # Python dependencies
├── vercel.json         # Vercel deployment configuration
└── README.md           # This file
```

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | Your OpenAI API key for GPT-4o-mini | Yes |

## How It Works

1. The API receives a POST request with an item to classify
2. It constructs a prompt for the OpenAI GPT-4o-mini model
3. The model analyzes the item and determines whether it should be:
   - **Recycle**: Items that can be recycled
   - **Compost**: Organic materials suitable for composting
   - **Trash**: Items that should go to landfill
4. The classification result is returned to the client

## Notes

- The local server uses auto port selection to avoid conflicts on macOS
- Debug mode is enabled in local development
- Make sure to keep your OpenAI API key secure and never commit it to version control

## License

[Add your license here]

## Contributing

[Add contribution guidelines here]