from sanic import Sanic
from sanic.response import json

app = Sanic()

@app.route("/")
async def test(request):
    
    return json({"hello": "안녕"}, ensure_ascii=False)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)