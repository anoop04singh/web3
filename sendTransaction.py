from tkinter import *
from web3 import Web3
        
        
def checkConnection():
    infuraURL = enterUrl.get()
    web3 = Web3((Web3.HTTPProvider(infuraURL)))
    if(web3.is_connected()):
        label1.config(text="Connection Successful!",font=("Poppins",10))
        #canvas.create_text(10,100,anchor='nw',text="Connection Successful!",font=("Poppins",10))
        checkCon.config(bg='#daffb3')
        canvas.create_text(10,140,anchor='nw',text="Enter Your Wallet Address / Public Key:",font=("Poppins",10))
        canvas.create_text(10,190,anchor='nw',text="Enter Receiver's Address / Public Key:",font=("Poppins",10))
        canvas.create_text(10,240,anchor='nw',text="Enter Amount:",font=("Poppins",10))
        canvas.create_text(10,290,anchor='nw',text="Enter PRIVATE KEY:",font=("Poppins",10))
        enterFrom = Entry()
        enterFrom.place(x=270,y=138,height=25,width=280)

        enterTo = Entry()
        enterTo.place(x=270,y=188,height=25,width=280)

        enterValue = Entry()
        enterValue.place(x=270,y=236,height=25,width=280)

        enterPkey = Entry(bg='#ffb3b3')
        enterPkey.place(x=270,y=286,height=25,width=280)
        
        def performTransaction():
            amountWei= int(float(enterValue.get())*pow(10,18))
            #amountWei = web3.to_wei(float(enterValue.get()) ,'ether')
            gasPrice = web3.eth.gas_price
            transaction = {'to': enterTo.get(),'value':amountWei,'gas':21000,'gasPrice':gasPrice,'nonce':web3.eth.get_transaction_count(enterFrom.get()),'chainId':11155111}
            signtxn = web3.eth.account.sign_transaction(transaction,enterPkey.get())
            txn_hash = web3.eth.send_raw_transaction(signtxn.raw_transaction)
            #canvas.create_text(10,370,anchor='nw',text=web3.to_hex(txn_hash),font=("Poppins",10))
            confirm_txn = web3.eth.wait_for_transaction_receipt(txn_hash)
            #canvas.create_text(10,400,anchor='nw',text=str(confirm_txn['blockNumber']),font=("Poppins",10))
            output = Entry()
            output.place(x=10,y=360,height=20,width=200)
            output2 = Entry()
            output2.place(x=10,y=390,height=20,width=500)
            output.insert(0,str(confirm_txn['blockNumber']))
            output2.insert(0,"https://sepolia.etherscan.io/tx/"+str(web3.to_hex(txn_hash)))
                
        transButton = Button(text='Send Transaction',command = performTransaction)
        transButton.place(x=10,y=320,width=200,height=30)
        
        
        
        
        
    else:
        label1.config(text="Connection Not Successful!",font=("Poppins",10))
        #canvas.create_text(10,100,anchor='nw',text="Connection Not Successful!",font=("Poppins",10))
        checkCon.config(bg='#ff3333')
        output.delete(0,END)
        output2.delete(0,END)
        

        
window = Tk()

window.title("Send Transaction on Sepholia Network")
window.geometry("720x480")

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 480,
    width = 720,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

label1 = Label(bg='white')
label1.place(x=0, y=80, width=200, height=20)

enterUrl = Entry()
enterUrl.place(x=10,y=10,height=20,width=250)

checkCon = Button(text='Check Connection',command = checkConnection)
checkCon.place(x=10,y=45,width=200,height=30)


canvas.place(x = 0,y=0)
window.mainloop()
