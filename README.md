# Udemy Course Downloader

This project is a script to download Udemy courses for educational purposes. Use it responsibly and only with content you have rightful access to. This guide will walk you through the installation, setup, and usage of the script.

## Features
- Download videos and resources from Udemy courses.
- Simple and efficient command-line interface.
- Supports providing additional values (e.g., API keys, custom parameters) through command-line arguments.

---

## Prerequisites

Ensure you have the following installed on your system:

- Python 3.7 or higher

---

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/neeraj2234444/UDEMY-hack.git
   cd UDEMY-hack
   ```

2. **Install Required Libraries**
   Use the `requirements.txt` file to install all dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   The required libraries include:
   - `requests`
   - `bs4` (BeautifulSoup)
   - `selenium`
   - `argparse`
   - `os`

---

## Setup

1. **Set Up Selenium WebDriver**
   - Download the WebDriver compatible with your browser (e.g., ChromeDriver for Chrome).
   - Place the WebDriver in a directory included in your system's PATH or specify its path in the script.

2. **Login Credentials**
   - Update the script with your Udemy login credentials if required, ensuring to keep them secure.

---

## Usage

Run the script using the following command:
```bash
python udemy.py -u <UDMY_COURSE_URL> -d <DOWNLOAD_PATH> -v <VALUE>
```

### Arguments
- `-u` or `--url`: The URL of the Udemy course to download.
- `-d` or `--download`: The directory where the course content will be saved.
- `-v` or `--value`: Additional value such as API keys, login credentials, or specific parameters required by the script.

### Example
To download a course to a folder named `UdemyCourses` with an additional value:
```bash
python udemy.py -u https://www.udemy.com/course/python-for-beginners/ -d ./UdemyCourses -v API_KEY_12345
```

---

## Important Notes
- **Legal Compliance:** Ensure you have proper authorization to download content from Udemy.
- **Ethical Use:** This script is for educational purposes only. Misuse may lead to account suspension or legal actions.

---

## Contributing
Contributions are welcome! Feel free to fork the repository, make your changes, and submit a pull request.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
