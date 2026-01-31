"""
List available Gemini models
"""
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

print("=" * 60)
print("📋 AVAILABLE GEMINI MODELS")
print("=" * 60)

try:
    models = genai.list_models()
    
    print("\n✅ Models that support 'generateContent':\n")
    
    for model in models:
        if 'generateContent' in model.supported_generation_methods:
            print(f"   • {model.name}")
            print(f"     Display: {model.display_name}")
            print(f"     Description: {model.description[:80]}...")
            print()
    
    print("=" * 60)
    print("💡 Use these model names in your code")
    print("=" * 60)
    
except Exception as e:
    print(f"\n❌ Error: {e}")
