import os
from flask import Flask, render_template, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import pymongo

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb+srv://admin:Madeforadmin1@myfirstcluster-bbdvy.mongodb.net/cookbook?retryWrites=true&w=majority'
app.config["MONGO_DBNAME"] = 'cookbook'
mongo=PyMongo(app)



@app.route('/')
def index():
    return render_template('index.html', recipes=mongo.db.recipes.find(), categories=mongo.db.categories.find())

@app.route('/search', methods=['POST'])
def search():
    
    ''' 
    The below line of code creates an index on each of the fields in the collection,
    allowing us to perform a text search on them
    '''
    # mongo.db.recipes.create_index([('description', 'text'), ('name','text'), ('ingredients', 'text')])
    
    
    ''' 
    The below line of code drops all indexes on a collection.
    '''
    # mongo.db.recipes.drop_indexes()
    
    query = request.form.get('query')
    recipes = mongo.db.recipes.find({'$text': {'$search': query}})
    return render_template('recipes.html', recipes=recipes, type='searched', query=query)

@app.route('/category/<type>')
def recipe_type(type):
    recipes=mongo.db.recipes.find({'category': type})
    return render_template('recipes.html', recipes=recipes, type=type)

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)