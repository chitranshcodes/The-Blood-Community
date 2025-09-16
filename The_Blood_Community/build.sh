set -o errexit
pip install -r requirements.txt
# Collect static files
python manage.py collectstatic --noinput

# Apply database migrations
python manage.py migrate