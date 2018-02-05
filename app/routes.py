# -*- coding: utf-8 -*-

from app import app
from flask import render_template,redirect
from app.models import Product,Characteristic

@app.route('/products/<id_prod_url>')
def index(id_prod_url):
    product = Product.query.filter_by(id=id_prod_url).first()
    if product ==None:
        return redirect('/404.html', code=404)

    d = Characteristic.query.filter_by(product_id=id_prod_url).first()
    print('123')
    print(d.product_id)
    return render_template('product.html',title=product,prod=d,img_source_big ='/static/img/'+str(d.product_id)+'_800.jpg')

@app.route('/products/')
@app.route('/products')
@app.route('/')
def catalog():
    products = Product.query.all()
    u=Characteristic.query.all()
    print(type(products))
    print(type(products[1]))
    return render_template('catalog.html',data=products,prod=u)