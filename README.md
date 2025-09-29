# API Payment Process - Test Automation Suite

Dockerized test suite for the Grow Payments API endpoint assignment that enforces proper HTTP status codes and API best practices.

## Current Status

**CI Pipeline will FAIL until developers will adopt proper HTTP status codes:**
- Validation errors currently return HTTP 200 (incorrect)
- Tests expect HTTP 422 for validation errors (correct standard)
- This enforces better API practices from the development team

## Quick Start

**Prerequisites:** [Docker](https://www.docker.com/get-started)

```bash
# Setup
touch .env
# Edit .env with your credentials

# Run Tests
docker build -t api-tests .
docker run --env-file .env api-tests
```

## Test Coverage

### Happy Path
- Successful payment creation

### Validation Tests (2 tests - Currently FAIL by design)
- **Invalid Email:** Expects HTTP 422, gets HTTP 200
- **Negative Sum:** Expects HTTP 422, gets HTTP 200


## CI/CD Pipeline

The CI pipeline is defined in `.github/workflows/run_tests.yml`:

This pipeline automatically builds the Docker image for the API tests and runs them on every pull request to the main branch, using environment variables for configuration. It checks out the code, builds the test image, and executes the tests inside a Docker container to ensure API compliance before merging changes.

Note: It could also be called for manual developer testing.

## 📋 Environment Variables


`API_URL` - API endpoint 
`PAGE_CODE` - Your page code 
`USER_ID` - Your user ID

## Why Tests Fail (By Design)

Our tests enforce REST API standards:
- HTTP 422: Validation errors (what we expect)
- HTTP 200: Success only (industry standard)

**Current Behavior (Poor Practice):**
```json
HTTP 200 + {"status": "0", "err": {...}}
```

**Expected Behavior (Best Practice):**
```json
HTTP 422 + {"error": "Invalid email format"}
```

---

**These tests serve as quality gatekeepers, ensuring API standards compliance.**