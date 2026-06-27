from flask import Flask, send_from_directory, jsonify
import threading
import subprocess
import os
import time

app = Flask(__name__, static_folder='.')

# مسار الملفات الثابتة
@app.route('/')
@app.route('/<path:path>')
def serve_static(path='index.html'):
    # تأكد من أن الملف موجود
    if os.path.exists(path):
        return send_from_directory('.', path)
    else:
        return send_from_directory('.', 'index.html')

# صفحة صحية (health check) لـ Railway
@app.route('/health')
def health():
    return jsonify({"status": "healthy", "message": "PickIt Store is running!"})

# تشغيل البوت في خلفية منفصلة
def run_bot():
    # انتظر 5 ثوانٍ لتأكد من بدء التطبيق
    time.sleep(5)
    try:
        subprocess.run(["python", "bot.py"])
    except Exception as e:
        print(f"❌ خطأ في تشغيل البوت: {e}")

if __name__ == '__main__':
    # شغّل البوت في خيط منفصل
    bot_thread = threading.Thread(target=run_bot, daemon=True)
    bot_thread.start()
    print("✅ تم تشغيل البوت في الخلفية")
    
    # شغّل خادم Flask
    port = int(os.environ.get("PORT", 5000))
    print(f"🚀 الموقع يعمل على المنفذ: {port}")
    app.run(host='0.0.0.0', port=port)
