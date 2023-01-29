from blockchain import Blockchain

if __name__ == '__main__':
    blockchain = Blockchain()

    blockchain.add_new_block('Primeiro bloco')
    blockchain.add_new_block('Segundo bloco')
    blockchain.add_new_block('Terceiro bloco')

    print(blockchain.get_all_blocks())