## - הגדרת שפת הקוד שעליה האפליקציה רצה ##
FROM python:3.12

## יצירת תקייה יעודית שתכיל את הקונטיינר ##
WORKDIR /app

## העתקת קובץ הדרישות והתקנת הספריות ##
COPY requirements.txt .
RUN pip install -r requirements.txt

## העתקת תוכן האפליקציה ##
COPY app.py .

## הגדרת הפקודה שתריץ את הקונטיינר שהאפליקציה תעלה בשפת פייתון ##
CMD ["python", "app.py"]