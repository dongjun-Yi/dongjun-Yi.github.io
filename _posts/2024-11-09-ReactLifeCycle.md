---
title: "React 라이프사이클"
author:
  name: dongjun-Yi
categories: [react]
tags: [react, javascript]
render_with_liquid: false
---
## 라이플사이클이란?

---

컴포넌트가 생성되고, 업데이트, 제거 까지의 과정을 말한다. 리액트 라이플사이클에서는 3가지의 단계로 나뉜다: **마운트(Mount)**, **업데이트(Update),** **언마운트(Unmount)**

- Mount : 컴포넌트가 생성되어 DOM에 추가되는 단계다. 이는 화면에 처음으로 랜더링 될 때를 말한다.
- Update : 컴포넌트가 상태(state)나 props의 변화로 인해 재렌더링되는 단계다. 화면에 리랜더링 될때를 말한다.
- Unmount : 컴포넌트가 DOM에서 제거되는 단계다. 이는 화면에서 사라질때를 말한다.

이 라이플 사이클 단계별로 컴포넌트들이 각각 다른  수행하도록 만드는 것을 라이플 사이클 제어라고 한다. 이 라이프 사이클 제어는 React의 hook인 `useEffect`를 이용해 제어할 수 있다.

## useEffect

---

`useEffect`란 React 컴포넌트의 **Side Effect**를 제어하는 `React hook`이다. 여기서 **Side Effect**란 컴포넌트의 동작에 따라 파생되는 여러 효과를 말한다. 예를 들어 컴포넌트 내부에 값이 변경되면 콘솔에 변경된 값을 출력하는 행위는 변경되는 행위에서 파생되는 **Side Effect**가 된다. 이러한 **Side Effect**를 제어하고 싶을 때는 useEffect를 통해 제어할 수 있다.

```jsx
// mount
useEffect(()=> {
   console.log('mount');
}, []);

// update
useEffect(()=> {
   console.log('update');
});

//unmount
useEffect(() => {
	return () => {
	  console.log('unmount'); //Clean up
  };
}, []);
```

- mount: `useEffect`로 의존성 배열에 빈 배열을 주게 되면 처음 랜더링 시점에만 `useEffect`에 setup 부분의 코드가 실행된다.
- update : 의존성 인자에 빈 값을 주게되면 화면이 랜더링 될 때마다 호출된다.
- unmount: `useEffect`에 `return`문을 사용하면 화면에서 컴포넌트가 사라질 때 실행하게 된다.

![Untitled.png](/assets/images/ReactLifeCycle/image.png)

<aside>
📖 references 
[https://ko.react.dev/reference/react/useEffect](https://ko.react.dev/reference/react/useEffect)

[https://github.com/Wavez/react-hooks-lifecycle](https://github.com/Wavez/react-hooks-lifecycle)

</aside>