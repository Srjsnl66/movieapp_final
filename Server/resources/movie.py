from importlib.resources import Resource
from flask import Response, request, jsonify
from flask_restful import Resource
from .db import mysql

class MoviesApi(Resource):
    def __init__(self) -> None:
        self.connection = mysql.connect()
        self.cursor = self.connection.cursor()
        
    def get(self):
        self.cursor.execute("SELECT * FROM movie")
        data = self.cursor.fetchall()

        movies = []
        for d in data: movies.append({ "id":d[0], "title": d[1], "category": d[2],  "description": d[3], "userid": d[4]})
        return movies, 200

    def post(self):
        body = request.get_json()
        print(body)
        self.cursor.execute('INSERT INTO movie (title, category, description, userid) VALUES (%s, %s, %s, %s)', (body['title'], body['category'], body['description'], body['userid']))
        self.connection.commit()
        return { "id": "" }, 200

    def put(self):
        body = request.get_json()
        print(body)
        self.cursor.execute("UPDATE movie SET title = %s, category = %s, description = %s WHERE id = %s", (body['title'], body['category'], body['description'], body['id']))
        self.connection.commit()
        return { "id": "" }, 200

class MovieApi(Resource):
    def __init__(self) -> None:
        self.connection = mysql.connect()
        self.cursor = self.connection.cursor()
    
    def get(self, id):
        print(id)
        self.cursor.execute("SELECT * FROM movie WHERE userid = %s", id)
        data = self.cursor.fetchall()

        movies = []
        for d in data: movies.append({ "id":d[0], "title": d[1], "category": d[2],  "description": d[3], "userid": d[4]})
        return movies, 200

    def delete(self, id):
        self.cursor.execute("DELETE FROM movie WHERE id = %s", id)
        self.connection.commit()
        return "", 200
    
