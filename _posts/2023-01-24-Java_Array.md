---
title: "[자바의 정석] 배열"
author:
  name: dongjun-Yi
categories: [java]
tags: [java]
render_with_liquid: false
---
## 배열이란?

---

같은 타입의 여러 변수를 하나의 묶음으로 다루는 것을 배열이라고 한다.

## 배열의 선언과 생성

---

| 선언방법 | 선언 예 |
| --- | --- |
| 타입 [] 변수이름; | int [] score;
String [] name; |
| 타입 변수이름[]; | int score[];
String name[]; |

### 배열의 생성

배열의 선언은 생성된 배열을 다루기 위한 참조변수를 위한 공간이 만들어질 뿐이고, 배열을 생성해야만 비로소 값을 저장할 수 있는 공간이 만들어지는 것이다. 

배열을 생성하기 위해서는 연산자 ‘new’와 함께 배열의 타입과 길이를 지정해줘야 한다.

<aside>
👉 타입 [] 변수이름; //배열 선언
변수이름 = new 타입[길이]; //배열 생성

</aside>

배열 생성 과정

```java
int [] score;
score = new int[5];
```

1. int [] score;
    - int형 배열 참조변수 score를 선언한다. 데이터를 저장할 수 있는 공간은 아직 마련되지 않았다.
2. score = new int[5];
    - 연산자 ‘new’에 의해서 메모리의 빈 공간에 5개의 int형 데이터를 저장할 수 있는 공간이 마련된다.
    - 각 배열 요소는 자동적으로 int의 기본값(default)인 0으로 초기화 된다.
    - 끝으로 대입 연산자’=’에 의해 배열의 주소가 int형 배열 참조변수 score에 저장된다.
        
        ![Untitled.png](/assets/images/Java_Array/Untitled.png)

## 배열의 길이와 인덱스

---

생성된 배열의 각 저장공간을 **배열의 요소(element)**라고 하며, 배열이름[인덱스]의 형식으로 배열에 요소에 접근한다. **인덱스(index)**는는 배열의 요소마다 붙여진 일련번호로 각 요소를 구별하는데 사용된다.

<aside>
👉 **인덱스(index)**의 범위는 0부터 ‘배열길이-1’까지

</aside>

배열 예제

```java
public static void main(String[] args) { 
		int[] score = new int[5];
		int k = 1;

		score[0] = 50;
		score[1] = 60;
		score[k+1] = 70;   // score[2] = 70
		score[3] = 80;
		score[4] = 90;

		int tmp = score[k+2] + score[4];  // int tmp = score[3] + score[4]

	    // for문으로 배열의 모든 요소를 출력한다.
		for(int i=0; i < 5; i++) {
			System.out.printf("score[%d]:%d%n",i, score[i]);		
		}

		System.out.printf("tmp:%d%n", tmp);
		System.out.printf("score[%d]:%d%n",7,score[7]); //index의 범위를 벗어난 값
	} // main
```

```java
//실행결과
score[0]:50
score[1]:60
score[2]:70
score[3]:80
score[4]:90
tmp:170
Exception in thread "main" java.lang.ArrayIndexOutOfBoundsException: Index 7 out of bounds for length 5
	at OperatorEx22.main(OperatorEx22.java:20)
```

배열 인덱스 범위에 속하지 않는 7을 배열의 인덱스로 해서 값을 출력하면 에러가 발생한다. 컴파일 시에는 아무런 문제가 없지만 실행 시에는 에러가 발생한다.

### 배열의 길이

- 배열의 길이는 int 범위의 양의 정수(0도 포함)이어야 한다.
- JVM에서는 모든 배열의 길이를 별도로 관리하며 ‘배열이름.length’를 통해 배열의 길이를 알 수 있다.
    
    ```java
    int [] arr = new int[5];
    int tmp = arr.length;
    ```
    
    - 배열은 한번 생성하면 길이를 변경할 수 없기 대문에, 이미 생성된 배열의 길이는 변하지 않느다.

## 배열의 초기화

---

```java
int [] score = new int[]{50,60,70,80,90}; //배열의 생성과 초기화를 동시에
int [] score = {50,60,70,80,90}; //new int[] 생략 가능
int [] score = {}; //길이가 0인 배열, new int[]가 생략됨
```

위와 같이 배열의 초기화는 생성과 동시에 가능하며, 배열의 선언과 생성을 따로 하는 경우는 new int[]를 생략할 수 없다.

```java
int [] score;
score = {50,60,70,80,90}; //에러, new int[]를 생략할 수 없음
```

### 배열의 출력

배열을 출력하면 배열의 주소가 아닌 ‘타입@주소’형태로 출력된다.

```java
int [] Arr = {100, 95, 90, 70, 60};
System.out.println(Arr); //[I@14318bb와 같은 형식의 문자열이 출력된다.
```

## 다차원 배열

---

| 선언 방법 | 선언 예 |
| --- | --- |
| 타입[][] 변수이름; | int [][] score; |
| 타입 변수이름[][]; | int score[][]; |
| 타입[] 변수이름[]; | int [] score[]; |

2차원 배열 예제

```java
class ArrayEx18 {
	public static void main(String[] args) {
		 int[][] score = {
							{ 100, 100, 100}
							, { 20, 20, 20}
							, { 30, 30, 30}
							, { 40, 40, 40}
						};
		int sum = 0;

		for(int i=0;i < score.length;i++) {
			for(int j=0;j < score[i].length;j++) {
				System.out.printf("score[%d][%d]=%d%n", i, j, score[i][j]);
			}
		}

		for (int[] tmp : score) { 
			 for (int i : tmp) { 
				sum += i;
			 } 
		} 

		System.out.println("sum="+sum);
	}
}
```

```java
//실행결과
score[0][0]=100
score[0][1]=100
score[0][2]=100
score[1][0]=20
score[1][1]=20
score[1][2]=20
score[2][0]=30
score[2][1]=30
score[2][2]=30
score[3][0]=40
score[3][1]=40
score[3][2]=40
sum=570
```

위와 같이 자바는 2차원 이상의 배열은 배열의 배열 형태로 처리된다.

<aside>
📖 references Java의 정석(3판) [남궁 성/도우출판/2016]

</aside>