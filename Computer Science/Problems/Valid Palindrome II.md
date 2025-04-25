
Given a string `s`, return `true` _if the_ `s` _can be palindrome after deleting **at most one** character from it_.

Sounds easy right?
Consider these two cases :
``` 
cuppucu
eceec 
```

```java
class Solution {

    public boolean validPalindrome(String s) {
        //check counts may be just to be sure only 1 char is extra?
        boolean relacedYet = false;
        int l = 0 , r = s.length()-1;
        while(l<r){
            if(s.charAt(l)==s.charAt(r)){
                l++;r--;
            }
            else if (relacedYet == false){
                //baabc
                //b != c
                if(s.charAt(l) == s.charAt(r-1)){
                    r--;r--;
                    l++;
                    relacedYet = true;
                }
                else if(s.charAt(l+1) == s.charAt(r)){
                    l++;l++;
                    r--;
                    relacedYet = true;
                }
                else{
                    return false;
                }
            }
            else{
                return false;
            }
        }
        return true;
    }
}
```


This approach fails no matter what for the above two inputs since we can either only choose left or right. We can not traverse on both paths to check if we get a palindrome later. So the solution is traversing both the paths. There is simply no other way.

So here it goes!

``Nice: First recursion problem that I solved without looking at solution!!!

```java
class Solution {
    public boolean validPalindrome(String s) {
        return checkPalindrome(s,0, s.length() -1, false);
    }
    private boolean checkPalindrome(String s, int l, int r, boolean deletedSoFar){
        if(l>=r){
            return true;
        }
        if(s.charAt(l) == s.charAt(r)){
            return checkPalindrome(s,l+1,r-1,deletedSoFar);
        }
        else{
            if(deletedSoFar){
                return false;
            }
            return checkPalindrome(s,l+1,r,true) || checkPalindrome(s,l,r-1,true);
        }
    }
}
```

```java

-------Most Optimized-----

class Solution {
    public boolean validPalindrome(String s) {
        int n = s.length();
        byte[] cs = new byte[n];
        s.getBytes(0, n, cs, 0);
        return isPalindrome(cs, 0, n-1, true);
    }

    private boolean isPalindrome(byte[] arr, int start, int end, boolean canDelete) {
        while (start < end) {
            if (arr[start] != arr[end]) {
                if (!canDelete) {
                    return false;
                }
                return isPalindrome(arr, start+1, end, false)
                        || isPalindrome(arr, start, end-1, false);
            }
            ++start;
            --end;
        }
        return true;
    }
}
```