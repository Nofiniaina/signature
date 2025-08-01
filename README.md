# Digital Signature Django Project

A Django-based application for digital signature functionality related to cybersecurity and cryptography.

## Project Structure

This is a Django project focused on digital signatures, part of a cybersecurity and cryptography curriculum.

## Setup

### Prerequisites

- Python 3.x
- pipenv (for dependency management)

### Installation

1. Clone the repository
2. Install dependencies using pipenv:
   ```bash
   pipenv install
   ```
3. Activate the virtual environment:
   ```bash
   pipenv shell
   ```
4. Create the required directories and files:
   ```bash
   mkdir -p project_data
   mkdir -p json_data
   echo '{}' > json_data/registration.json
   ```
5. Run migrations:
   ```bash
   python manage.py migrate
   ```
6. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Dependencies

This project uses pipenv for dependency management. The dependencies are defined in the `Pipfile` and locked in `Pipfile.lock`.

## Contributing

This project is part of an academic curriculum at ITU (Istanbul Technical University) for the Cybersecurity Master's program.

## License

Academic project - please refer to university guidelines for usage and distribution.
