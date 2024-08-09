blockchain = [[1]]

def add_value(trans_value):
    blockchain.append([blockchain[-1], trans_value])
    print(blockchain)
    
add_value(2)
add_value(0.9)
add_value(10.89)

# ? The program shows how one can make a simple block which stores the data and can remember last entered data. This project demonstrates working principle of a block chain.