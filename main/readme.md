# AI Fighter Matchup

AI Fighter Matchup is a web application that analyzes and provides insights about fighting game matchups using Google's Gemini AI.

## Project Overview

The website consists of a FastAPI backend and a React frontend that work together to provide AI-powered analysis of fighting game character matchups. The system uses Google's Gemini AI to analyze and provide detailed insights about character matchups.

## Project Structure

```
ai_fighter_matchup/
├── backend/              # FastAPI server
│   ├── data/            # JSON data files
│   ├── services/        # Business logic and AI services
│   └── main.py         # Main FastAPI application
├── frontend/            # React application
│   ├── public/         # Static files
│   └── src/            # React source code
```

## Technologies Used

### Backend
- FastAPI
- Python 3.x
- Google Generative AI (Gemini)
- uvicorn
- python-dotenv

### Frontend
- React 19
- Axios for API requests
- React Testing Library
- Jest

## Getting Started

### Prerequisites
- Python 3.x
- Node.js and npm
- Google Cloud API key for Gemini AI

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file and add your Google Cloud API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

4. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install Node dependencies:
   ```bash
   npm install
   ```

3. Start the React development server:
   ```bash
   npm start
   ```

## Testing

### Backend Tests
Run the backend tests using:
```bash
cd backend
python run_tests.py
```

### Frontend Tests
Run the frontend tests using:
```bash
cd frontend
npm test
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

- Contributors:
    -[Cristoffer Bohorquez](https://github.com/Cristofferb7)
    -[Nathan Josue](https://github.com/PresJosue)
    -[Ethan Fu](https://github.com/yaboi332)
    -[Valduarri Reid](https://github.com/valdaurriR)
- Repository: https://github.com/Cristofferb7/ai_fighter_matchup