# Use official Node image
FROM node:18-alpine

WORKDIR /app

# Copy package files and install deps first (for Docker cache)
COPY package*.json ./
RUN npm install

# Copy app code
COPY . .

# Expose port and run React
EXPOSE 3000
CMD ["npm", "start"]
