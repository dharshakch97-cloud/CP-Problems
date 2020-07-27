// # Write the function fun_nth_additive_prime(n) that takes a non-negative int n 
// # and returns the nth Additive Prime, which is a prime number such that 
// # the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5 
// # is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2


class nthtenlyprime {
	public boolean isPrime(int n) {
		if (n <= 1)
			return false;
		for (int i = 2; i < n; i++)
			if (n%i == 0)
				return false;
		return true;
	}

	public boolean istenly(int n) {
		int m = n;
		int s = 0;
		while (n!=0) {
			int r = n%10;
			n = n/10;
			s += r;
		}
		if (s == 10)
			return true;
		return false;
	}

	public int fun_nthtenlyprime(int n){
		int i = 2, c = 0;
		while (c <= n) {
			if (isPrime(i) && istenly(i)) {
				c++;
			}
			i++;
		}
		return i-1;
	}

	public static void main(String[] args) {
		nthtenlyprime t = new nthtenlyprime();
		System.out.println(t.fun_nthtenlyprime(1));
		System.out.println(t.fun_nthtenlyprime(4));
		System.out.println(t.fun_nthtenlyprime(10));
	}
}