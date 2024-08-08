class Solution
{
    public:
    void helper(Node* root, Node*& pre, Node*& suc, int key) {
        if(!root) {
            return;
        }

        helper(root->left, pre, suc, key);
        
        if(root->key < key) {
            pre = root;
        } 
        if(root->key > key && suc == NULL) {
            suc = root;
        }
        
        helper(root->right, pre, suc, key);
    }
    
    void findPreSuc(Node* root, Node*& pre, Node*& suc, int key)
    {
        // Your code goes here
        helper(root, pre, suc, key);
    }
};
