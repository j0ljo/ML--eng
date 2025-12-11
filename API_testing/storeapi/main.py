from fastapi import FastAPI

app = FastAPI()

@app.get("/")           # Decorator to define a GET endpoint at the root URL

async def root():       # Asynchronous function to handle requests to the root URL
    return {"message": "Hello, world!"} # Return a JSON response with a greeting message



