#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
    vector<string> croatian = { "c=","c-","dz=","d-","lj","nj","s=","z=" };
    int index;
    string s;
    cin >> s;
    for (int i = 0; i < croatian.size(); i++) {
        while (1)
        {
            index = s.find(croatian[i]);
            if (index == string::npos)
                break;
            s.replace(index, croatian[i].length(), "#");
        }
    }
    cout << s.length();
  
    

}

