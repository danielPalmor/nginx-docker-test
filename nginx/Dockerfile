FROM ubuntu:latest

# Update the packages list, install nginx in the container and clean APT cache
RUN apt-get update && apt-get install -y nginx && rm -rf /var/lib/apt/lists/*

# Copy nginx.conf file into container
COPY nginx.conf /etc/nginx/nginx.conf

# Copy index.html file into container
COPY index.html /etc/nginx/

EXPOSE 8080 8081

# Start nginx and prevent it from running as a daemon (in the background)
CMD ["nginx", "-g", "daemon off;"]
