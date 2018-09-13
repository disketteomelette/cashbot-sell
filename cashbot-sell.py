#!/usr/local/bin/python
import os, sys, subprocess, time
secret1='xxxxxxxxxxxxxxxx'
secret2='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
vendercuando='165'
cantidad='0.20'
print "Cashbot - Implementacion de Coinbase API autoventa ETH"
print "JCRueda - www.jcrueda.com"
while 1:
	from coinbase.wallet.client import Client
	client = Client(secret1, secret2)
	accounts = client.get_accounts()
	assert isinstance(accounts.data, list)
	assert accounts[0] is accounts.data[0]
	assert len(accounts[::]) == len(accounts.data)
	user = client.get_current_user()
	cuentas = client.get_accounts()
	idcuenta = cuentas["data"][0]["id"]
	acid = user['id']
	tiemp = client.get_time()
	tiempo = tiemp['iso']
	tiempo = tiempo.replace("T", " ")
	tiempo = tiempo.replace("Z", "")
	price = client.get_buy_price(currency_pair = 'ETH-EUR')
	c = client.get_buy_price(currency_pair = 'ETH-EUR')
	d = client.get_sell_price(currency_pair = 'ETH-EUR')
	e = client.get_spot_price(currency_pair = 'ETH-EUR')
	accounts = client.get_accounts() 
	cryptobalance = accounts["data"][0]["balance"]["amount"]
	cryptocurrency = accounts["data"][0]["balance"]["currency"]
	eurobalance = accounts["data"][0]["native_balance"]["amount"]
	currency = accounts["data"][0]["native_balance"]["currency"]
	pcompra=float(c['amount'])
	pventa=float(d['amount'])
	print "[",tiempo,"]     Cuenta:",user['name'],"!"
	print "[",tiempo,"] ID usuario:",acid
	print "[",tiempo,"]  ID cuenta:",idcuenta
	print "[",tiempo,"]     1 ETH =",price['amount'],"EUR"
	print "[",tiempo,"] P. Compra =",c['amount']
	print "[",tiempo,"]  P. Venta =",d['amount']
	print "[",tiempo,"]   P. Spot =",e['amount']
	print "[",tiempo,"]    Balance:",cryptobalance,cryptocurrency,"-",eurobalance,currency
	txs = client.get_transactions(idcuenta)
	ultimatx = txs["data"][0]["amount"]["amount"]
	ultimatxeur = txs["data"][0]["native_amount"]["amount"]
	ultimafecha = txs["data"][0]["created_at"]
	if '-' in ultimatx:
	    fue = "VENTA"
	else:
	    fue = "COMPRA"
	ultimafecha = ultimafecha.replace("T", " ")
	ultimafecha = ultimafecha.replace("Z", "")
	print "[",tiempo,"] Ultima transaccion:",fue,ultimatx, "ETH -",ultimafecha
	print "[",tiempo,"] Programaste VENDER cuando el ETH llegara a",vendercuando,"EUR!"
	if price['amount'] > vendercuando:
		print "[",tiempo,"] El precio ahora es de",price['amount'],"EUR, superior a los",vendercuando,"EUR que estableciste, por lo que vamos a vender",cantidad,"ETH!"
		payment_methods = client.get_payment_methods()
		sell = account.sell(amount=cantidad,
                      currency="ETH",
                      payment_method=payment_method.id)
		sys.exit()
	else:
		print "[",tiempo,"] El precio ahora es de",price['amount'],"EUR, no vendemos!"
		print "[",tiempo,"] Esperamos un minuto y volvemos a empezar..."
		time.sleep(60)
