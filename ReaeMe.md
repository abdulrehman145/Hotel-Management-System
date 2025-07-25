# Voice-Based Drive-Thru Ordering System

This Python project simulates a **voice-interactive drive-thru ordering system**. It uses the `pyttsx3` text-to-speech engine to interact with the customer and records each order in a daily log file based on the current date. The system allows customers to place single or multiple orders and calculates the total bill automatically.

**Features**

  - Voice-based interaction using pyttsx3
  - Accepts and confirms customer orders via text and speech
  - Supports multiple items per order
  - Calculates and announces the total bill
  - Automatically saves order details to a file named with the current date
  - Uses dictionaries for dynamic pricing and menu handling

**Technologies Used**

  - Python
  - pyttsx3
  - datetime

**Requirements**

Install the required library:

    pip install pyttsx3

**Run the App**

    python drive_thru.py

**Sample Menu (Hardcoded)**

  - Coffee   Rs. 150
  - Burger   Rs. 300
  - Drink    Rs. 70
  - Pizza    Rs. 1800

**Output Example**

  - Creates a text file like 2025-07-25.txt
  - Appends order details with timestamp and bill

**Future Improvements**

  - Add speech-to-text support using `speech_recognition`
  - Integrate live voice input via microphone
  - Connect to a GUI or terminal-based menu system
  - Add item customization (e.g., size, toppings)
  - Store user history for repeat orders
