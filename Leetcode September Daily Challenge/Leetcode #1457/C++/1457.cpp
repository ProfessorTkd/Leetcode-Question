#define tn TreeNode 
class Solution {
public:
int ans =0;
vector<int> vis;
void solve(tn *root){
    if(!root)return;
    vis[root->val]++;
    if(root->left==NULL and root->right==NULL){            
        int odd=-1;
        bool ok =true;
        for(int i=1;i<=9;i++){
            if(vis[i] %2   and (odd==-1)){
                odd=1;                    
            }
            else if(vis[i]%2){
                ok=false;
                break;
            }
        }
        if(ok) ans++;            
        
    }        
    solve(root->left);
    solve(root->right);
    vis[root->val]--;
}
int pseudoPalindromicPaths (TreeNode* root) {
    vis.resize(10,0);
    solve(root);
    return ans;
}
