from flask import Flask, request, jsonify, send_from_directory
import requests
from datetime import datetime
import os
import json
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, static_folder='static')

# Serve React App
@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

# API Routes
@app.route('/api/search-food', methods=['POST'])
def search_food():
    data = request.json
    food = data.get('food', '').strip().lower()
    meal_time = data.get('mealTime', 'breakfast')
    
    if not food:
        return jsonify({'error': 'Food name is required'}), 400
    
    if food == 'kerala sadhya':
        return jsonify({
            'name': 'Kerala Sadhya',
            'calories': 1200,
            'carbs': '200 g',
            'protein': '30 g',
            'fats': '40 g',
            'benefits': [
                'Rich in fiber from vegetables and rice',
                'Balanced mix of proteins from lentils and dairy',
                'High in antioxidants from spices like turmeric and curry leaves'
            ],
            'image_url': get_food_image('Kerala Sadhya')
        })
    
    try:
        prompt = f"""Provide nutritional information for the Kerala food "{food}" in JSON format with:
        {{
          "name": "string",
          "calories": number,
          "carbs": "string g",
          "protein": "string g",
          "fats": "string g",
          "benefits": ["string1", "string2", "string3"],
          "imageQuery": "string"
        }}"""
        
        gemini_response = requests.post(
            f'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={os.getenv("GEMINI_API_KEY")}',
            json={
                "contents": [{
                    "parts": [{
                        "text": prompt
                    }]
                }]
            }
        )
        
        gemini_response.raise_for_status()
        gemini_data = gemini_response.json()
        response_text = gemini_data['candidates'][0]['content']['parts'][0]['text']
        json_start = response_text.find('{')
        json_end = response_text.rfind('}') + 1
        food_data = json.loads(response_text[json_start:json_end])
        
        food_data['image_url'] = get_food_image(food_data.get('imageQuery', food))
        
        return jsonify(food_data)
    
    except Exception as e:
        print(f"Error processing food search: {str(e)}")
        return jsonify({'error': 'Failed to get food information'}), 500

def get_food_image(query):
    try:
        pixabay_response = requests.get(
            'https://pixabay.com/api/',
            params={
                'key': os.getenv("PIXABAY_API_KEY"),
                'q': query,
                'image_type': 'photo',
                'category': 'food',
                'per_page': 3
            }
        )
        
        pixabay_response.raise_for_status()
        pixabay_data = pixabay_response.json()
        
        if pixabay_data.get('hits') and len(pixabay_data['hits']) > 0:
            return pixabay_data['hits'][0]['webformatURL']
        
        return 'https://cdn.pixabay.com/photo/2016/03/05/19/02/empty-plate-1238248_640.jpg'
    
    except Exception as e:
        print(f"Error getting food image: {str(e)}")
        return 'https://cdn.pixabay.com/photo/2016/03/05/19/02/empty-plate-1238248_640.jpg'

@app.route('/api/add-to-diary', methods=['POST'])
def add_to_diary():
    try:
        food_data = request.json
        food_data['timestamp'] = datetime.now().isoformat()
        food_data['date'] = datetime.now().strftime('%Y-%m-%d')
        # In a real app, you'd save to a database
        return jsonify({'success': True, 'message': 'Food added to diary'})
    except Exception as e:
        print(f"Error adding to diary: {str(e)}")
        return jsonify({'error': 'Failed to add to diary'}), 500

@app.route('/api/get-diary', methods=['GET'])
def get_diary():
    # In a real app, you'd fetch from a database
    return jsonify([])

if __name__ == '__main__':
    app.run(debug=True)