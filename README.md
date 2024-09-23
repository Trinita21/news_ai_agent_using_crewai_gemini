# AI News Blogger with CrewAI and Google Gemini

Leverage the power of AI to search, collect, and generate blog posts from news articles on any topic!

This project uses **CrewAI** and the **Google Gemini model** to automatically search for news articles via the **Serper API** (a Google Search API), gather relevant information, and write insightful blog content based on the provided topic.

## Key Features
- **AI-Powered News Search:** Automatically fetch and collect news articles on any given topic using the Serper API.
- **Blog Post Generation:** AI processes the news and generates well-structured blog posts.
- **Simple Setup:** Easy to configure and run.

## Setup Instructions

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/news_ai_agent_using_crewai_gemini
    cd news_ai_agent_using_crewai_gemini
    ```

2. **Create and Activate Your Python Environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up API Keys:**
   - Create a `.env` file in the root directory.
   - Add your **Google API** and **Serper API** keys to the `.env` file in the following format:
     ```
     GOOGLE_API_KEY=your_crewAI_key
     SERPER_API_KEY=your_serperAPI_key
     ```

5. **Run the Script:**
    ```bash
    python crew.py
    ```

## How It Works
1. The user specifies a topic.
2. The AI searches for relevant news articles using Serper API.
3. Information is collected and processed using Google Gemini model.
4. The system generates a blog post based on the retrieved content.

---

Feel free to contribute, report issues, or suggest improvements!

