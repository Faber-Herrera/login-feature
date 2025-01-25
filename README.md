# Login Feature

A secure authentication system built with FastAPI and React.

## Features

- User authentication with JWT
- Secure password hashing
- MongoDB integration
- React frontend with Material-UI
- Docker containerization
- Rate limiting
- Protected routes

## Tech Stack

### Backend

- FastAPI
- MongoDB
- Motor (async MongoDB driver)
- PyJWT
- Bcrypt

### Frontend

- React
- TypeScript
- Material-UI
- Formik
- Axios

## Getting Started

### Prerequisites

- Docker and Docker Compose
- Node.js 18+ (for local development)
- Python 3.11+ (for local development)

### Quick Start

1. Clone the repository

```bash
git clone <repository-url>
cd login-feature
```

2. Start with Docker

```bash
docker compose up -d
```

3. Create test user

```bash
curl http://localhost:8000/api/auth/test-user
```

### Access the application

- Frontend: http://localhost:5173
- Backend API: http://localhost:8000
- API Documentation: http://localhost:8000/docs

### Test credentials

- Email: test@example.com
- Password: password123

## Local Development

### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

## Project Structure

```
login-feature/
├── backend/
│   ├── app/
│   │   ├── config/      # Database and app configuration
│   │   ├── models/      # Data models
│   │   ├── routes/      # API endpoints
│   │   ├── services/    # Business logic
│   │   └── utils/       # Helper functions
│   ├── tests/           # Test files
│   └── main.py         # Application entry point
├── frontend/
│   ├── src/
│   │   ├── components/  # React components
│   │   ├── contexts/    # React contexts
│   │   ├── services/    # API services
│   │   └── utils/       # Helper functions
│   └── index.html      # Entry HTML file
└── docker-compose.yml  # Docker configuration
```

## API Documentation

### Authentication Endpoints

#### Register User

```http
POST /api/auth/register
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "password123",
  "name": "John Doe"
}
```

#### Login

```http
POST /api/auth/login
Content-Type: application/x-www-form-urlencoded

username=user@example.com&password=password123
```

#### Get Current User

```http
GET /api/auth/me
Authorization: Bearer <token>
```

## Environment Variables

### Backend (.env)

```plaintext
MONGODB_URL=mongodb://mongodb:27017
DATABASE_NAME=login_feature_db
SECRET_KEY=your-secret-key
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### Frontend (.env)

```plaintext
VITE_API_URL=http://localhost:8000/api
```

## Docker Images

Images are available on Docker Hub:

```bash
docker pull faberherrera/login-feature-frontend:latest
docker pull faberherrera/login-feature-backend:latest
```

## Testing

### Running Backend Tests

```bash
cd backend
pytest
```

### Running Frontend Tests

```bash
cd frontend
npm test
```

## Security Features

- JWT-based authentication
- Password hashing with bcrypt
- Rate limiting for API endpoints
- CORS protection
- Environment variable configuration
- MongoDB security best practices
- Error handling
- Input validation

## Troubleshooting

### Common Issues

#### MongoDB Connection Issues

```bash
# Check MongoDB logs
docker logs login-feature-mongodb
```

#### Frontend API Connection

- Verify API URL in frontend .env file
- Check CORS settings in backend

#### JWT Token Issues

- Ensure SECRET_KEY is properly set
- Check token expiration time

#### Docker Issues

```bash
# Reset containers
docker compose down -v
docker compose up --build
```

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Faber Herrera

## Acknowledgments

- FastAPI documentation
- React documentation
- MongoDB documentation
- Material-UI components
