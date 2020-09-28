#include <bits/stdc++.h>

using namespace std;

void print(auto x){
    for(auto t : x){
        cout << t << ' ';
    }
    cout << '\n';
}

int main()
{
    int n, d, m;
    int arr[100001];
    cin >> n >> d >> m;
    for(int i=0; i<n; i++)
        cin >> arr[i];
    vector<int> sharps_, flats_;
    vector<long long> sharps, flats;
    for(int i=0; i<n; i++){
        if(arr[i] > m){
            sharps_.push_back(arr[i]);
        }
        else{
            flats_.push_back(arr[i]);
        }
    }
    sort(sharps_.begin(), sharps_.end(), greater<int>());
    sort(flats_.begin(), flats_.end(), greater<int>());
    print(sharps_);
    print(flats_);
    // make sum vecs
    long long sum = 0;
    for(int x:sharps_){
        sum += x;
        sharps.push_back(sum);
    }
    sum = 0;
    for(int x:flats_){
        sum += x;
        flats.push_back(sum);
    }
    cout << "sharps is : ";
    print(sharps);
    cout << "flats is : ";
    print(flats);
    
    int num_sharps = ceil(sharps.size()/double(d+1)); // min sharps
    int num_flats = n - sharps.size();
    vector<long long> ans;
    cout << '\n';
    while(num_flats >= 0 && num_sharps <= sharps.size()){
        cout << "num_sharps : " << num_sharps << '\n';
        cout << "num_flats : " << num_flats << '\n';
        long long tmp = 0;
        if(num_sharps > 0) 
            tmp += sharps[num_sharps-1];
        if(num_flats > 0)
            tmp += flats[num_flats-1];
         cout << "tmp : " << tmp << '\n';
        ans.push_back(tmp);
        num_sharps += 1;
        num_flats -= (d+1);
    }
    cout << *max_element(ans.begin(), ans.end()) << '\n';
    return 0;
}
