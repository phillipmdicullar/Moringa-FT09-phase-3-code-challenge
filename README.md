# Magazine Domain - Code Challenge
### Overview
This repository contains a solution for a Code Challenge focused on a Magazine Domain. The system models three key entities: Author, Article, and Magazine. The relationships between these models follow these rules:

An Author has many Articles.
A Magazine has many Articles.
Articles belong to both an Author and a Magazine.
The Author and Magazine models have a many-to-many relationship.

This challenge includes the design, implementation, and testing of CRUD operations for these models, as well as methods to handle complex relationships using SQL.

## Features
- Author Model: Handles the initialization of authors and their related articles.
- Magazine Model: Manages magazine details, including the category and relationships with authors and articles.
- Article Model: Represents articles, linking them to both an author and a magazine.
- Database: A fully functional database for storing author, magazine, and article information, with relationships between them.
### Setup Instructions
Clone the repository:

bash
Copy code
`git clone <repository-url>`
Install the required dependencies using pipenv:

bash
Copy code
`pipenv install`
Enter the pipenv shell:

bash
Copy code
`pipenv shell`
Run the application to set up the database:

bash
Copy code
`python3 app.py`
File Structure
plaintext
Copy code
`├── /app.py`                # Main application file to test and create database
`├── /database`              # Contains database setup and connection files
`│   ├── setup.py`           # Queries to create the database tables
`│   └── connection.py`      # Database connection string
`├── /models`                # Model files (Author, Article, Magazine)
`│   ├── Author.py`          # Author model with CRUD methods
`│   ├── Article.py `        # Article model with CRUD methods
`│   └── Magazine.py`        # Magazine model with CRUD methods
`└── /tests`                 # Test files for verifying the functionality
`    └── tests.py`           # Provided test cases to guide implementation

### Core Deliverables
#### Author Model
`Initialization (__init__)`: Initialize an author with a name.
ID Property: Returns the ID of the author (Primary Key from the database).
Name Property: Returns and manages the author's name (cannot be changed after instantiation).
Magazine Model
`Initialization (__init__)`: Initialize a magazine with a name and category.
`ID Property`: Returns the ID of the magazine.
`Name Property`: Returns and manages the magazine's name (can be changed after instantiation).
`Category Property`: Returns and manages the magazine's category (can be changed after instantiation).
Article Model
`Initialization (__init__)`: Initialize an article with a title, and links to both an author and a magazine.
`Title Property`: Returns the article's title (cannot be changed after instantiation).
`Author Property`: Returns the author of the article.
`Magazine Property`: Returns the magazine of the article.
## Methods for Relationships
#### Article Model:

`author`: Returns the author of the article.
`magazine`: Returns the magazine of the article.
Author Model:

`articles()`: Returns all articles written by the author.
`magazines()`: Returns all magazines associated with the author.
Magazine Model:

`articles()`: Returns all articles published in the magazine.
`contributors()`: Returns all authors who have contributed to the magazine.
Advanced Methods
Magazine Model:
`article_titles()`: Returns a list of article titles for a given magazine.
`contributing_authors()`: Returns a list of authors who have written more than 2 articles for the magazine.
Testing
To ensure the functionality of your code, test cases have been provided in the /tests folder. As you work on implementing methods, run these tests to verify your progress and ensure that your code works as expected.

Example Usage
python
Copy code
### Create Author
`author1 = Author("John Doe")`

### Create Magazine
`magazine1 = Magazine("Tech Monthly", "Technology")`

### Create Article
`article1 = Article(author1, magazine1, "The Future of the world")`

#### Get Author's Articles
`author_articles = author1.articles()`

### Get Magazine's Contributors
`magazine_contributors = magazine1.contributors()`

### Print Titles of Articles in a Magazine
`article_titles = magazine1.article_titles()`
### Conclusion
This repository represents a comprehensive solution for managing the relationships between authors, articles, and magazines. By implementing the required methods and testing your code, you will gain valuable experience working with databases, object-oriented programming, and SQL joins.

Happy coding! 😄





