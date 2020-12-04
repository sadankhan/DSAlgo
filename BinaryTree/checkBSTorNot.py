'''
This is algorithm.
A binary tree is BST if it satisfies any one of the following condition:
	1. It is empty
	2. It has no subtrees
	3. For every node x in the tree all the keys (if any) in the left sub tree must be less than key(x) and all the keys (if
	any) in the right sub tree must be greater than key(x)

'''

is_BST(root):
	if root == NULL:
		return true
# Check values in left subtree
	if root->left != NULL:
		max_key_in_left = find_max_key(root->left)
	if max_key_in_left > root->key:
		return false
# Check values in right subtree
	if root->right != NULL:
		min_key_in_right = find_min_key(root->right)
	if min_key_in_right < root->key:
		return false
return is_BST(root->left) && is_BST(root->right)


#Better Idea
is_BST(root, min, max):
	if root == NULL:
		return true
# is the current node key out of range?
	if root->key < min || root->key > max:
		return false
# check if left and right subtree is BST
return is_BST(root->left,min,root->key-1) && is_BST(root->right,root->key+1,max)

##Driver
is_BST(my_tree_root,KEY_MIN,KEY_MAX)
