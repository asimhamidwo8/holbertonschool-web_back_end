# ES6 Classes

A Holberton School back-end project covering the fundamentals of ES6 classes in JavaScript.

## Concepts

- Class definitions and constructors
- Getters, setters, and attribute type validation
- Static methods
- Inheritance (`extends` / `super`) and abstract classes
- Symbols: `Symbol.toStringTag`, `Symbol.toPrimitive`, `Symbol.species`
- Hoisting and class definition order

## Files

| File | Description |
|------|-------------|
| `0-classroom.js` | `ClassRoom` class |
| `1-make_classrooms.js` | `initializeRooms` function returning 3 classrooms |
| `2-hbtn_course.js` | `HolbertonCourse` class with getters/setters and type checks |
| `3-currency.js` | `Currency` class |
| `4-pricing.js` | `Pricing` class with a static `convertPrice` method |
| `5-building.js` | Abstract `Building` class |
| `6-sky_high.js` | `SkyHighBuilding` class extending `Building` |
| `7-airport.js` | `Airport` class using `Symbol.toStringTag` |
| `8-hbtn_class.js` | `HolbertonClass` using `Symbol.toPrimitive` |
| `9-hoisting.js` | Fixed hoisting issues |
| `10-car.js` | `Car` class with `cloneCar` using `Symbol.species` |

## Usage

```bash
npm install
npm run dev 0-main.js
```

## Requirements

- Ubuntu 24.04
- Node.js
- Babel (`@babel/core`, `@babel/node`, `@babel/preset-env`)
