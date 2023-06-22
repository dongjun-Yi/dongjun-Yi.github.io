---
title: "[Design Pattern] 빌더 패턴"
author:
  name: dongjun-Yi
categories: [Design Pattern]
tags: [java, design pattern]
render_with_liquid: false
---
**빌더 패턴은 복잡한 객체를 생성하는 방법과 표현하는 방법을 정의하는 클래스를 별도로 분리하여 서로 다른 표현이라도 이를 생성할 수 있는 동일한 절차를 제공하는 패턴**

book 클래스를 예로 들어 살펴보자

생성자의 인자가 많을 경우 일반적인 객체를 생성하는 방식은 다음과 같다. 

**Book(Telescoping Constructor pattern)**

```java
public class Book {
    private Long id;
    private String isbn;
    private String title;
    private String author;
    private int pages;
    private String category;

    public Book(Long id, String isbn) {
        this.id = id;
        this.isbn = isbn;
    }

    public Book(Long id, String isbn, String title) {
        this.id = id;
        this.isbn = isbn;
        this.title = title;
    }

    public Book(Long id, String isbn, String title, String author) {
        this.id = id;
        this.isbn = isbn;
        this.title = title;
        this.author = author;
    }

    public Book(Long id, String isbn, String title, String author,
                int pages) {
        this.id = id;
        this.isbn = isbn;
        this.title = title;
        this.author = author;
        this.pages = pages;
    }

    public Book(Long id, String isbn, String title, String author,
                int pages, String category) {
        this.id = id;
        this.isbn = isbn;
        this.title = title;
        this.author = author;
        this.pages = pages;
        this.category = category;
    }
}
```

그러나 이 방식은 인자가 많을수록 생성자 개수도 많아진다.

따라서 생성자의 인자가 어떤 의미인지를 파악하기 힘들며 가독성이 떨어지게 된다.

## JavaBeans Pattern

→ Setter 메소드로 각 속성의 값을 설정

**Book**

```java
public class Book{
    public Book() { }
    public void setId(Long id) { this.id = id; }
    public void setIsbn(String isbn) { this.isbn = isbn; }
    public void setTitle(String title) { this.title = title; }
    public void setAuthor(String author) { Author = author; }
    public void setPages(int pages) { this.pages = pages; }
    public void setCategory(String category) { this.category = category;}
}
```

Main

```java
public class Main {
    public static void main(String[] args) {
      Book book1 = new Book(1L, "isbn1234");
			book1.setCategory("CE");
    }
}
```

javaBeans 방식을 사용하면 **가독성은 향상되나** **immutable object를 만들수 없다.**

immutable 객체란 외부에서 값을 변경할수 있는 객체를 뜻한다.

## Builder Pattern

다음의 3가지 상황이 필요할 떄 빌더 패턴이 효과적이다.

- 생성자의 인자가 많거나
- 생성자의 인자들 중에 필수적 인자와 선택적 인자가 혼합되어 있는 경우
- immtuable 객체를 생성

**Book**

```java
public class Book {
    private Long id;
    private String isbn;
    private String title;
    private String author;
    private int pages;
    private String category;

    public Long getId() {
        return id;
    }

    public String getIsbn() {
        return isbn;
    }

    public String getTitle() {
        return title;
    }

    public String getAuthor() {
        return author;
    }

    public int getPages() {
        return pages;
    }

    public String getCategory() {
        return category;
    }
    public static class BookBuilder {
        private Long id;
        private String isbn;
        private String title;
        private String author;
        private int pages;
        private String category;

        public BookBuilder(Long id, String isbn) {
            this.id = id;
            this.isbn = isbn;
        }

        public BookBuilder Id(Long id) {
            this.id = id;
            return this;
        }

        public BookBuilder ISbn(String isbn) {
            this.isbn = isbn;
            return this;
        }

        public BookBuilder title(String title) {
            this.title = title;
            return this;
        }

        public BookBuilder author(String author) {
            this.author = author;
            return this;
        }

        public BookBuilder pages(int pages) {
            this.pages = pages;
            return this;
        }

        public BookBuilder category(String category) {
            this.category = category;
            return this;
        }

        public Book build() {
            Book book = new Book();
            book.id = this.id;
            book.isbn = this.isbn;
            book.author = this.author;
            book.title = this.title;
            book.pages = this.pages;
            book.category = this.category;
            return book;
        }
    }
}
```

Main

```java
public class Main {
    public static void main(String[] args) {
        Book book1 = new Book.BookBuilder(1L, "isb1234")
                .author("sanguining")
                .pages(360).category("CE")
                .title("Design Pattern").category("CE")
                .build();

        System.out.println(book1.getAuthor());

    }
}
```

→ builder 패턴을 적용하여 객체를 생성하게 되면 가독성이 개선되고, 메소드 체인닝과 immutable 객체를 생성할 수 있게 된다.

## Lombok Builder Pattern

@builder 어노테이션 사용

Book

```java
import lombok.Builder;
import lombok.Getter;
import lombok.NonNull;
@Builder
@Getter
public class Book {
    @NonNull
    private Long id;
    @NonNull
    private String isbn;
    private String title;
    private String author;
    private int pages;
    private String category;
}
```

Main

```java
Book book1 = new Book.BookBuilder().id(2L)
                .isbn("isbn1234")
                .author("sanguining")
                .pages(360).category("CE")
                .title("Design Pattern").category("CE")
                .build();

        System.out.println(book1.getAuthor());
```

<aside>
📖 references                                                                                                                                     정인상, 「JAVA 객체지향 디자인 패턴」, 한빛미디어

</aside>