class Comment:
    def __init__(self, comment_id, post_id, text):
        self.comment_id = comment_id
        self.post_id = post_id
        self.text = text

    @staticmethod
    def create_from_db_row(row):
        return Comment(row['comment_id'], row['post_id'], row['text'])