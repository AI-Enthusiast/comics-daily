# Use the official lightweight Python image based on Alpine Linux
FROM python

# Set the working directory
WORKDIR /docker_testcontainer

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Display all scraper.py files and their contents during build
RUN find /docker_testcontainer/src -name "scraper.py" -exec sh -c 'echo "=== {} ===" && cat {}' \;

# Run all scraper.py files to ensure they work correctly
RUN find /docker_testcontainer/src -name "scraper.py" -exec python {} \;

# Run the update_readme script to generate/update the README
RUN python /docker_testcontainer/src/update_readme.py

# Command to run the application
CMD ["python"]
