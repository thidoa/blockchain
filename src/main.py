from blockchain import Blockchain

if __name__ == '__main__':
    blockchain = Blockchain()

    blockchain.add_new_block('Block First!')
    blockchain.add_new_block('Blockchain is very nice!')
    blockchain.add_new_block('Speak some languages ?')

    print(blockchain.get_all_blocks())