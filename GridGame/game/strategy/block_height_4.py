from game.strategy.Block4 import Block

class BlockHeight4(Block) :
    def __init__(self,grid):
        self.blocks = []
        self.grid = grid
        self.height = grid.height
        self.width = grid.width


    def move_played(self,x,y,color,player_name):
        print("Move played in BlockHeight4")
        self.update_blocks(x)

        return

    def next_Bob_move(self):

        return
    
    def next_Alice_move(self):
        return
    
    def evaluate_block(self):

        return
    
    def update_blocks(self,x):
        block = self.block_at(x)
        if block == None:
            block_left = self.block_at(x-1)
            block_right = self.block_at(x+1)

            if(block_left):
                block_left.end_col = x
                block_left.size += 1
                block_left.columns.append([self.get_cell(x, row) for row in range(self.height)])
                #merge 2 blocks
                if(block_right):
                    block_left.end_col = block_right.end_col
                    block_left.size += block_right.size
                    block_left.columns.extend(block_right.columns)
                    self.blocks.remove(block_right)
                    
                block_left.check_configurations()
                #block_left.print_block()
                return
                      
            if(block_right):
                block_right.start_col = x
                block_right.size += 1
                block_right.columns.insert(0,[self.get_cell(x, row) for row in range(self.height)])
                block_right.check_configurations()
                #block_right.print_block()
                
                return
            
            #create new block
            block = Block(self)
            block.start_col = x
            block.end_col = x
            block.size = 1
            block.columns.append([self.get_cell(x, row) for row in range(self.height)])
            self.blocks.append(block)

        block.check_configurations()
        #block.print_block()
        return


    def block_at(self, x):
        for block in self.blocks:
            if block.start_col <= x <= block.end_col:
                return block
        return None
    
    def get_cell(self, x, y):
        return self.grid.get_cell(x, y)
    