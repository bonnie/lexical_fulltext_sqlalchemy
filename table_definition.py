"""Models and database functions for Poetry project"""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import TSVECTOR

db = SQLAlchemy()


############################################################################
# Model definitions

class Poem(db.Model):
    """class for poem objects"""

    __tablename__ = 'poems'

    __table_args__ = ( 
            db.Index( 
                    'tsv_full', 
                    'tsv', 
                    postgresql_using = 'gin', 
                    ),
            )


    poem_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    poem_url = db.Column(db.String(300), nullable=False)
    body = db.Column(db.Text, nullable=False)
    tsv = db.Column(TSVECTOR)


    author = db.relationship('Author', backref='poems')
    subjects = db.relationship('Subject', secondary='poems_subjects', backref='poems')

    def __repr__(self):
        """repr for a more readable poem object"""
        return "{}".format(self.title.encode('unicode-escape'))