# FIXES.md

Document every issue you find and fix in this file.

---

## Fix 1: Incorrect service hostname in service-b

**What was wrong:**
service-b was using `http://localhost:5000` to connect to service-a.

**Why it is a problem:**
Inside Docker, localhost refers to the container itself, not other services.

**How I fixed it:**
Changed the URL to `http://service-a:5000`.

**What could go wrong if left unfixed:**
service-b would fail to connect and continuously error while polling.

---

## Fix 2: Service startup dependency not handled correctly

**What was wrong:**
service-b depended on service-a using `depends_on`, but this does not ensure service readiness.

**Why it is a problem:**
service-b could start before service-a is ready, causing connection failures.

**How I fixed it:**
Added a Docker healthcheck to service-a and updated depends_on to use `condition: service_healthy`.

**What could go wrong if left unfixed:**
Intermittent failures during startup and unreliable system behavior.

---

## Fix 3: Missing curl for healthcheck

**What was wrong:**
The service-a container did not include curl, which is required for the healthcheck.

**Why it is a problem:**
The healthcheck command would fail, marking the container as unhealthy.

**How I fixed it:**
Installed curl in the Dockerfile.

**What could go wrong if left unfixed:**
service-b would never detect service-a as healthy and may fail to start.


## Fix 4: Obsolete docker-compose version field

**What was wrong:**
The docker-compose file used a deprecated `version` field.

**Why it is a problem:**
It generates warnings and may cause confusion with newer Docker Compose versions.

**How I fixed it:**
Removed the `version` field.

**What could go wrong if left unfixed:**
Future compatibility issues or misleading configuration behavior.


## Fix 5: Using Flask development server in production

**What was wrong:**
The application used Flask’s built-in development server.

**Why it is a problem:**
It is not designed for production and cannot handle concurrent requests efficiently.

**How I fixed it:**
Replaced it with a production-grade WSGI server (gunicorn).

**What could go wrong if left unfixed:**
Poor performance and instability under load.

## Fix 6: Hardcoded AWS credentials in Terraform

**What was wrong:**
AWS access keys and secret keys were hardcoded in the Terraform configuration.

**Why it is a problem:**
This is a major security risk and can lead to unauthorized access and credential leakage.

**How I fixed it:**
Removed hardcoded credentials and used environment variables / AWS CLI configuration.

**What could go wrong if left unfixed:**
Credential compromise, unauthorized resource usage, and security breaches.

## Fix 7: Missing resource tagging in Terraform

**What was wrong:**
The EC2 instance did not have any tags defined.

**Why it is a problem:**
Makes resource management, cost tracking, and ownership identification difficult.

**How I fixed it:**
Added meaningful tags such as Name, Environment, and Owner.

**What could go wrong if left unfixed:**
Operational confusion and difficulty managing infrastructure at scale.

## Self-initiated Improvements

## Improvement 1: Use production-ready WSGI server

**What I improved:**
Replaced Flask development server with a production-grade WSGI server (e.g., gunicorn).

**Why:**
The default Flask server is not suitable for production environments.

**Benefit:**
Improves performance, scalability, and reliability.

## Improvement 2: Hardcoded default SECRET_KEY

**What was wrong:**
A default insecure SECRET_KEY ("supersecret123") was used if environment variable was not set.

**Why it is a problem:**
This creates a security vulnerability and makes the application predictable.

**How I fixed it:**
Removed the default value and enforced SECRET_KEY via environment variables.

**What could go wrong if left unfixed:**
Security breaches, session hijacking, and compromised application integrity.

## Improvement 3: Missing global error handling in service-a

**What was wrong:**
The application did not handle exceptions globally.

**Why it is a problem:**
Unhandled exceptions result in default Flask error pages and lack of proper logging.

**How I fixed it:**
Added a global error handler to return structured JSON responses and log errors.

**What could go wrong if left unfixed:**
Poor debugging experience, inconsistent API responses, and potential exposure of internal details.



## Improvement 3: Secure and structured infrastructure configuration

**What was wrong:**
Refactored the Terraform configuration by removing hardcoded AWS credentials, introducing variables for configurable values, adding resource tagging, defining outputs, organizing code into multiple files (main.tf, variables.tf, outputs.tf), and adding a basic security group.

**Why it is a problem:**
The original configuration had security risks (hardcoded credentials), lacked flexibility (hardcoded values), and was incomplete (missing tags, outputs, and proper structure). This makes the infrastructure difficult to manage and unsafe.

**What could go wrong if left unfixed:**
Improves security by removing sensitive data from code, enhances flexibility and reusability through variables, enables better resource management with tagging, provides useful outputs, and aligns the setup with Terraform best practices for maintainability and scalability.


## Improvement 4: Production-ready deployment configuration

**What was wrong:**
The original configuration lacked health checks, resource limits, and proper scaling, making it unreliable and not production-ready.

**What I improved:**
Enhanced the Kubernetes deployment by adding readiness and liveness probes, defining resource limits, replacing the latest image tag with a versioned tag, introducing environment variables, increasing replicas, and improving service configuration. 

**Benefit:**
Improves application reliability, enables self-healing, ensures better resource management, supports scalability, and aligns with Kubernetes best practices.

## Improvement 5: Structured and secure pipeline

**What I improved:**
Enhanced the GitHub Actions workflow by defining proper triggers, structuring build steps, adding Docker image build and push, and using GitHub secrets for secure credential management.

**Why:**
The original workflow lacked proper structure, security practices, and complete CI/CD steps, making it unreliable and insecure.

**Benefits:**
Improves automation, ensures secure handling of credentials, enables reproducible builds, and aligns the pipeline with standard CI/CD best practices.   


