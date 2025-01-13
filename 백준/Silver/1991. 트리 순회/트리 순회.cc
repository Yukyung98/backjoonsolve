#include <iostream>
using namespace std;
int n;
pair<char,char> tree[26];

void preoder(char alp){
    if(alp == '.') return;

    std::cout << alp;
    preoder(tree[alp-'A'].first);
    preoder(tree[alp-'A'].second);
}
void inorder(char alp){
    if(alp == '.') return;

    inorder(tree[alp-'A'].first);
    std::cout << alp;
    inorder(tree[alp-'A'].second);
}
void postorder(char alp){
    if(alp =='.') return;

    postorder(tree[alp-'A'].first);
    postorder(tree[alp-'A'].second);
    std::cout << alp;
}
int main(){
    cin >> n;
    for(int i = 0;i<n;i++){
        char parent,left,right;
        cin >> parent>>left>>right;
        tree[parent-'A'].first = left;
        tree[parent-'A'].second = right;
    }
    preoder('A');
    cout<<"\n";
    inorder('A');
    cout<<"\n";
    postorder('A');
}