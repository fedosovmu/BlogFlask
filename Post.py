from datetime import datetime

class Post:
    def __init__(self, post_id, title, short_description, publication_date_iso_format, img_url):
        self.post_id = post_id
        self.title = title
        self.short_description = short_description
        self.publication_date = datetime.fromisoformat(publication_date_iso_format)
        self.img_url = img_url

    def get_publication_date_str(self):
        return self.publication_date.strftime("%m/%d/%Y, %H:%M:%S")
