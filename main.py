from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def sample():
    print("function came in")
    return {
        "status": "Ran Successfully"
    }


if __name__ == "__main__":
    uvicorn.run(app, host = "0.0.0.0", port = 9876)