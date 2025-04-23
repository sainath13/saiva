
```java

public static String sortString(String inputString){
	char tempArray[] = inputString.toCharArray();
	Arrays.sort(tempArray);
	return new String(tempArray);
}

```