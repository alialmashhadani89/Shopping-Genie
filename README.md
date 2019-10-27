# Shopping Genie

## Installation

TODO: Add installation instructions

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
