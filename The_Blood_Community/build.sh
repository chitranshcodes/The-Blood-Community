set -o errexit
pip install -r requirements.txt
python community/webscrape.py
# Collect static files
python manage.py collectstatic --noinput

# Apply database migrations
python manage.py migrate