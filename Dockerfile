# Use the official lightweight Python image based on Alpine Linux
FROM python

# Set the working directory
WORKDIR /docker_testcontainer

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Command to run all scrapers and then update the README
CMD ["sh", "-c", "echo 'Running all scraper.py files...' && find /docker_testcontainer/src -name 'scraper.py' -exec python {} \\; && echo 'All scrapers completed. Updating README...' && python /docker_testcontainer/src/update_readme.py && echo 'README updated successfully!'"]
