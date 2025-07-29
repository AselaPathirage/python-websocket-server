## Sample Python Websocket Server

## Setup

1. Install dependencies:
   ```bash
   pip3 install -r requirements.txt
   ```

2. Run the server:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
    or
   python3 -m uvicorn main:app --host 0.0.0.0 --port 8000
   ```

## WebSocket Endpoint

- URL: `ws://localhost:8000/ws`
