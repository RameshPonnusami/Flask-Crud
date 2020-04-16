import  os
from app import app,db
from flask import request,render_template,redirect,flash,url_for
from models import Shop
from forms import ShopForm


@app.route('/', methods=["GET", "POST"])
def home():

    if request.form:
        try:
            shop = Shop(name=request.form.get("name"),shop_name=request.form.get("shop_name"),status=request.form.get("status"))
            db.session.add(shop)
            db.session.commit()
        except Exception as e:
            print("Failed to add Shop")
            print(e)
    try:
        shops = Shop.query.all()
    except Exception as e:
        print(e)
        shops=[]
    return render_template("home.html", shops=shops)



@app.route("/edit/<int:id>", methods=["GET","POST"])
def edit(id):
    try:
        shops = Shop.query.filter_by(id=id).first()
    except Exception as e:
        print(e)
        shops = []
    if shops:
        form = ShopForm(formdata=request.form, obj=shops)
        if request.method == 'POST':
            print("post")
            name = request.form.get("name")

            shop_name = request.form.get("shop_name")
            status = request.form.get("status")
            shop = Shop.query.filter_by(id=id).first()
            shop.name = name
            shop.shop_name = shop_name
            shop.status = status
            db.session.commit()
            flash('Shop updated successfully!')
            return redirect('/')
        return render_template('edit_shop.html', form=form)

    return render_template("home.html", shops=shops)



@app.route("/delete", methods=["POST"])
def delete():
    id = request.form.get("id")
    shop = Shop.query.filter_by(id=id).first()
    db.session.delete(shop)
    db.session.commit()
    return redirect("/")

db.create_all()

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 85))
    app.run(host='0.0.0.0', port=port, debug=True)
