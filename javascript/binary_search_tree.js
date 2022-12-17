class BinarySearchTree {

  constructor(value, depth = 1) {
    // Default depth of 1 indicates inital node added to tree is the root
    this.value = value;
    this.depth = depth;
    this.left = null;
    this.right = null;
  }

  insert(value) {
    // "this" refers to the node that called insert().
    // Typically the root node on initial call

    if (value < this.value) {
      // The new node goes to the left of the current node
      if (this.left === null) {
        // Create new node and add as left child of current node
        this.left = new BinarySearchTree(value, this.depth + 1);
        console.log(`Tree node ${value} added to the left of ${this.value} at depth ${this.depth + 1}`);
        return;
      }
      // Call insert() with current node's left child as "this"
      this.left.insert(value);
      return;

    }
    
    // The new node goes to the right of the current node
    if (value > this.value) {

      if (this.right === null) {
        // Create new node and add as right child of current node
        this.right = new BinarySearchTree(value, this.depth + 1);
        console.log(`Tree node ${value} added to the right of ${this.value} at depth ${this.depth + 1}`);
        return;
      }
      
      // Call insert() with current node's right child as "this"
      this.right.insert(value);
      return;
      
    }

    // Values that are already in the tree are ignored

  }

  getNodeByValue(value) {
    // "this" refers to the node that called getNodeByValue().
    // Typically the root node on initial call
    if (this.value === value) {
      return this;
    }
    
    if (this.left !== null && value < this.value) {
      return this.left.getNodeByValue(value);
    }
    
    if (this.right !== null && value > this.value) {
      return this.right.getNodeByValue(value);
    }

    return null;
  }

  findMinValue() {
    // "this" refers to the node that called findMinValue().
    // Typically the root node on initial call
    if (this.left === null) {
      // If there is no left child, this is the minimum node
      return this;
    }
    return this.left.findMinValue();
  }

  findMaxValue() {
    // "this" refers to the node that called findMaxValue().
    // Typically the root node on initial call
    if (this.right === null) {
      // If there is no right child, this is the maximum node
      return this;
    }
    return this.right.findMaxValue();
  }

  delete(value) {
    // "this" refers to the node that called delete().
    // Typically the root node on initial call
    if (this.value === null) {
      return this;
    }

    if (value < this.value) {
      this.left = this.left.delete(value);
    }

    if (value > this.value) {
      this.right = this.right.delete(value);
    }

    if (value === this.value) {

      if (this.left === null) {
        let temp = this.right;
        this.value = null;
        return temp;
      }
      
      if (this.right === null) {
        let temp = this.left;
        this.value = null;
        return temp;
      }
      
      let temp = this.right.findMaxValue();
      this.value = temp.value;
      this.right.delete(temp);

    }
    return this;
  }
  

  depthFirstTraversal() {
    if (this.left !== null) {
      this.left.depthFirstTraversal();
    }
    console.log(`Depth: ${this.depth}, Value: ${this.value}`);
    if (this.right !== null) {
      this.right.depthFirstTraversal();
    }
  }


  printNode() {
    return (`
      Value:       ${this.value}
      Depth:       ${this.depth}
      Left Child:  ${this.left ? this.left.value : null}
      Right Child: ${this.right ? this.right.value : null}
      `);
  }

}

const arr = [8, 4, 10, 7, 1, 30, 20, 50, 43, 26];

const tree = new BinarySearchTree(12);
tree.depthFirstTraversal();

arr.forEach(el => tree.insert(el));
tree.depthFirstTraversal();
console.log(tree.getNodeByValue(20).printNode());
tree.delete(20);
tree.depthFirstTraversal();
console.log('Minimum value: ', tree.findMinValue().printNode());
console.log('Maximum value: ', tree.findMaxValue().printNode());