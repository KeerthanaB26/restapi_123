from flask import Flask, jsonify, render_template


todo = Flask(__name__)

students = [
    {
        'id':1,
        'name':'keerthana',
        'age':20
    },
    {
        'id':2,
        'name':'yashaswini',
        'age':20

    }
]
@todo.route('/students-list')
def get_students_list():
    return jsonify(students)

@todo.route('/students/get/<int:id>')
def get_student_by_id(id):
    print(id)
    for std in students:
        if std['id'] == id:
            return jsonify(std)
    print(std)
    return jsonify('not found')


if __name__ == '__main__':
    todo.run(
        host='127.0.0.1',
        port=5010,
        debug=True
    )