class BlockTower:
    def __init__(self):
        self.stack = []
        self.removed_blocks = []

    def add_block(self, block):
        self.stack.append(block)
        print(f"Block {block} added to the tower.")

    def remove_block(self):
        if self.stack:
            block = self.stack.pop()
            self.removed_blocks.append(block)
            print(f"Block {block} removed.")
        else:
            print("The tower is empty.")

    def peek_top(self):
        if self.stack:
            print(f"Top block: {self.stack[-1]}")
        else:
            print("The tower is empty.")

    def tower_status(self):
        print("\nCurrent tower status:")
        if self.stack:
            for block in reversed(self.stack):
                print(block)
        else:
            print("Tower is empty.")

    def dismantle_tower(self):
        print("\n⚠ Instability detected. Dismantling tower...")
        while self.stack:
            self.remove_block()


tower = BlockTower()

tower.add_block("A")
tower.add_block("B")
tower.add_block("C")

tower.tower_status()
tower.peek_top()

tower.dismantle_tower()

print("\nRemoved blocks history:", tower.removed_blocks)
