# GameSensei 🧠🎮

GameSensei turns Reddit, YouTube, and app store noise into real-time insights for players and developers.

## 🔍 What It Does

- Summarizes Reddit threads for game advice
- Detects pain points from app reviews
- Gives instant, AI-powered tips for player decks
- Shows devs which features are breaking after updates

## 🧰 Tech Stack

- Python + FastAPI backend
- OpenAI GPT-4o for summaries
- Reddit/YouTube scraping
- Streamlit dashboard
- TF-IDF / embedding-based semantic search

## 🚀 How to Run

1. Clone this repo
2. Install dependencies  
   `pip install -r requirements.txt`
3. Add `.env` with your OpenAI key
4. Run the backend  
   `uvicorn app.main:app --reload`
5. Open dashboard  
   `streamlit run ui/dashboard.py`

## 📁 Folder Structure

- `app/`: Core AI and API logic
- `ui/`: Streamlit demo frontend
- `data/`: Sample Reddit threads
- `prompts/`: LLM prompt templates

## 🤖 Example Query

Input:
```
P.E.K.K.A, Wizard, Giant, Archer Queen, Zap, Cannon
```

Output:
```
- Struggles vs splash/air units  
- Use Valk instead of Wizard for better elixir cycle  
- Based on 2.3k Reddit comments across last 30 days
```

## 📈 Future Plans

- In-game advisor mode (real-time)
- Multilingual feedback summarizer
- Dev dashboard with sentiment timelines
- Creator tagging for verified insights

## License

MIT
