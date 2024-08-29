# LLM Pipeline using Vext.app

This project demonstrates how to build and integrate a Language Model (LLM) pipeline using the Vext.app platform. The pipeline involves making API requests, processing queries, and utilizing custom tokens to manage endpoints.

## Table of Contents
- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)
- [License](#license)

## Introduction

This project showcases how to interact with the Vext.app API to process queries through a custom LLM pipeline. The project integrates HTTP requests with dynamically generated tokens, allowing flexible and secure communication between the client and the Vext.app platform.

## Prerequisites

Before running this project, ensure you have the following installed:

- Python 3.x
- `pip` (Python package installer)
- `requests` library
- `python-dotenv` library
- Access to Vext.app

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/0xPriyanshuJha/RAGPlummberr
    cd RAGPlummberr
    ```

2. **Install the required Python packages:**
    ```bash
    pip install requests python-dotenv
    ```

## Configuration

1. **Set up your environment variables:**

    Create a `.env` file in the root directory of your project and add your API key:

    ```plaintext
    API_KEY=your_actual_api_key
    ```

2. **Update the `channel_token` and `endpoint_id` in the script:**

    Edit the Python script to include your specific `channel_token` (a unique identifier, such as a user ID) and `endpoint_id` provided by Vext.app:

    ```python
    channel_token = "your_unique_token"
    endpoint_id = "your_endpoint_id"
    ```

## Usage

Run the script to process a query through the LLM pipeline using Vext.app:

```bash
python your_script_name.py
```


<img width="1128" alt="image" src="https://github.com/user-attachments/assets/f5aead96-d332-414f-8101-9db95bec3db7">

<img width="1200" alt="image" src="https://github.com/user-attachments/assets/11c04938-c740-4082-8fab-819ea1d428b7">
