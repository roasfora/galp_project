# Use the correct Astro runtime version
FROM quay.io/astronomer/astro-runtime:7.3.0

# Switch to root user to install dependencies
USER root

# Install PostgreSQL dependencies
RUN apt-get update && apt-get install -y libpq-dev

# Upgrade pip and install required Python dependencies
RUN pip install --upgrade pip && pip install dbt-postgres psycopg2-binary

# Switch back to non-root user
USER astro
