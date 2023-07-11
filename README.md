# FakeCSV

FakeCSV is a Django application that allows users to create custom data schemas with various column types and generate fake data based on those schemas. Users can log in to the app, create new schemas with customizable options, and build the data schema with any number of columns of any type. The app provides five pages for user interaction, including login, data schemas, new schema creation, data set display, and schema editing.

## Features

- User Authentication: Users can log in to the app.
- Schema Management: Users can create, edit, and delete data schemas.
- Column Management: Users can add, edit, and delete columns in a schema.
- Customizable Options: Users can specify the name, column separator, and string character for each schema.
- Column Types: Users can choose from various column types such as 'Full name', 'Job', 'Email', 'Integer', and 'Date'.
- Data Generation: Users can generate fake data based on their defined schemas.
- Data Download: Users can download the generated data as a CSV file.

## Pages

### Login

- URL: `/login/`
- Description: Allows users to log in to the application.

### Data Schemas

- URL: `/data-schemas`
- Description: Displays a list of all the data schemas created by the user.
- Actions:
  - Create a New Schema: Users can click on the "New Schema" button to create a new schema.
  - Go to Data sets: Users can go to data sets of an already created scheme.
  - Delete Schema: Users can delete an already created scheme.

### New Schema

- URL: `/data-schemas/new-schema`
- Description: Allows users to create a new data schema.
- Fields:
  - Name: Name of the schema.
  - Column Separator: Separator character for the columns (',' or ';').
  - String Character: Character to enclose string values ('"' or "'").
- Actions:
  - Add a New Column: Users can click on the "Add Column" button to add a new column to the schema.
  - Save the Schema: Users can click on the "Submit" button to save the schema.

### Data Sets

- URL: `/data-sets/<str:name>/`
- Description: Displays the generated data for a specific schema.
- Actions:
  - Edit Schema: Users can edit chosen schema when click on "Edit schema" link.
  - Generate Data: Users can enter the number of rows to generate and click on the "Generate data" button to generate data.
  - Download Data: Users can click on the "Download" button to download the generated data as a CSV file.

### Edit Schema

- URL: `/edit-schema/<str:name>/`
- Description: Allows users to edit an existing schema.
- Actions:
  - Edit Schema Details: Users can modify the schema name, column separator, or string character and click on the "Submit" button to save the changes.
  - Edit Columns: Users can modify the column details (name, type, etc.) and click on the "Submit" button to save the changes.
  - Delete Columns: Users can click on the "Delete" button to delete the column.

## Installation

1. Clone the repository:
```shell
git clone https://github.com/your-username/FakeCSV.git
```
2. Activate the virtual environment:
```shell
pipenv shell
```
3. Navigate to the project directory:
```shell
cd FakeCSV
```
4. Install the dependencies:
```shell
pipenv install
```
5. Apply database migrations:
```shell
python manage.py migrate
```
6. Start the development server:
```shell
python manage.py runserver
```
7. Open your web browser and visit http://localhost:8000 to access the application.

## Contributing
Contributions are welcome! If you find any bugs or have suggestions for new features, please open an issue on the [GitHub repository](https://github.com/Kalinka5/FakeCSV). If you would like to contribute code, feel free to open a pull request.

## License
This project is licensed under the [MIT License](LICENSE).
