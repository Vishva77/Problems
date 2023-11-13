function TreeNode(val) {
    this.val = val;
    this.left = this.right = null;
  }
  
  function isBalanced(root) {
    // Helper function to calculate the height of a subtree
    function getHeight(node) {
      if (!node) return 0;
      
      const leftHeight = getHeight(node.left);
      const rightHeight = getHeight(node.right);
  
      // If the subtree is unbalanced (-1 is used as a flag), propagate it upwards
      if (leftHeight === -1 || rightHeight === -1 || Math.abs(leftHeight - rightHeight) > 1) {
        return -1;
      }
      
      // Otherwise, return the height of the subtree
      return Math.max(leftHeight, rightHeight) + 1;
    }
  
    // Start the recursion from the root
    return getHeight(root) !== -1;
  }
  
  // Example usage:
  const root1 = new TreeNode(3);
  root1.left = new TreeNode(9);
  root1.right = new TreeNode(20);
  root1.right.left = new TreeNode(15);
  root1.right.right = new TreeNode(7);
  
  console.log(isBalanced(root1)); // Output: true
  
  const root2 = new TreeNode(1);
  root2.left = new TreeNode(2);
  root2.right = new TreeNode(2);
  root2.left.left = new TreeNode(3);
  root2.left.right = new TreeNode(3);
  root2.left.left.left = new TreeNode(4);
  root2.left.left.right = new TreeNode(4);
  
  console.log(isBalanced(root2)); // Output: false
  