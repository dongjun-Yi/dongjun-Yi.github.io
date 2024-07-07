---
title: "[JavaScript] Common Js 와 ES6 Module"
author:
  name: dongjun-Yi
categories: [javascript]
tags: [javascript, nodejs]
render_with_liquid: false
---

자바스크립트의 모듈 시스템은 코드를 분리해 유지보수성을 높여준다. 모듈 시스템 중 가장 대표적인 `Common JS`와 `ES6 Module` 시스템에 대해서 알아보자.

## Common JS

---

`Common JS`는 NodeJS에서 주로 사용되는 모듈 시스템으로 `require`와 `export` 키워드를 통해 모듈을 가져오고 내보낼 수 있다.
예제로 숫자를 더하고 빼는 기능을 모듈화하여 `math.js`를 사용해보는 기능을 만들면 아래와 같다.

**math.js**

```jsx
function add(a, b) {
	return a + b;
}

function sub(a, b) {
	return a - b;
}

module.exports = {
	add,
	sub
}
```

**main.js**

```jsx
const moduleData = require('./math.js');

console.log(moduleData.add(1, 2)); // 3
console.log(moduleData.minus(1, 2)); // -1
```

`math.js`에서 `add`와 `minus` 함수를 정의하고 이를 `export`로 내보내 `main.js`에서 이 내보낸 모듈을 `require()`로 사용할 수 있다. 그러면 `require`로 받아온 모듈에서 객체형태로 받아 `add`와 `minus`를 사용할 수 있다.

## ES6 Module

---

`ES6 Module` 시스템은 ECMAScript 2015(ES6)에서 처음 나온 모듈 시스템으로 `import`와 `export` 키워드를 통해 모듈을 내보내고 가져올 수 있다.
자바스크립트는 기본적으로 `CommonJS` 방식을 사용하고 있기 때문에 `ES6 Module` 시스템을 사용하려면 `package.json`에서 `type`을 `module`로 명시해줘야 사용할 수 있다.

**package.json**

```jsx
{
  ...
  "type": "module"
}

```

위와 같이 `package.json`을 설정해줬다면 더하고 뺴는 기능을 `math.js` 에 정의하고 `main.js`에서 이를 가져다 쓰는 코드를 작성하면 아래와 같이 작성할 수 있다.

**math.js**

```jsx
function add(a, b) {
	return a + b;
}

function sub(a, b) {
	return a - b;
}

export { add, sub};
```

**main.js**

```jsx
import { add, sub} from './math.js';

console.log(add(1, 2)); // 3
console.log(minus(1, 2)); // -1
```

ES6 모듈 시스템에서 모듈의 함수를 내보낼때는 `export`를 사용하고 이를 가져다 쓰려면 `import`를 통해 사용할 수 있다.
이처럼 자바스크립트에서는 모듈 시스템을 사용하여 **코드를 조직화**하고 **분리하여** **유지보수성을** 높일 수 있다.