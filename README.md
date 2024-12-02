Low Stock Alert Notification Script for ERPNext
This script automates low stock alerts in ERPNext by notifying Manufacturing Managers when inventory items fall below a predefined threshold. Notifications are sent via email, SMS, and in-app alerts to ensure prompt action is taken.

Features
1. Inventory Monitoring
Automatically checks the tabBin table for items with a stock quantity (actual_qty) below 5.
2. Stakeholder Notifications
Identifies users with the "Manufacturing Manager" role in ERPNext.
Sends notifications through:
Email: A detailed HTML table listing low-stock items.
SMS: A concise alert message using the TextLocal API.
In-App Notifications: Displays alerts in ERPNext’s Notification Log.
3. Activity Logging
Logs SMS details into the SMS Log doctype for traceability.
Creates Notification Log entries for easy access and follow-up.
Prerequisites
ERPNext Setup: Ensure your ERPNext instance is configured with the following doctypes:
tabBin (for inventory data)
tabUser (for user details)
Notification Log (for in-app alerts)
SMS Log (for SMS activity)
TextLocal API Credentials:
Obtain an API key and sender ID from TextLocal.
Installation & Configuration
Add the Script:

Copy and paste the script into your ERPNext custom app or server script.
Update the TextLocal API Details:

Replace the apikey and sender variables in the script with your TextLocal API credentials.
Schedule the Script:

Use ERPNext’s Scheduler to run the script periodically (e.g., daily or hourly).
Customize Threshold:

Modify the stock threshold (actual_qty < 5) in the SQL query to suit your inventory policy.
Usage
Run the Script:

Execute manually or wait for the scheduled job.
Notifications:

Check the email inboxes and SMS messages of Manufacturing Managers.
View in-app alerts in ERPNext’s Notification Log.
Review Logs:

Verify SMS delivery status in the SMS Log doctype.
Example Output
Email Notification
A detailed table like this will be sent to Manufacturing Managers:
----------------------------------------------------|
Item Code  |	Available Quantity	| Warehouse  |
____________________________________________________
ITEM001	   |        2	            | Main Store    |
ITEM002	   |        4	            | Secondary     |
_____________________________________________________
SMS Notification
A concise alert message like this will be sent:

"Low Stock Alert: Some items are below the minimum stock level. Please check your email for details."

Contributing
We welcome contributions to enhance this script. To contribute:

Fork the repository.
Create a new branch for your feature or bug fix.
Submit a pull request.
License
This project is open-source and distributed under the MIT License. Feel free to use and modify it as needed.

Contact
For questions or support, please open an issue in this repository or reach out to us directly.
