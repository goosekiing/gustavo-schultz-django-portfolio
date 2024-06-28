# Personal Portfolio Website

A personal webpage created using Django and Bootstrap technologies, featuring a portfolio section displayed in cards that redirect to a detailed project page when clicked. A responsive and dynamic website where all presented content is controlled by the Django admin. SQL data is configured to be stored in CockroachDB, and static and media files are stored in an AWS S3 bucket.

## Table of Contents

- [Features](#features)
- [Technologies Used and Prerequisites](#technologies-used-and-prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Contribution](#contribution)
- [License](#license)
- [Contact](#contact)

## Features

- **Index**: Section dedicated to a brief introduction and an infinite carousel loaded with images via admin. For personal use, the carousel displays logos of the technologies used.
- **About**: Section containing a personal image and space for a more detailed description. Data loaded and editable via admin.
- **Portfolio**: Displays projects in a card format with an image, title, and tag. Projects can be filtered by tags. The entire card is a link that redirects to the project page when clicked.
- **Project**: Accessed after clicking on a card. Displays project images in a carousel, title, description, and, if available, a link to GitHub. Projects are added via admin.
- **Contact**: Displays buttons with links that can redirect to WhatsApp, GitHub, LinkedIn, and email. Only buttons with filled data in the admin are displayed.

## Technologies Used and Prerequisites

- **Python**: 3.11.9
- **Django**: 4.1.13
- **Bootstrap**: 5.3
- **boto3**: 1.34.114
- **django-cockroachdb**: 4.1.1
- **django-storages**: 1.14.3
- **gunicorn**: 22.0.0
- **pillow**: 10.3.0
- **psycopg2**: 2.9.9

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/goosekiing/personal-portfolio-website.git
    cd personal-portfolio-website
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

Set the following environment variables:

- `DJANGO_SECRET_KEY`
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_STORAGE_BUCKET_NAME`
- `COCKROACHLABS_DB_PASSWORD`
- `DATABASE_URL`

Example configuration in the `.env` file:
```plaintext
DJANGO_SECRET_KEY='your-secret-key'
AWS_ACCESS_KEY_ID='your-access-key-id'
AWS_SECRET_ACCESS_KEY='your-secret-access-key'
AWS_STORAGE_BUCKET_NAME='your-bucket-name'
COCKROACHLABS_DB_PASSWORD='your-database-password'
DATABASE_URL='your-database-url'
```

## Usage

To make the project work as in the code, you need to have an AWS account and create an S3 bucket to store static and media files. AWS offers a 12-month free tier for new users. For the database, you need a Cockroach Labs account ([https://www.cockroachlabs.com/](https://www.cockroachlabs.com/)) to host the data. Cockroach Labs also offers a free plan that is sufficient to store the data of a small personal project like this. It is possible to change the settings to use other storage providers.

1. Apply database migrations:
    ```bash
    python manage.py migrate
    ```

2. Collect static files:
    ```bash
    python manage.py collectstatic
    ```

3. Start the development server:
    ```bash
    python manage.py runserver
    ```

4. Open your browser and access `http://localhost:8000`

## Contribution

I am not looking for contributions to this project at the moment.

## License

This project is Open Source and does not have a specific license.

## Contact

- GitHub: [goosekiing](https://github.com/goosekiing)
- LinkedIn: [Gustavo Schultz](https://linkedin.com/in/gustavosschultz/)
