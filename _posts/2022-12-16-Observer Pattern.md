---
title: "[Design Pattern] 옵서버 패턴"
author:
  name: dongjun-Yi
categories: [Design Pattern]
tags: [java, design pattern]
render_with_liquid: false
---
**옵서버 패턴은 객체 사이에 일 대 다의 의존 관계를 두어, 어떤 객체의 상태가 변할 때 그 객체에 의존성을 가진 다른 객체들이 그 변화를 통지받고 자동으로 갱신될 수 있게 만드는 패턴**

옵서버 패턴이 언제 쓰면 유용한지 알아보기 위해 성적 출력 프로그램으로 예를 들어보자. 성적 출력 프로그램은 점수를 목록 형태로 출력하는 구조를 가지고 있다.

- ScoreRecord class : 점수를 저장/관리하는 클래스
- DataSheetView class : 점수를 목록형태로 출력하는 클래스

![Untitled.png](/assets/images/Observer Pattern/Untitled.png)

ScoreRecord

```java
public class ScoreRecord {
    private DataSheetView dataSheetView;
    private List<Integer> scores = new ArrayList<Integer>();

    public void setDataSheetView(DataSheetView dataSheetView) {
        this.dataSheetView = dataSheetView;
    }

    public void addScore(int score){
        scores.add(score);
        dataSheetView.update();
    }

    public List<Integer> getScoreRecord(){
        return scores;
    }

}
```

DataSheetView

```java
public class DataSheetView {
    private ScoreRecord scoreRecord;
    private int viewCount;

    public DataSheetView(ScoreRecord scoreRecord, int viewCount) {
        this.scoreRecord = scoreRecord;
        this.viewCount = viewCount;
    }
    public void update(){
        List<Integer> record = scoreRecord.getScoreRecord();
        displayScores(record, viewCount);
    }

    private void displayScores(List<Integer> record, int viewCount) {
        System.out.println("List of " + viewCount + " entries");
        for(int i=0; i< viewCount && i< record.size(); i++){
            System.out.println(record.get(i));
        }
    }
}
```

Main

```java
public class Main {
    public static void main(String[] args) {
        ScoreRecord scoreRecord = new ScoreRecord();
        DataSheetView dataSheetView = new DataSheetView(scoreRecord, 3);
        scoreRecord.setDataSheetView(dataSheetView);

        for(int index = 1; index <=5;index++){
            int score = index*10;
            System.out.println("Adding "+ score);
            scoreRecord.addScore(score);
        }
    }
}
```

위와 같이 실행하면 성적들을 리스트 형식으로 출력할 수 있게 된다.

### But,

성적을 다른 방식으로 출력해야 하거나, 성적을 동시에 여러가지 형태로 출력해야한다면?

ScoreRecord 클래스를 수정해야하고 다음과 같이 작성할 수 있다.

ScoreRecord

```java
public class ScoreRecord {
    private MinMaxView minmaxView;

    private List<DataSheetView> dataSheetViews = new ArrayList<DataSheetView>();
    private List<Integer> scores = new ArrayList<Integer>();

    public void setMinmaxView(MinMaxView minmaxView) {
        this.minmaxView = minmaxView;
    }

    public void addScore(int score){
        scores.add(score);

				//기존 코드 수정 -> OCP 위반
        minmaxView.update();
        for(DataSheetView dataSheetView : dataSheetViews){
            dataSheetView.update();
        }
    }

    public void addDataSheetView(DataSheetView dataSheetView){
        dataSheetViews.add(dataSheetView);
    }

    public List<Integer> getScoreRecord(){
        return scores;
    }

}
```

MinMaxView

```java
public class MinMaxView {
    private ScoreRecord scoreRecord;

    public MinMaxView(ScoreRecord scoreRecord) {
        this.scoreRecord = scoreRecord;
    }

    public void update(){
        List<Integer> record = scoreRecord.getScoreRecord();
        displayScores(record);
    }

    private void displayScores(List<Integer> record) {
        int min = Collections.min(record);
        int max = Collections.max(record);

        System.out.println("Min" + min + " Max" + max);
    }
}

```

Main

```java
public class Main {
    public static void main(String[] args) {
        ScoreRecord scoreRecord = new ScoreRecord();
        MinMaxView minMaxView = new MinMaxView(scoreRecord);
        DataSheetView dataSheetView3 = new DataSheetView(scoreRecord, 3);
        DataSheetView dataSheetView5 = new DataSheetView(scoreRecord, 5);

        scoreRecord.setMinmaxView(minMaxView);
        scoreRecord.addDataSheetView(dataSheetView3);
        scoreRecord.addDataSheetView(dataSheetView5);

        for(int index = 1; index <=5;index++){
            int score = index*10;
            System.out.println("Adding "+ score);
            scoreRecord.addScore(score);
        }
    }
}
```

요구사항에 맞게 변경된 위와 같은 코드를 보면 ScoreRecord 클래스에서 최대/최소 값을 출력하게 하는 방식으로 바뀌어서 minmaxview.update()로 변경 되고, 동시에 여러가지 방식으로 출력하기 위해 for문을 사용해 dataSheetView.update()로 코드가 변경된 것을 볼 수 있다.

즉, ScoreRecord 클래스가 변경되므로 **OCP에 위반되는것을 알 수 있다.**

이를 해결 하기 위해 변화되는 것을 식별하면 성적의 통보 대상이 변경될 때 기존 코드가 수정되기 때문에 **임의의 데이터가 변경 되었을 때 이에 관심을 가지는 모든 대상 객체에 통보하는 것을 인터페이슬 일반화**하는 것이 좋다. 이때 사용하는 것이 observer 패턴이다. observer 인터페이스를 이용하여 데이터가 변경됨을 감지하여 출력 방식에 맞게 해당하는 클래스를 사용하면 된다.

**Observer 클래스 다이어그램**

![Untitled1.png](/assets/images/Observer Pattern/Untitled 1.png)

Observer interface

```java
public interface Observer {
    public void update();
}
```

DataSheetView

```java
public class DataSheetView implements Observer{
    private ScoreRecord scoreRecord;
    private int viewCount;

    public DataSheetView(ScoreRecord scoreRecord, int viewCount) {
        this.scoreRecord = scoreRecord;
        this.viewCount = viewCount;
    }
    public void update(){
        List<Integer> record = scoreRecord.getScoreRecord();
        displayScores(record, viewCount);
    }

    private void displayScores(List<Integer> record, int viewCount) {
        System.out.println("List of " + viewCount + " entries");
        for(int i=0; i< viewCount && i< record.size(); i++){
            System.out.println(record.get(i));
        }
    }
}
```

MinMaxView

```java
public class MinMaxView implements Observer{
    private ScoreRecord scoreRecord;

    public MinMaxView(ScoreRecord scoreRecord) {
        this.scoreRecord = scoreRecord;
    }

    public void update(){
        List<Integer> record = scoreRecord.getScoreRecord();
        displayScores(record);
    }

    private void displayScores(List<Integer> record) {
        int min = Collections.min(record);
        int max = Collections.max(record);

        System.out.println("Min" + min + " Max" + max);
    }
}
```

ScoreRecord

```java
public class ScoreRecord {
    private List<Observer> observers = new ArrayList<Observer>();

    //Observer setter 메소드
    public void attach(Observer observer){
        observers.add(observer);
    }

    public void detach(Observer observer){
        observers.remove(observer);
    }
    private List<Integer> scores = new ArrayList<Integer>();

    public void addScore(int score){
        scores.add(score);

        for(Observer observer : observers){
            observer.update();
        }
    }

    public List<Integer> getScoreRecord(){
        return scores;
    }
}
```

Main

```java
public class Main {
    public static void main(String[] args) {
        ScoreRecord scoreRecord = new ScoreRecord();
        Observer minMaxView = new MinMaxView(scoreRecord);
        Observer dataSheetView3 = new DataSheetView(scoreRecord, 3);
        Observer dataSheetView5 = new DataSheetView(scoreRecord, 5);

        scoreRecord.attach(minMaxView);
        scoreRecord.attach(dataSheetView3);
        scoreRecord.attach(dataSheetView5);

        Random random = new Random();
        for(int index = 1; index <=5;index++){
            int score = random.nextInt(101);
            System.out.println("Adding "+ score);
            scoreRecord.addScore(score);
        }
    }
}
```

위와 같이 코드를 짜면 OCP에 위배되지 않고 코드를 구성할 수 있고 새로운 방식의 출력 방식이 추가되어도 기존 코드에 영향 없이 Observer 인터페이스를 상속하여 출력 방식을 지정해줄 수 있다.

그러나 ScoreRecord클래스를 살펴보면 옵서버들을 관리해주는 메소드 즉, attach, detach, update의 메소드들은 ScoreRecord클래스만 관리하는 것이 아닌 **데이터를 관리하는 다른 클래스들도 관리하게 된다.**

따라서 다른 클래스들도 사용할 수 있게 옵서버들 관리하는 인터페이스를 하나 만들어 다른 클래스들도 데이터를 관리 할 수 있게 만들 수 있다.

Subject 인터페이스를 구현한 ScoreRecord로 수정하면

Subject 

```java
public abstract class Subject {
    private List<Observer> observers = new ArrayList<Observer>();

    public void attach(Observer observer){
        observers.add(observer);
    }

    public void detach(Observer observer){
        observers.remove(observer);
    }

    public void notifyObservers(){
        for(Observer observer : observers){
            observer.update();
        }
    }
}
```

ScoreRecord

```java
public class ScoreRecord extends Subject{
    private List<Integer> scores = new ArrayList<Integer>();

    public void addScore(int score){
        scores.add(score);
        notifyObservers();
    }

    public List<Integer> getScoreRecord(){
        return scores;
    }
}
```

위와 같은 코드를 보게 되면 **Subject 클래스에는 성적 변경에 관심이 있는 대상 객체들의 관리하는것으로 구성**하고 ScoreRecord 클래스는 Subject 클래스를 상속받아 scores라는 데이터를 관리하는 클래스가 된다.

즉, Subject 클래스는 **옵서버 객체를 관리하는** 클래스, ScoreRecord 클래스는 **변경 관리 대상이 되는 데이터가 있는** 클래스가 된다. 

![Untitled1.png](/assets/images/Observer Pattern/Untitled 2.png)

- **Subject : 감시자들을 알고 있는 주체. 임의 개수의 감시자 객체는 주체를 감시할 수 있다. 주체는 감시자 객체를 붙이거나 떼는 데 필요한 인터페이스를 제공한다.**
- **Observer : 주체에 생긴 변화에 관심 있는 객체를 갱신하는 데 필요한 인터페이스를 정의. 이로써 주체의 변경에 따라 변화되어야 하는 객체들의 일관성을 유지.**
- **ConcreteSubject : ConecreteObserver 객체에게 알려주어야 하는 상태를 저장. 이 상태가 변경될 때 감시자에게 변경을 통보**
- **ConcreteObserver : ConcreteSubject 객체에 대한 참조자를 관리. 주체의 상태와 일관성을 유지해야 하는 상태를 저장. 주체의 상태와 감시자의 상태를 일관되게 유지하는 데 사용하는 갱신 인터페이스를 구현**

**옵서버 패턴은 통보 대상 객체의 관리를 Subject 클래스와 Observer 인터페이스로 일반화한다.**

**그러면 데이터 변경을 통보하는 클래스(Concrete Subject)는 통보 대상 클래스/객체(ConcreteObserver)에 대한 의존성을 제거할 수 있다. 결과적으로 옵서버 패턴은 통보 대상 클래스나 대상 객체의 변경에도 ConcreteSubject 클래스를 수정 없이 그대로 사용할 수 있도록 한다.**

위의 예에 적용하면 ScoreRecord 클래스는 ConcreteSubject의 역할, DataSheetView클래스와 MinMaxView 클래스는 ConcreteObserver 역할을 한다.

<aside>
📖 references                                                                                                                                     정인상, 「JAVA 객체지향 디자인 패턴」, 한빛미디어

</aside>