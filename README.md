# PRODIGY_CS_01

# 🔐 Caesar Cipher Web Application

## Project Description
This project is a full-stack web application designed to demonstrate the implementation of the classic **Caesar Cipher** cryptographic algorithm. The application provides a user-friendly web interface for encrypting and decrypting text messages, showcasing a simple yet effective method of secure communication. The core functionality is built using Python, while the user-facing components are crafted with standard web technologies.

## Technology Stack
The application is developed using the following technologies:

* **Backend:**
    * **Python 3:** The programming language used for the core logic.
    * **Flask:** A lightweight and flexible Python web framework that handles server-side routing, request processing, and template rendering.

* **Frontend:**
    * **HTML5:** The markup language for structuring the web page.
    * **CSS3:** Used for styling the user interface, providing a clean and responsive design.

## Features
* **Intuitive User Interface:** A single-page application that is easy to navigate and use.
* **Message Encryption:** Encrypts an input message by shifting each letter by a specified numeric value.
* **Message Decryption:** Decrypts an encrypted message by reversing the shift operation.
* **Error Handling:** The application ensures that only valid input is processed, with non-alphabetic characters remaining unchanged during the cipher operation.
* **Dynamic Results:** Utilizes server-side templating to dynamically display the encrypted or decrypted text on the same page without a full page reload.

## Installation and Setup

### Prerequisites
Before running the application, ensure you have the following installed:
* Python 3.x
* `pip`, the Python package installer

### Step-by-Step Guide
1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/your-username/your-project-name.git](https://github.com/your-username/your-project-name.git)
    cd your-project-name
    ```

2.  **Install Dependencies:**
    The project relies on the Flask library. Install it by running the following command in your terminal:
    ```bash
    pip install Flask
    ```

3.  **Run the Application:**
    Navigate to the project's root directory and execute the main Python file.
    ```bash
    python app.py
    ```

4.  **Access the Application:**
    Once the server is running, open your web browser and navigate to the following URL:
    ```
    [http://127.0.0.1:5000](http://127.0.0.1:5000)
    ```

## Usage
* Enter the message you wish to encrypt or decrypt into the "Enter your message" text field.
* Specify a numeric "Shift value" to be used for the cipher.
* Click the "Encrypt" button to perform encryption or the "Decrypt" button to perform decryption.
* The result will be displayed dynamically on the page.

## Project Structure
````

caesar\_cipher\_app/
├── templates/
│   └── index.html         \# Frontend HTML template
└── app.py                 \# Backend Python code (Flask app)


## License
This project is open-sourced under the MIT License.

