# Flask RestAPI

- **Description**: Flask RestAPI is a RESTful web application built using Flask, a lightweight Python web framework. It provides a user-friendly interface to perform CRUD operations on user data stored in a database. The application follows the Model-View-Controller (MVC) architectural pattern, separating concerns and enhancing maintainability.


- **Features**:
  - RESTful API for managing user data
  - MVC architecture for improved organization
  - Routes for CRUD operations on users
  - Responsive HTML page for route information display

- **File Structure** 
```
flask_restapi/
│
├── app.py
├── controller/
│ └── userController.py
├── model/
│ └── userModel.py
└── view/
└── index.html
```

- **Installation**:
  1. Clone the repository:
     ```bash
     git clone https://github.com/MaliDipak/Flask-RestAPI
     ```
  2. Navigate to the project directory:
     ```bash
     cd Flask-RestAPI
     ```
  3. Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```

- **Usage**:
  1. Run the Flask application:
     ```bash
     python app.py
     ```
  2. Access the application in your web browser at `http://localhost:5000/`.
  3. Use the provided routes to perform CRUD operations on user data.

- **Routes**:
  - **GET /:** Home page route. Displays information about all routes in the application.
  - **GET /routes:** Endpoint to fetch information about all routes in the application.
  - **GET /user/getall:** Retrieves all users from the database.
  - **GET /user/getone:** Retrieves one random user from the database.
  - **GET /user/getone/&lt;id&gt;:** Retrieves a user by their ID from the database.
  - **POST /user/add:** Adds a new user to the database.
  - **PUT /user/update:** Updates an existing user in the database.
  - **PATCH /user/updatepatch:** Updates an specific user information in the database.
  - **DELETE /user/delete/&lt;id&gt;:** Deletes a user from the database by their ID.
  - **DELETE /user/deleteall:** Deletes all users from the database.




