def check_low_stock_and_notify():
    
    date =  frappe.utils.getdate();
    
    # Fetch items below the stock threshold
    items_below_threshold = frappe.db.sql("""
        SELECT item_code, actual_qty, warehouse
        FROM `tabBin`
        WHERE actual_qty < 5
    """, as_dict=True)

    # Fetch Manufacturing Managers
    manufacturing_managers = frappe.db.sql("""
        SELECT DISTINCT `tabUser`.email, `tabUser`.name, `tabUser`.mobile_no
        FROM `tabUser`
        INNER JOIN `tabHas Role` ON `tabUser`.name = `tabHas Role`.parent
        WHERE `tabUser`.enabled = 1
        AND `tabHas Role`.role = 'Manufacturing Manager'
    """, as_dict=True)

    if not items_below_threshold or not manufacturing_managers:
        return

    # Create HTML table for email content
    item_list = "".join([
        f"<tr><td>{item['item_code']}</td><td>{item['actual_qty']}</td><td>{item['warehouse']}</td></tr>"
        for item in items_below_threshold
    ])

    email_message = f"""
    <html>
        <body>
            <h3>Low Stock Alert</h3>
            <p>The following items are below the minimum stock threshold:</p>
            <table border="1" cellpadding="5" cellspacing="0" style="border-collapse: collapse; width: 100%;">
                <thead>
                    <tr>
                        <th>Item Code</th>
                        <th>Available Quantity</th>
                        <th>Warehouse</th>
                    </tr>
                </thead>
                <tbody>
                    {item_list}
                </tbody>
            </table>
        </body>
    </html>
    """

    sms_message = "Low Stock Alert: Some items are below the minimum stock level. Please check your email for details."

    # Send email notifications
    subject = "Low Stock Alert"
    recipients = [manager['email'] for manager in manufacturing_managers if manager['email']]
    if recipients:
        frappe.sendmail(recipients=recipients, subject=subject, message=email_message)

    # Send SMS notifications
    mobile_numbers = [manager['mobile_no'] for manager in manufacturing_managers if manager.get('mobile_no')]

    
    url = "https://api.textlocal.in/send/"
    
    apikey = "<your_key>"
    message = (
        "For job post name ERPNEXT, a selected candidate has accepted the opportunity. "
        "Please visit the link to complete the post formalities. The Job Plus Team"
                )
    numbers =   mobile_numbers
    sender = "JOBPLS"
    
    data = {
        "apikey": apikey,
        "message": message,
        "numbers": numbers,
        "sender": sender,
    }
        
    response = frappe.make_post_request(url, data=data)
    status = response['status']

    if status == 'success':
        for manager in manufacturing_managers:
            if manager.get('mobile_no'):  
                try:
                    # Create a new SMS Log document
                    sms_log = frappe.get_doc({
                        'doctype': 'SMS Log',
                        'sent_to': manager['mobile_no'], 
                        'message': message,
                        'no_of_requested_sms': 1,
                        'requested_numbers': manager['mobile_no'],
                        'no_of_sent_sms': 1,  
                        'status': 'Sent',
                        'sent_on': date
                    })
                    sms_log.insert(ignore_permissions=True)  
                    frappe.db.commit()  
                except Exception as e:
                    frappe.log_error(f"Error sending SMS to {manager['mobile_no']}: {e}", "SMS Log Error")


    # Create notifications in Notification Log
    for manager in manufacturing_managers:
        notification_message = f"""
        <h3>Low Stock Alert</h3>
        <p>The following items are below the minimum stock threshold:</p>
        <table border="1" cellpadding="5" cellspacing="0" style="border-collapse: collapse; width: 100%;">
            <thead>
                <tr>
                    <th>Item Code</th>
                    <th>Available Quantity</th>
                    <th>Warehouse</th>
                </tr>
            </thead>
            <tbody>
                {item_list}
            </tbody>
        </table>
        """
        notification = frappe.get_doc({
            'doctype': 'Notification Log',
            'for_user': manager['name'],
            'subject': subject,
            'email_content': notification_message,
            'type': 'Alert'
        })
        notification.insert(ignore_permissions=True)
        


check_low_stock_and_notify()
