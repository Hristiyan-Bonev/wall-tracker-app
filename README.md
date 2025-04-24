
# Wall Tracker App

This Django application tracks the progress of wall construction profiles and their respective sections. It includes a REST API to manage construction data and a system to calculate the cost and resources required.

## How to Setup and Run the App

### 1. **Flush Database**

To ensure the database is clean and empty before loading new profiles, run the following command:

```bash
python manage.py flush
```

This will delete all data from your database. Confirm when prompted.

### 2. **Load Profiles**

You must provide an `input_profiles.txt` file to load data into the app. The file should be structured as follows:

```
10 15 20
5 10 15
30 25
```

Where:
- Each line represents a new profile.
- Each number on a line represents the initial height of a wall section within that profile.

Once the `input_profiles.txt` file is prepared, run:

```bash
python manage.py load_profiles
```

IMPORTANT: You have to run `python manage.py migrate` prior to executing `load_profiles`, because this will create the required tables.


This will load the profiles and sections from the file into the database.

### 3. **Run the App**

To start the Django development server, run:

```bash
python manage.py runserver
```

You can now access the application at `http://localhost:8000`.

---

## Docker Setup

### 1. **Build the Docker Image**

To build the Docker image for the app, run:

```bash
docker build -t wall-tracker-app .
```

This will build the image using the provided `Dockerfile`.

### 2. **Run the Docker Container**

Once the image is built, run the container with the following command:

```bash
docker run -p 8000:8000 wall-tracker-app
```

The app will be available at `http://localhost:8000` inside your Docker container.

---

## Admin Panel

### 1. **Create a Superuser**

To create an admin user, run:

```bash
python manage.py createsuperuser
```

You will be prompted to enter a username, email, and password.

### 2. **Access the Admin Panel**

Once the superuser is created, you can access the Django admin panel by visiting:

```
http://localhost:8000/admin
```

Log in with the superuser credentials you just created.

---

## Notes on `input_profiles.txt`

The `input_profiles.txt` file is essential for loading wall profile data into the application. Each line of the file represents a new **wall profile**. Each number in a line corresponds to a **section** of the wall profile, with the number indicating the **initial height** of the section.

- For example, the line:
  ```
  10 15 20
  ```
  Means Profile 1 contains three sections with initial heights of 10, 15, and 20.

- The height can range from 0 to 30. A section with a height less than 30 will be considered **incomplete** and needs more work to reach the maximum height.
  
- The system will calculate the **cost** and **ice** required for each section based on its initial height and the work remaining.

---
## Endpoints and Example Responses

### 1. **GET /profiles/1/days/1/**

Returns the ice amount used on day 1 for the given profile.

**Example Response:**
```json
{
  "day": "1",
  "ice_amount": "585"
}
```

### 2. **GET /profiles/1/overview/1/**

Returns the cost for the given profile on day 1.

**Example Response:**
```json
{
  "day": "1",
  "cost": "1,111,500"
}
```

### 3. **GET /profiles/overview/1/**

Returns the total cost of all profiles for day 1.

**Example Response:**
```json
{
  "day": "1",
  "cost": "3,334,500"
}
```

### 4. **GET /profiles/overview/**

Returns the total cost of all profiles, regardless of the day.

**Example Response:**
```json
{
  "day": null,
  "cost": "32,233,500"
}
```

---
