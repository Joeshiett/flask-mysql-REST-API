from flask import Flask, request, json, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields, Schema

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://joseph:password@localhost/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Created a model titled "Author" which has the fields
#ID, name and specialization. ID is self generated
class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    specialization = db.Column(db.String(50))

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization

    def __repr__(self):
        return '<Author %d>' % self.id


#This class helps return json from SQLAlchemy
class AuthorSchema(Schema):
    class Meta:
        model = Author
        sqla_session = db.session
    
    id = fields.Integer()
    name = fields.String()
    specialization = fields.String()

# author route
@app.route('/authors', methods=['GET'])
def index():
    get_authors = Author.query.all()
    author_schema = AuthorSchema(many=True)
    authors = author_schema.dump(get_authors)
    return make_response(jsonify({"authors": authors}))

@app.route('/authors', methods=['POST'])
def create_author():
    data = request.get_json()
    new_author=Author(
        name=data.get('name'),
        specialization=data.get('specialization')
    )
    author_schema = AuthorSchema()
    data = author_schema.dump(new_author)
    return make_response(jsonify({'authors': data}),201)


if __name__ == '__main__':
    app.run(debug=True)
