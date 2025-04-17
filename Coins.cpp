


int main(){

    int n, x;
    cin >> n >> x;
    vector<int> coins(n);
    for(int i = 0; i < n; i++){
        cin >> coins[i];
    }


    vector<int> dp(x + 1, INT_MAX);

    dp[0] = 0;

    for(int i = 0; i < n; i++){
        for(int j = 0; j < x; j++){
            if(j >= coins[i]){
                dp[j] = min(dp[j], dp[j - coins[i]] + 1);
            }
        }
    }


    if(dp[x] == INT_MAX) {
        cout << -1 << endl;
    } 
    else {
        cout << dp[x] << endl; 
    }
    return 0;
}