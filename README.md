# Shopping Genie

## Installation

### Back-End
The back-End has been tested on python 3.6.8. Please follow the link for instaltion.
```
https://www.python.org/downloads/release/python-365/
```

Please run the following command in the back-end folder
```sh
pip install -r requirements.txt
```

### Front-End
1. Please install npm that will come with node.js
2. Please install react using the following command
```sh
npm install --save react
npm install --save react-dom
npm install
```

## Running

This project is composed of a react app and a flask back-end. The flask back-end has `/api/*` endpoints, but everything outside of `/api` will serve the react app.

To run this project, follow these steps:

### Buidling the React app

To build the react app, use the following commands:

```sh
cd front-end
npm run build # Use npm run build when shipping to production
```

This command will run webpack on the JavaScript files and generate the minified files and put them in `/back-end/static/`, as well as generate the `index.html` inside `/back-end/templates/index.html`.
*NOTE: This step is neessary before running the server*

---

### Running Flask

To run the Flask server, use the following commands:

```sh
cd back-end
python json_io.py
```

This will boot the server on port 5000 so you can access it on http://127.0.0.1:5000.
