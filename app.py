from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import fields


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://joseph:password@localhost/test'
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Created a model titled "Author" which has the fields
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

#This class helps return json from SQLAlchemy
class AuthorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Author
        sqla_session = db.session
    
    id = fields.Number(dump_only=True)
    name = fields.String(required=True)
    specialization = fields.String(required=True)

# author route
@app.route('/authors', methods=['GET'])
def index():
    get_authors = Author.query.all()
    author_schema = AuthorSchema(many=True)
    authors, error = author_schema.dump(get_authors)
    return make_response(jsonify({"authors": authors}))


if __name__ == '__main__':
    app.run(debug=True)
