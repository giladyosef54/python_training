import ds_to_db
from flask import Flask, request

app = Flask(__name__)

tree = ds_to_db.ds_to_db()


@app.post('/insert_treasure')
def insert_treasure():
    treasure = request.get_json()
    status = tree.insert(treasure['value'])
    if status == 200:
        response = 'Successfully inserted', status
    else:
        response = 'Something went wrong', status
    return response


@app.delete('/delete_all_treasures')
def delete_all_treasures():
    return 'Cleared', tree.clear()


@app.get('/get_treasures')
def get_treasures():
    response = {'treasures':[]}
    treasures_list = response['treasures']
    for val in tree:
        treasures_list.append(val)
    return response


@app.delete('/delete_treasure')
def delete_treasure():
    treasure = request.get_json()
    status = tree.delete(treasure['value'])
    if status == 200:
        response = 'Successfully deleted', status
    else:
        response = 'Something went wrong', status
    return response


@app.get('/search_treasure')
def search_treasure():
    value = request.args.get('value')
    value = float(value)
    status = tree.search_treasure(value)
    if status == 200:
        response = {'message': 'Treasure found!', 'status': status}
    else:
        response = {'message': 'Treasure not found'}, status
    return response


def main():
    app.run()


if __name__ == '__main__':
    main()
