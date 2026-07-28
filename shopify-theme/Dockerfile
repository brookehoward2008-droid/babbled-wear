FROM node:20-alpine

WORKDIR /app

# Install Shopify CLI and theme tools
RUN npm install -g @shopify/cli@latest

# Copy theme files
COPY . .

# Install any additional dependencies (if needed for build tools)
RUN npm install --omit=dev 2>/dev/null || true

EXPOSE 9292

CMD ["shopify", "theme", "dev"]
