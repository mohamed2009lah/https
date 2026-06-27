# 🛍️ PickIt Store — دليل الإعداد الكامل

## 📂 الملفات

| الملف | الوظيفة |
|-------|---------|
| `index.html` | الموقع الرئيسي للمتجر |
| `dashboard.html` | لوحة تحكم المشرف |
| `bot.py` | بوت تيليغرام للإدارة |
| `requirements.txt` | مكتبات Python |

---

## 🔥 إعداد Firebase

### 1. قواعد Firestore (Security Rules)
افتح Firebase Console → Firestore → Rules، والصق:

```
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    // المنتجات: قراءة للجميع، كتابة للمسجلين فقط
    match /products/{id} {
      allow read: if true;
      allow write: if request.auth != null;
    }
    // المستخدمون: كل مستخدم يرى بياناته فقط
    match /users/{uid} {
      allow read, write: if request.auth != null && request.auth.uid == uid;
    }
    // المشرفون يرون كل شيء
    match /users/{uid} {
      allow read: if request.auth != null;
    }
  }
}
```

### 2. تفعيل Authentication
Firebase Console → Authentication → Sign-in method → فعّل "Email/Password"

---

## 🌐 رفع الموقع

### Netlify (مجاني وسريع)
1. اذهب إلى [netlify.com](https://netlify.com)
2. اسحب مجلد `pickit-store` وأفلته
3. الموقع سيكون جاهزاً في دقيقة!

### Vercel
```bash
npm i -g vercel
cd pickit-store
vercel
```

---

## 🤖 إعداد بوت تيليغرام

### الخطوات:

**1. أنشئ بوتاً جديداً:**
- افتح @BotFather في تيليغرام
- أرسل `/newbot`
- اتبع التعليمات واحصل على **TOKEN**

**2. احصل على Service Account من Firebase:**
- Firebase Console → Project Settings → Service accounts
- اضغط "Generate new private key"
- احفظ الملف باسم `serviceAccount.json` في نفس مجلد `bot.py`

**3. عدّل `bot.py`:**
```python
BOT_TOKEN = "1234567890:ABCdefGHIjklMNOpqrsTUVwxyz"  # توكنك
ADMIN_IDS = [123456789]  # معرّف حساب تيليغرام الخاص بك (اختياري)
```

**4. شغّل البوت:**
```bash
pip install -r requirements.txt
python bot.py
```

---

## 📱 أوامر البوت

| الأمر | الوظيفة |
|-------|---------|
| `/start` | بدء وعرض الأوامر |
| `/add` | إضافة منتج جديد خطوة بخطوة |
| `/list` | عرض آخر 20 منتج |
| `/search كلمة` | البحث في المنتجات |
| `/edit [id]` | تعديل حقل في منتج |
| `/delete [id]` | حذف منتج |
| `/stats` | إحصائيات المتجر |
| `/cancel` | إلغاء العملية الحالية |

---

## 🔄 سير العمل المقترح

```
إدارة المنتجات:
  بوت تيليغرام ──→ Firebase Firestore ←── لوحة التحكم (dashboard.html)
                                                ↓
                                        index.html (المتجر)
```

---

## 💡 نصائح

- استخدم **لوحة التحكم** لإضافة منتجات متعددة بسرعة
- استخدم **البوت** للإدارة من الهاتف في أي وقت
- المنتجات تظهر في المتجر **فوراً** بعد الإضافة
- إذا كانت Firebase فارغة، الموقع يعرض **منتجات تجريبية** تلقائياً
