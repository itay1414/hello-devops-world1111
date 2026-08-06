
from flask import Flask   ## בניית שרת FLASK מתוך ספריית FLASK##
import redis   ##ייבוא ספריית RDIS לטובת התקקשרות עם השרת##

print("Hello, DevOps world V2")   ##הדפסה מהתרגיל הראשון##

app = Flask(__name__)   ##יצירת אובייקט וקישור לשרת##

r = redis.Redis(host='redis', port=6379, decode_responses=True)   ##יצירת חיבור ראשוני, הגדרת הפורט ושינוי הפלט לקטקט רגיל##
@app.route('/')   ##כהרצת הפונקציה בעת פנייה לשרת##
def home():
    counter = r.get('counter')   ##פנייה למאגר להבין מה הערך של קאונטר##
    if counter is None:   ##אם עדיין אין שום ערך שמור (פעם ראשונה, לפני שלחצו על משהו)##
        counter = 0   ##ברירת מחדל - מתחילים מ-0##
    return f"Num Counter: {counter} <br> <a href='/PLUS'><button>+</button></a> <a href='/MINUS'><button>-</button></a>"   
    ##מחזיר HTML: מציג את הערך הנוכחי, ירידת שורה, וכפתורי + ו- שכל אחד מפנה לכתובת אחרת##

@app.route('/PLUS')   ##decorator: כשמישהו פונה ל-'/PLUS' (לחיצה על כפתור +), תריץ את increment##
def increment():
    r.incr('counter')   ##פקודה אטומית ל-Redis: קרא את הערך, הוסף 1, שמור בחזרה - הכל בפעולה אחת##
    return home()   ##מציג בחזרה את הדף המעודכן, עם הערך החדש##

@app.route('/MINUS')   ##decorator: כשמישהו פונה ל-'/MINUS' (לחיצה על כפתור -), תריץ את decrement##
def decrement():
    counter = r.get('counter')   ##קודם קוראים את הערך הנוכחי, כי יש תנאי לבדוק לפני שמורידים##
    if counter is None:
        counter = 0
    if int(counter) > 0:   ##בודקים: מותר להוריד רק אם הערך גדול מ-0 (int כי Redis מחזיר טקסט, לא מספר)##
        r.decr('counter')   ##אם מותר - מורידים 1 מ-Redis##
    return home()   ##בכל מקרה (גם אם לא ירדנו), מציגים את הדף המעודכן##

if __name__ == '__main__':   ##בודק: האם הקובץ הזה רץ ישירות (לא מיובא מקובץ אחר)? אם כן -##
    app.run(host='0.0.0.0', port=5000, debug=True)   
    ##מפעיל בפועל את השרת: host='0.0.0.0' מקשיב מכל כתובת (חובה ב-Codespaces), port=5000 הפורט הפנימי, debug=True מצב פיתוח נוח##