# FakeCSV
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/faker?style=plastic&color=green)
![PyPI](https://img.shields.io/pypi/v/django?color=orange)
![GitHub](https://img.shields.io/github/license/Kalinka5/FakeCSV?color=blue)


<b>📊 FakeCSV</b> is a <b><i>Django application</i></b> that allows users to create custom <b><i>data schemas</i></b> with various column types and generate <b><i>fake data</i></b> based on those schemas. Users can <b><i>log in</i></b> to the app, <b><i>create new schemas</i></b> with customizable options, and build the data schema with <b><i>any number of columns</i></b> of any type. The app provides five pages for user interaction, <i>including login</i>, <i>data schemas</i>, <i>new schema creation</i>, <i>data set display</i>, and <i>schema editing</i>.

## Features

- <b>🔐 User Authentication</b>: Securely log in to the app. 🔐
- <b>🗄️ Schema Management</b>: <i>Create</i>, <i>edit</i>, and <i>delete</i> data schemas. 🗄️
- <b>📝 Column Management</b>: <i>Add</i>, <i>edit</i>, and <i>delete</i> columns in a schema. 📝
- <b>🎨 Customizable Options</b>: Personalize schemas with custom <i>names</i>, <i>column separators</i>, and <i>string characters</i>. 🎨
- <b>🔢 Column Types</b>: Choose from a variety of column types, including <i>'Full name'</i>, <i>'Job'</i>, <i>'Email'</i>, <i>'Integer'</i>, and <i>'Date'</i>. 🔢
- <b>🔄 Data Generation</b>: Generate realistic <i>fake data</i> based on defined schemas. 🔄
- <b>⬇️ Data Download</b>: Download generated data as a <i>CSV file</i>. ⬇️

## Pages

### Login

- <b>URL</b>: `/login/`
- <b>Description</b>: Allows users to log in to the application.

![image](https://github.com/Kalinka5/FakeCSV/assets/106172806/a382d1a6-b6fd-4779-a267-bccf1d859439)

<hr>

### Data Schemas

- <b>URL</b>: `/data-schemas`
- <b>Description</b>: Displays a table of all the data schemas created by the user.
- <b>Actions</b>:
  - <b>➕ Create a New Schema</b>: Click the "New Schema" button to create a new schema. ➕
  - <b>📚 Access Data Sets</b>: Explore data sets of existing schemas. 📚
  - <b>❌ Delete Schema</b>: Remove an already created schema. ❌

![image](https://github.com/Kalinka5/FakeCSV/assets/106172806/08f291c9-a4fa-41a9-965f-ba70bc127a72)

<hr>

### New Schema

- <b>URL</b>: `/data-schemas/new-schema`
- <b>Description</b>: Allows users to create a new data schema.
- <b>Fields</b>:
  - <b>🖊️ Name</b>: Name of the schema. 🖊️
  - <b>🔀 Column Separator</b>: Separator character for the columns (',' or ';'). 🔀
  - <b>📰 String Character</b>: Character to enclose string values ('"' or "'"). 📰
- <b>Actions</b>:
  - <b>➕ Add a New Column</b>: Users can click on the "Add Column" button to add a new column to the schema. ➕
  - <b>💾 Save the Schema</b>: Users can click on the "Submit" button to save the schema. 💾

![image](https://github.com/Kalinka5/FakeCSV/assets/106172806/a81cf50f-fa0d-4486-a059-94f1cc0f4cc9)

<hr>

### Data Sets
- <b>URL</b>: `/data-sets/<str:name>/`
- <b>Description</b>: Displays the generated data for a specific schema.
- <b>Actions</b>:
  - <b>✏️ Edit Schema</b>: Users can edit the chosen schema by clicking on the "Edit schema" link. ✏️
  - <b>📊 Generate Data</b>: Users can enter the number of rows to generate and click on the "Generate data" button to generate data. 📊
  - <b>⬇️ Download Data</b>: Users can click on the "Download" button to download the generated data as a CSV file. ⬇️

![image](https://github.com/Kalinka5/FakeCSV/assets/106172806/46f69997-2736-4e86-b7fc-ae4e2b1bd0cc)

<hr>

### Edit Schema

- <b>URL</b>: `/edit-schema/<str:name>/`
- <b>Description</b>: Allows users to edit an existing schema.
- <b>Actions</b>:
  - <b>✏️ Edit Schema Details</b>: Users can modify the schema name, column separator, or string character and click on the "Submit" button to save the changes. ✏️
  - <b>✏️ Edit Columns</b>: Users can modify the column details (name, type, etc.) and click on the "Submit" button to save the changes. ✏️
  - <b>❌ Delete Columns</b>: Users can click on the "Delete" button to delete the column. ❌

![image](https://github.com/Kalinka5/FakeCSV/assets/106172806/0c92f710-2081-425c-808f-437946037caf)

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
