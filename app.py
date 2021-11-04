from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://joseph:password@localhost/test.db'
db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(debug=True)

# Created a model titled "Authors" which has the fields
#ID, name and specialization. ID is self generated
class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    specialization = db.Column(db.String(50))

    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization

    def __repr__(self):
        return '<Product %d>' % self.id
db.create_all()

# This class helps return json from SQLAlchemy
class AuthorSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Authors
        sqla_session = db.session
    
    id = fields.Number(dump_only=True)
    name = fields.String(required=True)
    specialization = fields.String(required=True)
