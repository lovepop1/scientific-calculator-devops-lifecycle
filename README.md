# Scientific Calculator with a Full DevOps Lifecycle

This project is a hands-on demonstration of a complete DevOps pipeline, built around a simple Python command-line scientific calculator. The primary goal is not the calculator itself, but to showcase the integration of various industry-standard tools to achieve Continuous Integration (CI) and Continuous Deployment (CD).

The pipeline automatically tests, packages, and publishes the application, and a final manual step deploys it, all using an automated script.

---
## 🧮 Calculator Features

The application is a menu-driven scientific calculator with the following functions:
* **Square Root** (`√x`)
* **Factorial** (`x!`)
* **Natural Logarithm** (base e, `ln(x)`)
* **Power Function** (`x^b`)

---
## 🛠️ DevOps Toolchain

| Tool | Category | Role in this Project |
| :--- | :--- | :--- |
| **Git & GitHub** | Source Control Management | To track code changes and host the project's central repository. |
| **Jenkins** | Continuous Integration Server | To automate the entire pipeline from testing to publishing the Docker image. |
| **Docker** | Containerization Platform | To package the Python application and its environment into a portable image. |
| **Ansible** | Configuration Management | To automate the deployment of the Docker container to a target host. |

---
## 🚀 Pipeline Overview

This project implements a full CI/CD workflow:

1.  **Commit & Push:** A developer commits code changes to the GitHub repository.
2.  **Continuous Integration (CI):**
    * **Jenkins** automatically detects the push to the `main` branch.
    * It checks out the latest code.
    * It runs the **unit tests** inside a clean Python Docker container to ensure code quality.
    * If tests pass, it builds a new **Docker image** of the calculator application.
    * Finally, it pushes the newly built image to **Docker Hub** as a distributable artifact.
3.  **Continuous Deployment (CD):**
    * The **Ansible playbook** is run manually to connect to a target host.
    * Ansible pulls the latest version of the application image from Docker Hub.
    * It stops and removes any old running container.
    * It starts a new container from the latest image, completing the deployment.

---
## 🏁 Getting Started

To deploy and run this application using the automated Ansible playbook, you will need the following prerequisites installed on your machine:
* Git
* Docker
* Ansible

### Deployment Instructions

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/lovepop1/scientific-calculator-devops-lifecycle.git](https://github.com/lovepop1/scientific-calculator-devops-lifecycle.git)
    cd scientific-calculator-devops-lifecycle
    ```

2.  **Install the Ansible Docker Collection:**
    ```bash
    ansible-galaxy collection install community.docker
    ```

3.  **Run the Deployment Playbook:**
    This command will pull the image from Docker Hub and start the application container. You will be prompted for your `sudo` password.
    ```bash
    ansible-playbook -i inventory deploy.yml --ask-become-pass
    ```

4.  **Interact with the Calculator:**
    The container will be running. Attach your terminal to it to use the application:
    ```bash
    docker attach scientific-calculator-container
    ```

---
## 📂 Project Structure

```
.
├── calculator.py         # The core Python application
├── test_calculator.py    # Unit tests for the application
├── Dockerfile            # Instructions to build the Docker image
├── Jenkinsfile           # The CI pipeline-as-code script
├── inventory             # Ansible inventory file (defines target hosts)
├── deploy.yml            # Ansible playbook for deployment
├── requirements.txt      # Python dependencies (empty for this project)
└── README.md             # This file
```