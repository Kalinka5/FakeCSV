# FakeCSV
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/faker?style=plastic&color=green)
![PyPI](https://img.shields.io/pypi/v/django?color=orange)
![GitHub](https://img.shields.io/github/license/Kalinka5/FakeCSV?color=blue)


<b>📊 FakeCSV</b> is a <b><i>Django application</i></b> that allows users to create custom <b><i>data schemas</i></b> with various column types and generate <b><i>fake data</i></b> based on those schemas. Users can <b><i>log in</i></b> to the app, <b><i>create new schemas</i></b> with customizable options, and build the data schema with <b><i>any number of columns</i></b> of any type. The app provides twelve pages for user interaction, <i>including login</i>, <i>data schemas</i>, <i>new schema creation</i>, <i>data set display</i>, <i>schema editing</i>, <i>register</i>, <i>home</i>, <i>profile</i>, <i>profile/change_password</i>, <i>profile/delete</i>, and <i>password success</i>.

## Usage
I deployed this Django project in the <a href="https://www.pythonanywhere.com/">PythonAnywhere</a> free service. So you can go and try my site on <a href="https://55kalina55.pythonanywhere.com/">this link</a>.

## Features

- <b>🔐 User Authentication</b>: Securely log in to the app and register page. This app has a Register page where users can register new accounts.
- <b>🗄️ Schema Management</b>: <i>Create</i>, <i>edit</i>, and <i>delete</i> data schemas.
- <b>📝 Column Management</b>: <i>Add</i>, <i>edit</i>, and <i>delete</i> columns in a schema.
- <b>🎨 Customizable Options</b>: Personalize schemas with custom <i>names</i>, <i>column separators</i>, and <i>string characters</i>.
- <b>🔢 Column Types</b>: Choose from a variety of column types, including <i>'Full name'</i>, <i>'Job'</i>, <i>'Email'</i>, <i>'Integer'</i>, and <i>'Date'</i>.
- <b>🔄 Data Generation</b>: Generate realistic <i>fake data</i> based on defined schemas.
- <b>⬇️ Data Download</b>: Download generated data as a <i>CSV file</i>.
- <b>👤 User Profile</b>: Manage and update <i>personal information</i> and preferences through the user profile page. In the Profile page, users can click on a link to change their passwords on another page. Additionally, users can delete their accounts on the /members/profile/delete page. When users successfully change their passwords, they will be redirected to the <i>password success</i> page.

## Pages

### Home

- <b>URL</b>: ``
- <b>Description</b>: Allows users to understand its functionalities and purpose at a glance.

![image](https://github.com/Kalinka5/FakeCSV/assets/106172806/611a0bd9-dd4a-4934-b81e-d8c3cb9c36e6)

<hr>

### Login

- <b>URL</b>: `/members/login/`
- <b>Description</b>: Provides users with a secure and convenient way to access their accounts.

![image](https://github.com/Kalinka5/FakeCSV/assets/106172806/7534ddbb-abb6-4051-9183-95f6a23528e1)

<hr>

### Register

- <b>URL</b>: `/members/register/`
- <b>Description</b>: Provide their personal details, including name, email address, and password.

![image](https://github.com/Kalinka5/FakeCSV/assets/106172806/11ad6a0e-92b5-4311-aa43-8419529963e2)

<hr>

### Data Schemas

- <b>URL</b>: `/data-schemas`
- <b>Description</b>: Displays a table of all the data schemas created by the user.
- <b>Actions</b>:
  - <b>➕ Create a New Schema</b>: Click the "New Schema" button to create a new schema.
  - <b>📚 Access Data Sets</b>: Explore data sets of existing schemas.
  - <b>❌ Delete Schema</b>: Remove an already created schema.

![image](https://github.com/Kalinka5/FakeCSV/assets/106172806/d07c1eda-e68f-4cdb-8e2a-87f4f596c38c)

<hr>

### New Schema

- <b>URL</b>: `/data-schemas/new-schema`
- <b>Description</b>: Allows users to create a new data schema.
- <b>Fields</b>:
  - <b>🖊️ Name</b>: Name of the schema.
  - <b>🔀 Column Separator</b>: Separator character for the columns (',' or ';').
  - <b>📰 String Character</b>: Character to enclose string values ('"' or "'").
- <b>Actions</b>:
  - <b>➕ Add a New Column</b>: Users can click on the "Add Column" button to add a new column to the schema.
  - <b>💾 Save the Schema</b>: Users can click on the "Submit" button to save the schema.

![image](https://github.com/Kalinka5/FakeCSV/assets/106172806/53e1d62f-1881-4ffe-be23-aa035122259a)

<hr>

### Data Sets
- <b>URL</b>: `/data-sets/<str:name>/`
- <b>Description</b>: Displays the generated data for a specific schema.
- <b>Actions</b>:
  - <b>✏️ Edit Schema</b>: Users can edit the chosen schema by clicking on the "Edit schema" link.
  - <b>📊 Generate Data</b>: Users can enter the number of rows to generate and click on the "Generate data" button to generate data.
  - <b>⬇️ Download Data</b>: Users can click on the "Download" button to download the generated data as a CSV file.

![image](https://github.com/Kalinka5/FakeCSV/assets/106172806/e3383094-65a2-403e-9be4-47390c74936f)

<hr>

### Edit Schema

- <b>URL</b>: `/edit-schema/<str:name>/`
- <b>Description</b>: Allows users to edit an existing schema.
- <b>Actions</b>:
  - <b>✏️ Edit Schema Details</b>: Users can modify the schema name, column separator, or string character and click on the "Submit" button to save the changes.
  - <b>✏️ Edit Columns</b>: Users can modify the column details (name, type, etc.) and click on the "Submit" button to save the changes.
  - <b>❌ Delete Columns</b>: Users can click on the "Delete" button to delete the column.

![image](https://github.com/Kalinka5/FakeCSV/assets/106172806/bc5358a3-720d-4d77-8d44-3c4a7cec2375)

<hr>

### Profile

- <b>URL</b>: `/members/profile/`
- <b>Description</b>: The profile web page is a user-centric space for managing personal information and preferences within the platform.

![image](https://github.com/Kalinka5/FakeCSV/assets/106172806/afb0d74d-08bc-48a0-b98e-227a8faca30a)

<hr>

### Change password

- <b>URL</b>: `/members/password/`
- <b>Description</b>: Web page enables users to update their account's password securely for enhanced online security.

![image](https://github.com/Kalinka5/FakeCSV/assets/106172806/cc13d704-45d6-47b9-907f-c7439ee6f1f7)

<hr>

### Delete account

- <b>URL</b>: `/members/profile/delete`
- <b>Description</b>: Allows users to permanently remove their accounts from the system.

![image](https://github.com/Kalinka5/FakeCSV/assets/106172806/92463d0c-472c-4576-9e80-6c8625dcc637)

<hr>

## Installation

1. <b>Clone the repository</b>:
```shell
git clone https://github.com/your-username/FakeCSV.git
```
2. <b>Activate the virtual environment</b>:
```shell
pipenv shell
```
3. <b>Navigate to the project directory</b>:
```shell
cd FakeCSV
```
4. <b>Install the dependencies</b>:
```shell
pipenv install
```
5. <b>Apply database migrations</b>:
```shell
python manage.py migrate
```
6. <b>Start the development server</b>:
```shell
python manage.py runserver
```
7. <b>Open your web browser</b> and visit <b>http://localhost:8000</b> to access the application.

## Contributing
Contributions are welcome! If you find any bugs or have suggestions for new features, please open an issue on the [<b>GitHub repository</b>](https://github.com/Kalinka5/FakeCSV). If you would like to contribute code, feel free to open a pull request.

## License
This project is licensed under the [<b>MIT License</b>](LICENSE).

Feel free to reach out if you have any questions or need further assistance. Enjoy using FakeCSV!👩‍💻🚀
