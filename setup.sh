#!/bin/bash
set -e

echo "🚀Starting setup for Secure Task Manager project..."

# Create root folder
mkdir -p secure-task-manager
cd secure-task-manager

##########################################
# Backend Setup
##########################################
echo "Setting up backend..."
mkdir -p backend/src/routes backend/src/models
cd backend

# Ensure Node.js and npm are installed
if ! command -v npm &> /dev/null
then
    echo "npm could not be found. Please install Node.js and npm before running this script."
    echo "Visit https://nodejs.org/ for installation instructions."
    exit 1
fi

# Initialize Node.js project
npm init -y

# Install dependencies
npm install express cors dotenv pg bcryptjs jsonwebtoken
npm install --save-dev nodemon

# Create env file
cat <<EOL > .env
DATABASE_URL=postgres://user:password@localhost:5432/securetaskdb
JWT_SECRET=supersecretkey
EOL

# Create index.js
cat <<EOL > src/index.js
import express from 'express';
import cors from 'cors';
import dotenv from 'dotenv';

dotenv.config();

const app = express();
app.use(cors());
app.use(express.json());

app.get('/', (req, res) => {
    res.send("Secure Task Manager Backend is running");
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
    console.log(\`Server is listening on port \${PORT}\`);
});
EOL

# Create database.js
cat <<EOL > src/database.js
import pkg from 'pg';
import dotenv from 'dotenv';
dotenv.config();

const { Pool } = pkg;

const pool = new Pool({
    connectionString: process.env.DATABASE_URL,
});

export default pool;
EOL

cd ..

##########################################
# Frontend Setup
##########################################
echo "Setting up frontend..."
mkdir -p frontend
cd frontend

# Create React project with Vite
npm create vite@latest . -- --template react

# Install extra dependencies
npm install axios react-router-dom

# Create env file
cat <<EOL > .env
VITE_API_URL=http://localhost:5000
EOL

# Overwriter App.jsx with starter
cat <<'EOL' > src/App.jsx
import { BrowserRouter, Routes, Route } from 'react-router-dom';

function Login() {
    return <h1>Login Page</h1>;
}
function Register() {
    return <h1>Register Page</h1>;
}
function Dashboard() {
    return <h1>Dashboard</h1>;
}

function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Login />} />
                <Route path="/register" element={<Register />} />
                <Route path="/dashboard" element={<Dashboard />} />
            </Routes>
        </BrowserRouter>
    );
}

export default App;
EOL

cd ../..

echo "✅Setup complete!!"
echo "Next steps:"
echo "1. cd secure-task-manager/backend && npm run dev   # Start backend server"
echo "2. cd secure-task-manager/frontend && npm run dev  # Start frontend server"
