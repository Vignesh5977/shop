from flask import Flask, request, render_template
from flask_mysqldb import MySQL
import MySQLdb

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '22@Pugazh'
app.config['MYSQL_DB'] = 'store'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)
@app.route('/Shop', methods=['GET','POST'])
def index():
    if request.method == "POST":
        selected_item = request.form.get("itemSelect")
        quantity = int(request.form.get("quantity"))
        if selected_item.__eq__("pen"):
            rate = 4
        elif selected_item.__eq__("pencil"):
            rate = 3
        elif selected_item.__eq__("sheet"):
            rate = 0.15
        elif selected_item.__eq__("eraser"):
            rate = 2
        elif selected_item.__eq__("sharpener"):
            rate = 2
        elif selected_item.__eq__("geometryBox"):
            rate = 175
        else:
            rate = 0  

        amount = rate * quantity
        print(selected_item)
        print(amount)
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO itemss (itemname, quantity,rate, amount) VALUES (%s, %s, %s ,%s)", (selected_item, quantity,rate, amount))
        mysql.connection.commit()
        cur.close()
        

        #return "Data received successfully"

    return render_template("shop.html")  

@app.route('/Sell',methods=['POST','GET'])
def sell_item():
    if request.method == "POST":
        selected_items = request.form.get("itemName")
        rates = request.form.get("itemPrice")
        quan = request.form.get("itemQuantity")
        
        rate=int(rates)
        quantity=int(quan)
        amounts=rate*quantity  
        print(selected_items)
        print(rates)
        print(amounts)
        print(amounts)
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO sellitemss (itemname, quantity,rate, amount) VALUES (%s, %s, %s ,%s)", (selected_items, quantity,rate, amounts))
        mysql.connection.commit()
        cur.close()
        
    cur = mysql.connection.cursor()
    cur.execute("SELECT itemname,quantity,rate,amount FROM sellitemss")
    fetchdata = cur.fetchall()
    cur.close()
    return render_template("sell.html", users=fetchdata)        
        #return "Data success"
        
        
    # return render_template("sell.html")    

if __name__ == "__main__":
    app.run(debug=True)
