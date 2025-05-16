# Use official nginx image
FROM nginx:alpine

# Remove default nginx website content (optional)
RUN rm -rf /usr/share/nginx/html/*

# Copy your static frontend files to nginx html folder
COPY *.html /usr/share/nginx/html

COPY *.jpg /usr/share/nginx/html

# Expose port 80 (already exposed in base image but good to be explicit)
EXPOSE 80

# Start nginx in foreground
CMD ["nginx", "-g", "daemon off;"]
