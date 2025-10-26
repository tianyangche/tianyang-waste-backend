import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
import openai
import socket

# -----------------------------------------------------
# 1. 自动加载 .env 文件（用于本地开发）
# -----------------------------------------------------
load_dotenv()

# 2. 从环境变量读取 OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

# -----------------------------------------------------
# 3. 主分类接口
# -----------------------------------------------------
@app.route("/classify", methods=["POST"])
def classify():
    data = request.get_json()
    item = (data.get("item") or "").strip()

    if not item:
        return jsonify({"error": "missing 'item'"}), 400

    prompt = f"Classify the following item as Recycle, Compost, or Trash. Item: {item}"

    try:
        # 调用 OpenAI
        completion = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a waste classification assistant."},
                {"role": "user", "content": prompt},
            ],
        )
        reply = completion.choices[0].message.content.strip()
        return jsonify({"item": item, "result": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# -----------------------------------------------------
# 4. 自动选择可用端口（避免 macOS 端口占用）
# -----------------------------------------------------
def find_free_port(default_port=5000):
    port = default_port
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(("127.0.0.1", port)) != 0:
                return port
            port += 1


# -----------------------------------------------------
# 5. 启动 Flask 本地服务（Vercel 部署时不会触发这段）
# -----------------------------------------------------
if __name__ == "__main__":
    port = find_free_port(5000)

    if not openai.api_key:
        print("❌ ERROR: OPENAI_API_KEY not found.")
        print("   Please create a .env file or export the environment variable.")
        exit(1)

    print(f"🚀 Flask server running on http://127.0.0.1:{port}")
    app.run(host="0.0.0.0", port=port, debug=True)