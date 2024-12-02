<div>
    <h1>Low Stock Alert Notification Script for ERPNext</h1>
    <p>
        This script automates low stock alerts in ERPNext by notifying Manufacturing Managers 
        when inventory items fall below a predefined threshold. Notifications are sent via email, 
        SMS, and in-app alerts to ensure prompt action is taken.
    </p>
</div>
    <h2>Features</h2>
    <h3>1. Inventory Monitoring</h3>
    <p>Automatically checks the <code>tabBin</code> table for items with a stock quantity (<code>actual_qty</code>) below 5.</p>
<div>
    <h3>2. Stakeholder Notifications</h3>
    <p>Identifies users with the "Manufacturing Manager" role in ERPNext. Sends notifications through:</p>
    <ul>
        <li><strong>Email:</strong> A detailed HTML table listing low-stock items.</li>
        <li><strong>SMS:</strong> A concise alert message using the TextLocal API.</li>
        <li><strong>In-App Notifications:</strong> Displays alerts in ERPNext’s Notification Log.</li>
    </ul>
</div>
    <h3>3. Activity Logging</h3>
    <p>
        Logs SMS details into the <code>SMS Log</code> doctype for traceability.
        Creates Notification Log entries for easy access and follow-up.
    </p>
<div>
    <h2>Prerequisites</h2>
    <ul>
        <li><strong>ERPNext Setup:</strong> Ensure your ERPNext instance is configured with the following doctypes:
            <ul>
                <li><code>tabBin</code> (for inventory data)</li>
                <li><code>tabUser</code> (for user details)</li>
                <li><code>Notification Log</code> (for in-app alerts)</li>
                <li><code>SMS Log</code> (for SMS activity)</li>
            </ul>
        </li>
        <li><strong>TextLocal API Credentials:</strong> Obtain an API key and sender ID from <a href="https://www.textlocal.com/">TextLocal</a>.</li>
    </ul>
</div>
    <h2>Installation & Configuration</h2>
    <ol>
        <li><strong>Add the Script:</strong>
            <p>Copy and paste the script into your ERPNext custom app or server script.</p>
        </li>
        <li><strong>Update the TextLocal API Details:</strong>
            <p>Replace the <code>apikey</code> and <code>sender</code> variables in the script with your TextLocal API credentials.</p>
        </li>
        <li><strong>Schedule the Script:</strong>
            <p>Use ERPNext’s Scheduler to run the script periodically (e.g., daily or hourly).</p>
        </li>
        <li><strong>Customize Threshold:</strong>
            <p>Modify the stock threshold (<code>actual_qty &lt; 5</code>) in the SQL query to suit your inventory policy.</p>
        </li>
    </ol>
<div>
    <h2>Usage</h2>
    <ol>
        <li><strong>Run the Script:</strong>
            <p>Execute manually or wait for the scheduled job.</p>
        </li>
        <li><strong>Notifications:</strong>
            <p>Check the email inboxes and SMS messages of Manufacturing Managers. View in-app alerts in ERPNext’s Notification Log.</p>
        </li>
        <li><strong>Review Logs:</strong>
            <p>Verify SMS delivery status in the <code>SMS Log</code> doctype.</p>
        </li>
    </ol>
</div>
    <h2>Example Output</h2>
    <h3>Email Notification</h3>
    <p>A detailed table like this will be sent to Manufacturing Managers:</p>
    <table border="1" cellpadding="5" cellspacing="0" style="border-collapse: collapse; width: 100%;">
        <thead>
            <tr>
                <th>Item Code</th>
                <th>Available Quantity</th>
                <th>Warehouse</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>ITEM001</td>
                <td>2</td>
                <td>Main Store</td>
            </tr>
            <tr>
                <td>ITEM002</td>
                <td>4</td>
                <td>Secondary</td>
            </tr>
        </tbody>
    </table>
<div>
    <h3>SMS Notification</h3>
    <p>A concise alert message like this will be sent:</p>
    <blockquote>
        "Low Stock Alert: Some items are below the minimum stock level. Please check your email for details."
    </blockquote>
</div>
    <h2>Contributing</h2>
    <p>
        We welcome contributions to enhance this script. To contribute:
    </p>
    <ul>
        <li>Fork the repository.</li>
        <li>Create a new branch for your feature or bug fix.</li>
        <li>Submit a pull request.</li>
    </ul>
<div>
    <h2>License</h2>
    <p>This project is open-source and distributed under the MIT License. Feel free to use and modify it as needed.</p>
</div>
    <h2>Contact</h2>
    <p>
        For questions or support, please open an issue in this repository or reach out to us directly.
    </p>
</>
