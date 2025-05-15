from typing import List, Dict, Optional

class TreeNode:
    """Represents a node in the pricing calculation tree"""
    def __init__(self, parent: Optional['TreeNode'], rule: Optional[str], items: List[str], rules: Dict[str, float]):
        self.parent = parent
        self.rule = rule
        self.items = items.copy()
        self.price = parent.price + rules[rule] if parent and rule else 0
        self.valid = self._apply_rule(rule)

    def _apply_rule(self, rule: str) -> bool:
        """Apply the rule to the items"""
        if not rule:
            return True
        for item in rule:
            if item not in self.items:
                return False
            self.items.remove(item)
        return True

class Checkout:
    def __init__(self, rules: Dict[str, float]):
        self.rules = rules
        self.best_node = None
        self.best_price = float('inf')

    def calculate_price(self, items: List[str]) -> TreeNode:
        """Calculates the best possible price for the given items"""
        self.best_node = None
        self.best_price = float('inf')
        root = TreeNode(None, None, items, self.rules)
        self._build_tree(root)
        return self.best_price
    
    def print_tree(self, node: TreeNode) -> None:
        """Prints the tree"""
        if not node:
            print()
            return
        if node.rule is not None:
            print(f"{node.rule}", end=" ")
        self.print_tree(node.parent)

    def _build_tree(self, node: TreeNode) -> None:
        """Recursively builds the pricing tree"""
        if not node.items:
            if node.price < self.best_price:
                self.best_price = node.price
                self.best_node = node
            return

        for rule in self.rules:
            child = TreeNode(node, rule, node.items.copy(), self.rules)
            if child.valid:
                self._build_tree(child)

def main():
    # Example usage
    rules = {
        "A": 1,
        "B": 2,
        "C": 3,
        "D": 4,
        "AAA": 2,
        "AAAAA": 3.4,
        "CC": 5,
        "CD": 5,
    }
    
    checkout = Checkout(rules)
    all_items = 'AAAAAAAAAA'
    items = []
    for item in all_items:
        items.append(item)
        result = checkout.calculate_price(items)
        print(f"Current items: {''.join(items)}, price: {result}")
        checkout.print_tree(checkout.best_node)


    checkout = Checkout(rules)
    all_items = 'CDCCDCD'
    items = []
    for item in all_items:
        items.append(item)
        result = checkout.calculate_price(items)
        print(f"Current items: {''.join(items)}, price: {result}")
        checkout.print_tree(checkout.best_node)

if __name__ == "__main__":
    main() 