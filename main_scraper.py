import requests
from bs4 import BeautifulSoup
import json
import time

# Vibe Coding: AI-Assisted Data Extraction Workflow
def vibe_scrape_engine(target_url):
    print(f"--- Initializing Vibe Check on {target_url} ---")
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(target_url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Example: Extracting headlines and metadata for AI training
        extracted_data = []
        for article in soup.find_all(['h1', 'h2', 'h3'], limit=10):
            text = article.get_text().strip()
            if len(text) > 10:  # Filter noise
                extracted_data.append({
                    "content_type": "headline",
                    "raw_text": text,
                    "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
                    "source_url": target_url
                })
        
        # Save as Structured JSON (The gold standard for AI Trainers)
        with open('training_data.json', 'w') as f:
            json.dump(extracted_data, f, indent=4)
            
        print(f"Successfully normalized {len(extracted_data)} data points.")
        
    except Exception as e:
        print(f"Vibe check failed: {e}")

if __name__ == "__main__":
    vibe_scrape_engine("https://news.ycombinator.com") # Sample tech site
