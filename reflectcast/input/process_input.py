import os
from datetime import datetime

def save_reflection(text, uploads_dir="uploads"):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"reflection_{timestamp}.txt"
    filepath = os.path.join(uploads_dir, filename)

    with open(filepath, 'w') as file:
        file.write(text.strip())

    return filepath
