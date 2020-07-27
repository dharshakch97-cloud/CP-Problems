// # largestNumber: Write the function largestNumber(text) that takes a string of text and 
// # returns the largest int value that occurs within that text, or 0 if no such value occurs. 
// # You may assume that the only numbers in the text are non-negative integers and 
// # that numbers are always composed of consecutive digits (without commas, for example). For example:
// #     	largestNumber("I saw 3 dogs, 17 cats, and 14 cows!")
// # returns 17 (the int value 17, not the string "17"). And
// #     	largestNumber("One person ate two hot dogs!")
// # returns None (the value None, not the string "None").


class largestnumber {
	public int fun_largestnumber(String s){
		String[] str = s.split(" ");
		int l = 0;
		for (int i = 0; i < str.length; i++) {
			try {
				int num = Integer.parseInt(str[i]);
				if (num > l)
					l = num;
			}	
			catch (Exception e) {
				continue;
			}
		}
		return l;
	}

	public static void main(String[] args) {
		largestnumber l = new largestnumber();
		System.out.println(l.fun_largestnumber("wehave15dogs2cats"));
	}
}
	