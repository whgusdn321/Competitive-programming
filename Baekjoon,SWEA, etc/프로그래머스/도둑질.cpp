#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> money) {
    int n = money.size();
    int arr1[n], arr2[n], arr3[n];
    fill(arr1, arr1+n, 0);
    fill(arr2, arr2+n, 0);
    fill(arr3, arr3+n, 0);
    arr1[0] = money[0];
    arr1[2] = money[2] + arr1[0];
    arr2[1] = money[1];
    arr3[2] = money[2];
    if (n==3)
        return max(money[0], max(money[2], money[1]));
    for (int i=3; i<n-1; i++){
        arr1[i] = max(money[i] + arr1[i-2], money[i] + arr1[i-3]);
    }

    for (int i=3; i<n; i++){
        arr2[i] = max(money[i] + arr2[i-2], money[i] + arr2[i-3]);
    }
    for (int i=3; i<n; i++){
        arr3[i] = max(money[i] + arr3[i-2], money[i] + arr3[i-3]);
    }
    int max1 = max(arr1[n-3], arr1[n-2]);
    int max2 = max(arr2[n-2], arr2[n-1]);
    int max3 = max(arr3[n-2], arr3[n-1]);
    return max({max1, max2, max3});

}