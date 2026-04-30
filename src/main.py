import uvicorn
from src.interface.api import app

if __name__ == "__main__":
    print("\n" + "="*50)
    print("3LandSpiel App wird gestartet!")
    print("Web-GUI: http://localhost:8000")
    print("API-Docs: http://localhost:8000/docs")
    print("="*50 + "\n")
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)
