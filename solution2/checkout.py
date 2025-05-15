from typing import List, Dict, Optional

class TreeNode:
    """Represents a node in the pricing calculation tree.

    Attributes:
        parent (Optional[TreeNode]): The parent node in the tree structure
        rule (Optional[str]): The pricing rule applied at this node
        items (List[str]): List of remaining items to be processed
        price (float): The accumulated price up to this node
        valid (bool): Whether the rule application was successful
    """
    def __init__(self, parent: Optional['TreeNode'], rule: Optional[str], items: List[str], rules: Dict[str, float]):
        """Initialize a new TreeNode.

        Args:
            parent (Optional[TreeNode]): The parent node in the tree
            rule (Optional[str]): The pricing rule to apply
            items (List[str]): List of items to process
            rules (Dict[str, float]): Dictionary mapping rules to their prices
        """
        self.parent = parent
        self.rule = rule
        self.items = items.copy()
        self.price = parent.price + rules[rule] if parent and rule else 0
        self.valid = self._apply_rule(rule)

    def _apply_rule(self, rule: str) -> bool:
        """Apply the pricing rule to the items.

        Args:
            rule (str): The rule to apply (e.g., "AAA" for three A's)

        Returns:
            bool: True if the rule was successfully applied, False otherwise
        """
        if not rule:
            return True
        for item in rule:
            if item not in self.items:
                return False
            self.items.remove(item)
        return True

class Checkout:
    """A checkout system that calculates the best possible price for items based on rules.

    Attributes:
        rules (Dict[str, float]): Dictionary mapping rules to their prices
        best_node (Optional[TreeNode]): The node with the best price found
        best_price (float): The best price found so far
    """
    def __init__(self, rules: Dict[str, float]):
        """Initialize the checkout system.

        Args:
            rules (Dict[str, float]): Dictionary mapping rules to their prices
        """
        self.rules = rules
        self.best_node = None
        self.best_price = float('inf')

    def calculate_price(self, items: List[str]) -> TreeNode:
        """Calculate the best possible price for the given items.

        Args:
            items (List[str]): List of items to calculate price for

        Returns:
            TreeNode: The node containing the best price found
        """
        self.best_node = None
        self.best_price = float('inf')
        root = TreeNode(None, None, items, self.rules)
        self._build_tree(root)
        return self.best_price
    
    def print_tree(self, node: TreeNode) -> None:
        """Print the tree structure showing the sequence of rules applied.

        Args:
            node (TreeNode): The node to start printing from
        """
        if not node:
            print()
            return
        if node.rule is not None:
            print(f"{node.rule}", end=" ")
        self.print_tree(node.parent)

    def _build_tree(self, node: TreeNode) -> None:
        """Recursively build the pricing tree by trying all possible rule combinations.

        Args:
            node (TreeNode): The current node to build from
        """
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
    """Main function demonstrating the usage of the Checkout system.
    """
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