# Node.js Basics

A set of exercises to learn the basics of Node.js: running JavaScript with Node, reading user input, reading files synchronously and asynchronously, and building HTTP servers with the `http` module and Express.

## Requirements

- Node.js 12.x or later
- npm
- Ubuntu 20.04 LTS (or WSL)
- Code follows the ESLint Airbnb style

## Installation

```bash
npm install
```

## Database

The tasks use `database.csv`, a list of students with the columns:

```
firstname,lastname,age,field
```

## Tasks

| # | File | Description |
|---|------|-------------|
| 0 | `0-console.js` | `displayMessage` prints a string to STDOUT. |
| 1 | `1-stdin.js` | Asks for the user's name with `process.stdin` and prints it. |
| 2 | `2-read_file.js` | `countStudents` reads the database synchronously and logs the number of students per field. |
| 3 | `3-read_file_async.js` | Same as task 2, but reads the database asynchronously and returns a Promise. |
| 4 | `4-http.js` | Small HTTP server with the `http` module on port 1245. |
| 5 | `5-http.js` | HTTP server with `/` and `/students` routes, using the database passed as argument. |
| 6 | `6-http_express.js` | Small HTTP server with Express on port 1245. |
| 7 | `7-http_express.js` | Express server with `/` and `/students` routes. |
| 8 | `full_server/` | Organized Express server with controllers, routes, and a utility function. |

## Full server structure

```
full_server/
├── controllers/
│   ├── AppController.js       # GET /
│   └── StudentsController.js  # GET /students and /students/:major
├── routes/
│   └── index.js               # Links routes to controllers
├── utils.js                   # readDatabase: reads the CSV and groups students by field
└── server.js                  # Express app on port 1245
```

## Usage

```bash
# Task 2
node 2-main_1.js

# Task 5 / 7
node 5-http.js database.csv
curl localhost:1245/students

# Task 8
npm run dev
curl localhost:1245
curl localhost:1245/students
curl localhost:1245/students/SWE
```

## Example output

```
This is the list of our students
Number of students in CS: 6. List: Johann, Arielle, Jonathan, Emmanuel, Guillaume, Katie
Number of students in SWE: 4. List: Guillaume, Joseph, Paul, Tommy
```

## Author

Asim Hamid
