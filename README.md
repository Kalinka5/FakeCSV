# FakeCSV

<b>📊 FakeCSV</b> is a Django application that allows users to create custom data schemas with various column types and generate fake data based on those schemas. Users can log in to the app, create new schemas with customizable options, and build the data schema with any number of columns of any type. The app provides five pages for user interaction, including login, data schemas, new schema creation, data set display, and schema editing.

## Features

- <b>🔐 User Authentication</b>: Users can log in to the app.
- <b>🗄️ Schema Management</b>: Users can create, edit, and delete data schemas.
- <b>📝 Column Management</b>: Users can add, edit, and delete columns in a schema.
- <b>🎨 Customizable Options</b>: Users can specify the name, column separator, and string character for each schema.
- <b>🔢 Column Types</b>: Users can choose from various column types such as 'Full name', 'Job', 'Email', 'Integer', and 'Date'.
- <b>🔄 Data Generation</b>: Users can generate fake data based on their defined schemas.
- <b>⬇️ Data Download</b>: Users can download the generated data as a CSV file.

## Pages

### Login

- <b>URL</b>: `/login/`
- <b>Description</b>: Allows users to log in to the application.

### Data Schemas

- <b>URL</b>: `/data-schemas`
- <b>Description</b>: Displays a list of all the data schemas created by the user.
- <b>Actions</b>:
  - <b>➕ Create a New Schema</b>: Users can click on the "New Schema" button to create a new schema.
  - <b>📚 Go to Data sets</b>: Users can go to data sets of an already created scheme.
  - <b>❌ Delete Schema</b>: Users can delete an already created scheme.

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

### Data Sets

- <b>URL</b>: `/data-sets/<str:name>/`
- <b>Description</b>: Displays the generated data for a specific schema.
- <b>Actions</b>:
  - <b>✏️ Edit Schema</b>: Users can edit the chosen schema by clicking on the "Edit schema" link.
  - <b>📊 Generate Data</b>: Users can enter the number of rows to generate and click on the "Generate data" button to generate data.
  - <b>⬇️ Download Data</b>: Users can click on the "Download" button to download the generated data as a CSV file.

### Edit Schema

- <b>URL</b>: `/edit-schema/<str:name>/`
- <b>Description</b>: Allows users to edit an existing schema.
- <b>Actions</b>:
  - <b>✏️ Edit Schema Details</b>: Users can modify the schema name, column separator, or string character and click on the "Submit" button to save the changes.
  - <b>✏️ Edit Columns</b>: Users can modify the column details (name, type, etc.) and click on the "Submit" button to save the changes.
  - <b>❌ Delete Columns</b>: Users can click on the "Delete" button to delete the column.

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
