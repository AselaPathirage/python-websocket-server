from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse

app = FastAPI()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>WebSocket Chat</title>
    </head>
    <body>
        <h1>WebSocket Test</h1>
        <textarea id="messages" rows="10" cols="30" readonly></textarea><br/>
        <input type="text" id="messageInput" autocomplete="off"/>
        <button onclick="sendMessage()">Send</button>

        <script>
            var ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages');
                messages.value += '\\n' + event.data;
            };
            function sendMessage() {
                var input = document.getElementById("messageInput");
                ws.send(input.value);
                input.value = '';
            }
        </script>
    </body>
</html>
"""

@app.get("/")
async def get():
    return HTMLResponse(html)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    headers = websocket.headers
    print("Headers received:", headers)
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Message text was: {data}")
    except WebSocketDisconnect:
        print("Client disconnected")
