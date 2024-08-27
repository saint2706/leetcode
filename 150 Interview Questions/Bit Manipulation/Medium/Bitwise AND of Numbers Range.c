int rangeBitwiseAnd(int m, int n){
    int sum = 0, val1 = m, val2 = n;
    long int k = 1;
    while(m>0){
        if(m&1 && n&1){
            if(val2-val1<k){
                sum+=k;
            }
        }
        m=m>>1;
        n=n>>1;
        k=k<<1;
    }
    return sum;
}