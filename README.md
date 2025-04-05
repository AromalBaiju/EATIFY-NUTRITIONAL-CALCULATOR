# 🍽️ Eatify – AI-Powered Food Nutrition Analyzer  

**Eatify** is a web application that helps users analyze the **nutritional value** of different foods. It provides insights into **calories, macronutrients (carbs, protein, fats), and health benefits** using AI-generated data.  

## 🚀 Features  
✅ **Food Search** – Get nutritional information for any dish.  
✅ **AI-Powered Nutrition Data** – Uses **Google Gemini API** to generate nutrition details.  
✅ **Food Image Fetching** – Retrieves relevant food images using **Pixabay API**.  
✅ **Meal Diary** – Users can **add food to their diary** and track their meals.  
✅ **Fast & Simple UI** – Built with **Flask** and a **React frontend** (served statically).  

## 🔧 Technologies Used  
- **Flask (Python)** – Backend for handling food searches and diary management.  
- **Google Gemini API** – AI-powered nutritional data retrieval.  
- **Pixabay API** – Fetches images of foods.  
- **React** – Frontend (served as static files from Flask).  
- **JavaScript, HTML, CSS** – For frontend development.  

## 📂 Project Structure  
Eatify/ │── static/ # Frontend files (HTML, CSS, JavaScript) │ ├── index.html # Main UI │ ├── style.css # Styling file │ ├── script.js # JavaScript for interactivity │── templates/ # Flask HTML templates (if used) │── app.py # Main Flask app │── requirements.txt # Python dependencies │── .env # API keys (not included in repo) │── README.md # Project documentation

## 🛠️ Installation & Setup  

Run the following commands in your terminal:  

sh
git clone https://github.com/Abramqureshi/Eatify.git && cd Eatify
pip install -r requirements.txt
echo -e "GEMINI_API_KEY=your_google_gemini_api_key\nPIXABAY_API_KEY=your_pixabay_api_key" > .env
python app.py

Now, open your browser and go to http://127.0.0.1:5000/ to use the app.

## 📜 License  
**Eatify** is an open-source project and is **free to use, modify, and distribute**.  
You are welcome to contribute and improve the project!  






