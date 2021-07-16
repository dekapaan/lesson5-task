from flask import *

app = Flask(__name__)


@app.route('/')
def entry_page():
    return render_template('shoppingList.html')
@app.route('/showitems', methods=['POST'])
def show():
    item_name = request.form['item_name']
    item_id = request.form['item_id']
    quantity = request.form['quantity']
    price = request.form['price']
    return render_template('showItems.html', item_name=item_name, item_id=item_id, quantity=quantity, price=price)
if __name__ == '__main__':
    app.run(debug=True)
