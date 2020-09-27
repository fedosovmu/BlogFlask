from datetime import datetime

class Post:
    def __init__(self, post_id, title, short_description, text, publication_date_iso_format, img_url):
        self.post_id = post_id
        self.title = title
        self.short_description = short_description
        self.text = text
        self.publication_date = datetime.fromisoformat(publication_date_iso_format)
        self.img_url = img_url

    def get_publication_date_str(self):
        return self.publication_date.strftime("%d %B %Y в %H:%M")

    @staticmethod
    def create_from_db_row(row):
        return Post(row['post_id'], row['title'], row['short_description'], row['text'], row['publication_date'], row['img_url'])