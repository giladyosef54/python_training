import MongoBackedAVL
from flask import Flask, request
from json import dumps
import pymongo


app = Flask(__name__)

try:
    tree = MongoBackedAVL.MongoBackedAVL()
except Exception as e:
    print("There is some problem with connecting to the database server, "
          "please validate the connection string and the server connection.\n")
    print(e.args[0])
    raise SystemExit


@app.post('/insert_treasure')
def insert_treasure():
    treasure = request.get_json()
    try:
        tree.insert(treasure['value'])
        response = 'Successfully inserted', 200

    except ValueError as e:
        response = e.args[0], 400
    except Exception as e:
        print("There is some problem, probably with connecting to the database server, "
              "please validate the connection string and that the server is activate.\n")
        print(e.args[0])
        raise SystemExit

    return response


@app.delete('/delete_all_treasures')
def delete_all_treasures():
    try:
        tree.clear()
    except Exception as e:
        print("There is some problem, probably with connecting to the database server, "
              "please validate the connection string and that the server is activate.\n")
        print(e.args[0])
        raise SystemExit
    return 'Cleared', 200


@app.get('/get_treasures')
def get_treasures():
    treasures_list = []
    for val in tree:
        treasures_list.append(val)
    return {'treasures': treasures_list}


@app.delete('/delete_treasure')
def delete_treasure():
    treasure = request.get_json()
    try:
        tree.delete(treasure['value'])
        response = 'Successfully deleted', 200
    except ValueError as e:
        response = e.args[0], 400
    except Exception as e:
        print("There is some problem, probably with connecting to the database server, "
              "please validate the connection string and that the server is activate.\n")
        print(e.args[0])
        raise SystemExit

    return response


@app.get('/search_treasure')
def search_treasure():
    value = request.args.get('value')
    value = float(value)

    try:
        found = tree.search_treasure(value)
    except Exception as e:
        print("There is some problem, probably with connecting to the database server, "
              "please validate the connection string and that the server is activate.\n")
        print(e.args[0])
        raise SystemExit

    if found:
        response = {'message': 'Treasure found!'}, 200
    else:
        response = {'message': 'Treasure not found'}, 400
    return response


@app.get('/pre_order_traversal')
def pre_order_traversal():
    values = tree.pre_order_traversal()
    response = {'traversal_result': values}, 200
    return response


@app.get('/in_order_traversal')
def in_order_traversal():
    values = tree.in_order_traversal()
    response = {'traversal_result': values}, 200
    return response


@app.get('/post_order_traversal')
def post_order_traversal():
    values = tree.post_order_traversal()
    response = {'traversal_result': values}, 200
    return response


@app.get('/validate_bst')
def validate_bst():
    if tree.validate():
        print(tree.get_visualized_tree())
        status = 200
        data = dumps({'message': 'BST is valid'})
    else:
        status = 400
        data = dumps({'message': 'BST is not valid'})
    return data, status


def main():
    app.run()


if __name__ == '__main__':
    main()
