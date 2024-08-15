---
title: "[Clean Code] 7장. 오류 처리"
author:
  name: dongjun-Yi
categories: [clean code]
tags: [clean code]
render_with_liquid: false
---

## Use Exceptions Rather than Return Codes
---
**DeviceController.java**

```java
public class DeviceController {
	...

	public void sendShutDown() {
		DeviceHandle handle = getHandle(DEV1); // Check the state of the device
		if (handle != DeviceHandle.INVALID) {
			// Save the device status to the record field retrieveDeviceRecord(handle);
			// If not suspended, shut down
			if (record.getStatus() != DEVICE_SUSPENDED) {
				pauseDevice(handle);
				clearDeviceWorkQueue(handle);
				closeDevice(handle);
			} else {
				logger.log("Device suspended. Unable to shut down");
			}
		} else {
			logger.log("Invalid handle for: " + DEV1.toString()); }

	...
}
```

위의 코드를 보면 함수 호출자는 함수를 호출 후 에러 발생 여부를 체크를 하는 코드가 있다. 이러한 에러 체크는 호출자에게 혼란을 준다.
함수의 호출자는 에러 발생여부를 확인하기 위해 오류 코드를 작성하는 것보다 **에러를 마주했을 때는 예외를 발생시키는게 더 낫다**. 그러면 호출자의 코드는 더 깔끔해지게 되고 이러한 오류 처리는 논리가 모호해지지 않는다.

**DeviceController.java**

```java
public class DeviceController {
	...

	public void sendShutDown() {
		try {
			tryToShutDown();
		} catch (DeviceShutDownError e) {
			logger.log(e);
		}
	}

	private void tryToShutDown() throws DeviceShutDownError {
		DeviceHandle handle = getHandle(DEV1);
		DeviceRecord record = retrieveDeviceRecord(handle);
		pauseDevice(handle);
		clearDeviceWorkQueue(handle);
		closeDevice(handle);
	}

	private DeviceHandle getHandle(DeviceID id) { ...
		throw new DeviceShutDownError("Invalid handle for: " + id.toString());
		...
	}

	...
}
```

위와 같이 예외를 발생시키는 코드는 중요한 2가지가 있다. 장치 종료 알고리즘과 오류처리가 나뉘어 작성되어 2개의 **관심사가 분리**된 것이다. 따라서 코드를 읽게 되면 **2개의 기능을 독립적으로 작동**되는 것을 살펴볼 수 있다.

## Write your Try-catch-Finally Statement First

---

`try` 블럭은 마치 **트랜잭션**과 같다. **트랜잭션**은 데이터베이스에서 수행하는 여러 작업들이 하나의 단위로 처리되어 **모두 성공하거나 모두 실패**하는 것을 보장하는 개념인데 `try` 블럭도 성공과 실패에 대해서 명확하게 이루어지기 때문에 이는 트랜잭션과 유사하다.
`try` 블럭에서 비즈니스 로직을 수행하고, 코드가 실행에 실패할 수 있다는 예측이 가능하다.

파일을 열고 파일의 내용을 읽는 예를 살펴보자.

```java
@Test(expected = StorageException.class)
public void retrieveSectionShouldThrowOnInvalidFileName() {
	sectionStore.retrieveSection("invalid - file");
}
```

```java
public List<RecordedGrip> retrieveSection(String sectionName) {
	// dummy return until we have a real implementation
	return new ArrayList<RecordedGrip>();
}
```

위의 코드는 실행하면 빈 객체를 반환하기 때문에 테스트에 실패한다.

```java
public List<RecordedGrip> retrieveSection(String sectionName) {
	try {
	    FileInputStream stream = new FileInputStream(sectionName)
	} catch (Exception e) {
	    throw new StorageException("retrieval error", e);
	}
	    return new ArrayList<RecordedGrip>();
}
```

위의 코드는 예외 처리를 했기 때문에 테스트가 통과한다. 여기서 더 **예외 처리를 구체적**으로 다루면 다음과 같이 코드를 바꿀 수 있다.

```java
public List<RecordedGrip> retrieveSection(String sectionName) {
	try {
	    FileInputStream stream = new FileInputStream(sectionName);
		stream.close();
	} catch (FileNotFoundException e) {
	    throw new StorageException("retrieval error”, e);
	}
	return new ArrayList<RecordedGrip>();
}
```

위의 코드는 예외 클래스를 `FileNotFoundException`으로 선언하여 **예외 범위를 좁혀** 파일을 찾을 수 없는 에러에 대해서 헨들링을 하여 코드를 읽을 때 어떤 상황에서 **예외가 발생할지 예측**할 수 있게 된다.

이처럼 예외를 강제하는 테스트를 작성하고 테스트를 만족하기 위한 `catch` 블럭을 작성하게 되면
**트랜잭션의 범위를 구축**하고 **해당 범위에서 발생하는 예외**를 짐작할 수 있어 트랜잭션 특성을 유지하는데 도움을 준다.

## Use Unchecked Exception

---

`Cheked Exception`의 경우 예외 처리를 강제한다. 이 특징 때문에 `Checked Exception`은 확장에는 열려있고 수정에는 닫혀있어야 하는 `OCP` 원칙을 위반한다.

예를 들어 3단계에 거쳐서 호출하는 구조를 가진 함수에서 만약 가장 늦게 불리는 함수가 `Checked Exception` 예외를 발생시키는 코드로 수정됐다면, 이는 상위 호출자의 함수에도 `throws`를 추가해줘야 되기 때문에 하위 함수 때문에 **모든 상위 함수들이 수정해야 하는 문제**가 발생하게 된다.

이러한 전파되는 수정사항 때문에 캡슐화의 외부로 부터 세부사항을 숨기는 특징을 지키지 못해 하위 레벨의 세부 사항을 상위 레벨에서 알아야 하도록 강제되는 것이다.

`Checked Exception`은 가끔 중요한 라이브러리를 작성할 때 반드시 잡아야 하는 오류를 처리할 때 유용하지만 일반적인 애플리케이션 개발에서는 의존성 비용이 장점들보다 더 많이 든다.

## Provide Context with Exceptions

---

예외를 발생시킬 때 **충분한 정보가 담긴 에러 메세지**를 만들고 예외를 발생시켜야 에러가 발생했을 때 원인을 찾기 쉽게 된다.

## Define Exception Classes in Terms of a Caller’s Needs

---

```java
ACMEPort port = new ACMEPort(12);

try {
    port.open();
} catch (DeviceResponseException e) {
    reportPortError(e);
    logger.log("Device response exception", e);
} catch (ATM1212UnlockedException e) {
    reportPortError(e);
    logger.log("Unlock exception", e);
} catch (GMXError e) {
    reportPortError(e);
    logger.log("Device response exception");
} finally {
	...
}

```

```java
LocalPort port = new LocalPort(12);

t시ry {
    port.open();
} catch (PortDeviceFailure e) {
    reportError(e);
    logger.log(e.getMessage(), e);
} finally {
	...
}

public class LocalPort {
	private ACMEPort innerPort;

	public LocalPort(int portNumber) {
	    innerPort = new ACMEPort(portNumber);
	}

	public void open() {
		try {
		    innerPort.open();
		} catch (DeviceResponseException e) {
		    throw new PortDeviceFailure(e);
		} catch (ATM1212UnlockedException e) {
    		    throw new PortDeviceFailure(e);
		} catch (GMXError e) {
		    throw new PortDeviceFailure(e);
		}
	}
	...
}
```

위의 코드와 아래 코드를 비교해보면 위에 코드는 하나의 `try`문에 여러 `catch`문이 선언되어 있지만 두번째 코드에서는 Third-party Library를 이용한 API 안에 예외처리를 해두어 외부로부터 세부구현을 숨기고 실제 `port`를 `open`하는 로직에 대해서만 `try catch`문을 작성한 것이다. 이렇게 되면 코드를 더 간소화하고 예외를 발생시키는 클래스를 정의하여 어떤 예외가 발생하는 지를 명확하게 알 수 있다.

> 따라서 하나의 예외 클래스로 여러 오류를 처리할 수 있으면 단일 예외 클래스를 사용하고, 특정 예외를 구분하여 처리할 필요가 있다면, 서로 다른 예외 클래스를 정의하는 것이 더 나은 선택이다.

## Define the Normal Flow

---

```java
try {
	MealExpenses expenses = expenseReportDAO.getMeals(employee.getID());
	m_total += expenses.getTotal();
} catch(MealExpensesNotFound e) {
	m_total += getMealPerDiem();
}
```

위의 코드는 식사비가 지출된 경우 총 금액에 더하는 로직이다. 만약 식사비가 지출이 되지 않았다면 그날의 일당 식사량을 총액에 더하는 로직이다. 이 코드는 예외로 인해 기본 비즈니스 로직까지 복잡해지는 경우이며 특별한 경우를 다루는 코드를 작성해야 단순해진다.

```java
public class PerDiemMealExpenses implements MealExpenses {
	public int getTotal() {
		// return the per diem default
	}
}
```

위 코드는 항상 `MealExpense` Object를 반환하는 코드이며, 만약 식사비 지출이 없다면 일당 식사비를 가진 객체를 반환하게 된다.

위와 같은 패턴을 `Special Case Pattern`이라고 한다. 특별한 경우를 다루는 클래스로, 이렇게 특별한 경우를 클래스안에 함수로 감싸 예외 처리를 안해도 되게 된다.

## Don’t Return Null

---

`Null`을 반환하지 마라.

```java
public void registerItem(Item item) {
	if (item != null) {
		ItemRegistry registry = peristentStore.getItemRegistry();
		if (registry != null) {
			Item existing = registry.getItem(item.getID());
			if (existing.getBillingPeriod().hasRetailOwner()) {
				existing.register(item);
			}
		}
	}
}

```

`Null`값이 return되는 것을 예상하고 예외 처리를 수행하고 있다. 이는 호출자에게 문제를 떠넘기는 구조로, 만약 `Null`을 넘기는 로직을 작성하게 되면 이대신 예외를 던지거나, `Special Case Object`를 반환하도록 하라.

```java
List<Employee> employees = getEmployees();
if (employees != null) {
	for(Employee e : employees) {
		totalPay += e.getPay();
	}
}
```

만약 위와 같이 `Null`를 반환하는 `getEmployees()`를 `Null`이 아닌 빈 리스트로 반환한고 하면 코드는 다음과 같이 수정된다.

```java
List<Employee> employees = getEmployees();
for(Employee e : employees) { // if check문이 없어짐.
	totalPay += e.getPay();
}

public List<Employee> getEmployees() {
	if( .. there are no employees .. )
		return Collections.emptyList();
}
```

위와 같이 작성하면 `NullPointException`을 최소화하고 코드가 깔끔해진다.

## Dont Pass Null

---

함수의 매개변수나 return 값으로 `Null` 값을 전달하면 안된다. 왜냐하면 이는 `NullPointException`을 발생할 뿐만 아니라 이를 예외처리 한들 `Runtime Error`가 발생하기 때문에 `Null` 값을 넘겨주는 로직은 지양해야 한다.

Robert C. Martin - Clean Code\_ A Handbook of Agile Software Craftsmanship-Prentice Hall (2008)
